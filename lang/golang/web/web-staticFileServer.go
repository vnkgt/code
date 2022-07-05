//=>golang实现静态文件服务器
package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("web-staticFileServer start running")
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		//浏览器请求127.0.0.1:8080/src/img/01.jpg--->则
		http.ServeFile(w, r, r.RequestURI[1:])
	})
	http.ListenAndServe(":8080", nil)
	// http.ListenAndServe(":8080", http.FileServer(http.Dir("/src/img/")))
}
