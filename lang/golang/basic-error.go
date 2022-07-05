/*
=>golang中的错误处理
	golang的错误内置数据类型:	error
	golang中函数可以有多个返回值=>最后一个返回值应该“返回错误信息”,无错误信息返回“nil”
	1)逻辑判断=>写代码时从逻辑上处理可能出现的错误,代码保护
	2)创建新的错误类型
		//errorMsg:错误信息
		errors.New(<errorMsg>)
	3)panic错误
		//panicMsg:错误信息
		panic(<panicMsg>)
	4)直接退出程序
		os.Exit(1)
	错误处理方法使用的优先级:
		逻辑判断->errors.New()->panic->os.Exit(1)
		//errors.New()与panic均会在执行defer延迟操作后结束;os.Exit(1)则是直接退出程序,不会执行defer
=>defer延迟关键词
	//保证无论是否有panic,都会在函数结束前执行sentence,能够及时释放掉资源
	defer <sentence>
=>recover恢复异常状态
	recover()
*/
package main
import (
	"fmt"
	"errors"
	"os"
)

//errors.New()
func assignArg2Slice(listArg []string,index int,value string) error{							//给listArg赋值
	if (index<0 || index>=10){return errors.New("out of listArg range...赋值失败")}	//超过slice的长度
	listArg[index] = value
	return nil		//正常赋值成功
}
//os.Exit(1)
func judgeFlag(danger bool){
	if danger==true{
		fmt.Println("have same danger happening...force stop and exit process")
		os.Exit(1)
	}
	fmt.Println("there is no danger...process is safe")
}
//recover异常状态恢复
func saveDivide(num1, num2 int) int {
	defer func() {
	   fmt.Println("saveDivide 异常...",recover())
	}()
	quotient := num1 / num2
	return quotient
 }
func main(){
	//error
	fmt.Println("errorhandle.....................errors.New()")
	/*
	var listArg = make([]string,10)	//创建一个slice
	fmt.Println("src slice",listArg)
	fmt.Println(assignArg2Slice(listArg,12,"aaaa"))
	fmt.Println("assign before slice",listArg)
	*/

	//panic
	fmt.Println("\n\nerrorhandle.....................panic()")
	/*
	defer func(){					//创建函数后立即调用
		fmt.Println("befor panic")
	}()
	panic("panic=>forget pwd")
	*/

	//os.Exit(1)
	fmt.Println("\n\nerrorhandle.....................os.Exit(1)")
	// judgeFlag(true)
	// fmt.Println("false to run os.Exit(1)")

	//recover()异常状态恢复
	fmt.Println("\n\nerrorhandle.....................recover()")
	fmt.Println("saveDivide return value...",saveDivide(1,0))
	fmt.Println("saveDivide return value...",saveDivide(10,10))
}