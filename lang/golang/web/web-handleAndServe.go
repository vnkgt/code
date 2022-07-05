/*
web编程的流程:
	客户端client	=>	服务器server
	1.server:创建监听器,服务器
	2.handleAndProcess:创建不同url地址的处理函数
		handle:匹配器,主要指“匹配url与函数”
			eg:	localhost:8080/		=>	retIndex(),返回index.html页面
				localhost:8080/setting	=> 	retSetting(),返回setting.html页面
		process:处理器,函数功能的实现
			eg:	retIndex()	=>	实现返回index.html页面的具体流程
				retSetting()	=>	实现返回settting.html页面的具体逻辑
		routing:路由
			eg:	客户端的请求
				url地址"localhost:8080/"		=>	路由"/"
				url地址"localhost:8080/index"	=>	路由"/index"
				url地址"localhost:8080/setting/name"	=>	路由"/setting/name"
		绑定相应的routing与对应的handle函数
		1)返回对应的html页面:
			html与客户端的数据交换
		2)数据库处理:database
			储存客户端的相关请求
		3)中间件:middleware
	3.listenAndServer:开启监听器
		开启前一定要在之前写好对应的handleAndProcess,否则客户端的请求没有对应的出路逻辑
	4.waitForClient:等待客户端访问
		request:client发来的请求(包含客户端的ip,请求类型等信息)
	5.serve2Client/retSrc:将服务器server主机中的对应资源返回给客户端client
		response:服务器返回给client的数据
	6.循环"步骤4-5"


=>golang中的web编程
	监听器server	=>	http.Server结构体对象
		//创建http.Server结构体
			<server> = http.Server{			//server监听器名
				Addr:	<ip:port>,			//server绑定的ip:port,"localhost:8080"表示本地8080端口
				Handler:	<handleFunc>	//http.Handle函数,"nil->http.DefaultServerMux"
			}
		//开启http监听器
			<server>.ListenAndServer()
		//开启https监听器
			<server>.ListenAndServerTLS()
		//创建并开启server
			http.ListenAndServer(<ip:port>,<handleFunc>)
			http.ListenAndServerTLS(<ip:port>,<handleFunc>)
	处理器handle	=>	Handler接口
		handle=>动词,是方法或函数,一个过程
		handler=>名称,是结构体或者类型转换方法,一个对象
		区分http.Handler接口,http.Handle处理方法,http.HanleFunc处理函数:
			http.Handler	=>	一个接口
			http.Handle()	=>	一个将“对应url与对应方法相关联”的函数
			http.HandleFunc()	=>	一个将“对应routing与对应函数相关联”的函数
			Handle()与HandleFunc()基本逻辑是相同的只有些许不同:
				Handle():返回一个“结构体对象中的"ServeHTTP"方法”
				HandleFunc():返回一个“满足http.ServeHTTP()参数形式函数”
				//无论是方法还是函数,其实现参数中必须要有以下两个参数
					<writer> http.ResponseWriter
					<requester> *http.Request
		//http.Handler接口源码
			type Handler interface{
				ServeHTTP(ResponseWriter,*Request)		//ResponseWriter:写数据;Request:客户端的请求
			}
		//http.Handle()通过调用方法实现process
		//patter:要匹配的url地址,不包含ip:port
		//handler:对应的处理方法,一般由自己重写
			一般要自定义一个结构体对象,该对象需要有“ServeHTTP”方法,程序运行时会自动调用该方法;若没有该方法,http.Handle会报错
			http.Handle(<patter> string,<handler> http.Handler)
		//将满足接口形式的“函数(非方法)”转换为http.HandlerFunc()
		//http.HandleFunc()通过调用函数实现process
		//func(ResponseWriter, *Request):一个函数类型
			http.HandleFunc(<patter> string,<handler> func(http.ResponseWriter, *http.Request))
	内置的http.Handler	=>	自带的url处理对象,“方法”(非“函数”)
		//给每个请求都响应“404 page not found”
			http.NotFoundHandler()	Handler
		//重定向至url
		//code:跳转的状态码,常见的有StatusMovedPermanently,StatusFound,StatusSeeOther
			http.RedirectHandler(<url> string,<code> int) Handler
		//去掉请求中指定的prefix前缀,再返回h; 匹配不到prefix则返回404
			http.StripPrefix(<prefix> string, <h> Handler) Handler
		//限制请求的时间,h运行超过dt则报信息msg
			http.TimeoutHandler(<h> Handler,<dt> time.Duration,<msg> string) Handler
		//静态文件服务器
			http.FileServer(<root> FileSystem) Handler
			使用时需要用到操作系统的文件系统:
				type Dir string
				func(<d> Dir)Open(<name> string) (File,error)	//满足FileSystem接口
			eg:	实现静态文件服务器,请求的url直接与root中的同名文件相对应
				http.ListenAndServe("<ip>:<port>",http.FileServer(http.Dir(<root>)))
			//FileSystem接口源码
				type FileSystem interface{
					Open(name string) (File,error)
				}
			//文件返回“函数”,返回root对应的文件
				http.ServeFile(<w> http.ResponseWriter,<r> *http.Request,<name> string)
*/
package main

import (
	"fmt"
	"net/http"
)

//自定义的muxStruct结构体
type muxStruct struct{ name string }

//实现http.Handle接口中的ServeHTTP方法以满足接口
func (mux *muxStruct) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("=>this is muxStruct.ServeHTTP"))
	w.Write([]byte("\nrequest url:" + r.Host + r.RequestURI))
}

//muxHTTP函数满足http.ServeHTTP()函数中的参数形式
func muxFunc(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte(`=>this is muxFunc`))
	w.Write([]byte("\nrequest url:" + r.Host + r.RequestURI))
}

func main() {
	//1.创建监听器server
	serverObj := http.Server{
		Addr:    "localhost:8080",
		Handler: nil, //表示http.DefaultServerMux
	}

	//2.配置handle
	http.Handle("/index", &muxStruct{name: "index"})   //"/index"的路由,自动调用muxStructObj.ServeHttp方法
	http.HandleFunc("/home", muxFunc)                  //"/home"的路由,关联路由与muxHome函数
	http.Handle("/setting", http.HandlerFunc(muxFunc)) //"/setting"的路由,将"handle函数"转换为"handle方法"
	//测试内置的Handler
	http.Handle("/404", http.NotFoundHandler())                                       //404
	http.Handle("/baidu", http.RedirectHandler("http://baidu.com", http.StatusFound)) //重定向
	http.Handle("/src/img", http.StripPrefix("/src", &muxStruct{name: "srcImg"}))     //去掉请求中指定的prefix前缀
	http.TimeoutHandler(&muxStruct{name: "outOfTime"}, 1000, "out of time limit")     //限制请求的时间
	http.HandleFunc("/src/img/01.jpg", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, r.RequestURI[1:]) //r.RequestURI即为“/src/img/01.jpg”
	}) //返回“/src/img/01.jpg”
	//默认handler
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Default-->\n" + "request url:" + r.Host + r.RequestURI))
	})
	//3.开启监听器
	fmt.Println("serve starting...")
	serverObj.ListenAndServe()
}
