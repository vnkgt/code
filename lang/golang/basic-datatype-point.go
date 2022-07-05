/*
=>golang中的指针:
	//声明
	var <argName> *<datatype>
	//取地址
	//pointName:指针变量名
	&<pointName>
	//取值
	*<pointName>
===>golang中指针可以指向的对象:
	变量(var)、数组(list)、切片(slice)、映射(map)、结构体(struct)、函数(func)、接口(interface)
	//指向函数时
		//pointName:函数名
		//arg:函数的参数
		//datatype:参数的类型
		//retDatatype:函数的返回值类型
		var <pointName> func(<arg> <datatype>) <retDatatype>
*/
package main

import (
	"fmt"
)


func funcArg(argA, argB string) string{	//定义一个函数,返回值类型为func()
	return argA+"...And..."+argB+"=>this is funcArg"
}

func main() {
	fmt.Println("指针指向普通数据类型...............")
	//指针指向,普通数据类型
	var strArg = "hello word"
	var strP *string
	strP = &strArg
	fmt.Println("strP:",strP)	//指针的值
	fmt.Println("strP addr:",&strP)	//指针的地址
	fmt.Println("strP value:",*strP)	//指针的值


	fmt.Println("\n\n指针指向结构体.............")
	//指针指向,结构体
	type peo struct{	//定义结构体peo
		name string
		age  int
	}
	var peoArg = peo{name:"小明",age:15}
	var peoP *peo
	peoP = &peoArg
	fmt.Println("peoP:",peoP)	//指针的值
	fmt.Println("peoP addr:",&peoP)	//指针的地址
	fmt.Println("peoP value:",*peoP)	//指针的值


	fmt.Println("\n\n指针指向函数..............")
	//指针指向函数
	var funcP func(argA,argB string) string
	funcP = funcArg
	fmt.Printf("调用funcP指向的函数:%v\n",funcP("aaa","bbb"))


	fmt.Println("\n\n接口指针..............")
	//接口指针实现泛型
	// var interfP interface{}
	// interfP = &strArg
	// fmt.Printf("%T\n",interfP.strArg)

	fmt.Println("func main over!")
}
