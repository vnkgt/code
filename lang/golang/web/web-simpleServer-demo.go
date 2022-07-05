/*
	web服务器处理的大致流程:
		客户端http请求->服务器总路由->服务器子路由->返回数据
		总路由->处理访问“根url”的请求:
			https://vnkgt.com/*
			https://baidu.com/*
		子路由->处理访问“子url”的请求:
			https://vnkgt.com/home/*
			https://baidu.com/news/tec/*
	1.创建http监听器,等待url
	//创建监听器,绑定相应的端口,并监听客户端的请求
	http.ListenAndServer()
	2.设置路由(对应url的处理方法/函数/返回值)->route
*/
package main

import (
	"fmt"
	"net/http"
)

func main() {
	//2.配置handle处理方法->路由route
	//http.HandleFunc:处理相应路由地址的请求
	//http.HandleFunc(<route>,<handleFunc>)
	//http.ResponseWriter:向客户端服务,写客户端请求的返回数据,返回对象
	//http.Request:标记请求客户端的地址
	//"/"->"localhost:8080/*",主路由
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hello word"))
	})
	fmt.Println("running...")
	//1.创建监听器,并等待客户端请求,为阻塞状态;若在handle之前创建,则不会运行相应的handle
	//nil表示http.DefaultServeMux,默认主路由
	http.ListenAndServe("localhost:8080", nil)
}
