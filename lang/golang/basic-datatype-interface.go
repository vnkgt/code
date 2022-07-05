/*
=>golang中的接口interface{}:
===>接口:golang实现“面对对象编程中的类class方法”封装
	//接口interface的作用:“相当于面对对象编程中的class类对象”,将一个“自定义的数据类型”的所有处理方法“打包”
	//<selfDatatype>---接口interface--->打包selfDatatype的所有方法{<methon>,}
	//selfDatatype:自定义的数据类型,一般是结构体struct、type关键字定义的数据类型
	//infName:接口名,class类名
	//methon:selfDatatype的方法,class类的方法
	//methonArg:methon方法的参数
	//methonRetDatatype:selfDatatype方法的返回值,class类方法的返回值
	var <infName> interface{									//infName:接口名,class类名
		<methon>(<methonArg> <datatype>)	<methonRetDatatype>	//methon:selfDatatype的方法,class类的方法
	}															//methonRetDatatype:selfDatatype方法的返回值,class类方法的返回值

===>接口还原,接口断言
	接口还原成底层的数据类型,即操作对象本身,相当于python中"class的__init__属性"
	//是一个断言,有返回值
	//infName:接口名
	//bottomDatatype:底层的数据类型,int/*int/string/*string/func() int/*func() int
	<infName>.(<bottomDatatype>)
	//获取arg的数据类型
	reflect.TypeOf(<arg>)
*/
package main

import (
	"fmt"
	"strconv"
	"reflect"
)

//自定义的数据类型(类对象),selfDatatype
type tankClass struct {
	tankName string
}

//封装tankClass所有的方法,并重命名为tank
type tank interface {
	fixTank(fixTime int) string //tankClass的方法;	fixTank:方法名;	fixTime:方法的参数;	string:方法的返回值
	runTank(runAim string) string
}

//方法fixTank的实现
func (m tankClass) fixTank(fixTime int) string {
	return m.tankName + "=>修车tank时间->" + strconv.Itoa(fixTime)
}

//方法runTank的实现
func (m tankClass) runTank(runAim string) string {
	return m.tankName + "=>跑tank目的地->" + runAim
}

func main() {
	var t tank //tankClass的实例对象,需要使用“封装后的接口tank”作为数据类型
	t = tankClass{tankName: "代非驻号"}
	fmt.Println("维修时间:", t.fixTank(12))
	fmt.Println("跑目的地:", t.runTank("解放日本"))

	fmt.Println("\n\n还原接口的数据类型..........")
	//接口接收后,还原成原
	var infE interface{}	//空接口
	type peo struct{		//定义结构体peo
		age int
		name string
	}
	p1 := peo{age:12,name:"小明"}	//创建peo类型的变量p1
	infE = p1						//用接口接收p1
	fmt.Printf("infE datatype:%v\n",reflect.TypeOf(infE))		//获取接口的底层数据类型
	fmt.Printf("src var p1.age:%v\n",p1.age)					//打印原始数据p1.age
	fmt.Printf("infE judge:%v\n",infE.(peo).name)				//接口断言为peo数据类型,并打印peo数据类型的name属性
	
}
