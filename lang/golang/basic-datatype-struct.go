/*
=>golang中的结构体struct:
	//golang中struct---类似--->clang中struct
	//golang中的struct一般与定义“方法methon”一起使用
	struct的声明:
		//struct的隐式声明
		var <argName> = struct{
			<structArg>	<datatype>
			<arg>	<datatype>
		}
		//struct的type关键字定义,复用性更强,一般使用该方法
		//structName:struct结构体的名字
		//structArg:“struct结构体内”的变量名
		type <structName> struct{
			<structArg>	<datatype>
			<structArg>	<datatype>
		}
	struct变量的声明:
		//argName:变量名
		//structName:struct结构体的名字
		var <argName> <structName>
	struct的调用:
		//structArg:“struct结构体内”的变量名
		<argName>.<structArg>
	struct的赋值:
		//方法一:逐一赋值
		//argName:变量名

		<argName>.<structArg> = <value>
		//方法二:位置参数赋值
		//structName:struct结构体的名字
		<argName> = <structName>{<value>,<value>,}
		//方法三:关键字参数赋值
		<argName> = <structName>{
			<structArg> : <value>,
			<structArg> : <value>,
		}
	struct的组合:
		//struct的组合:结构体---内部变量--->结构体
		//struct组合的声明
		//structName:struct结构体的名字
		//structArg:“struct结构体内”的变量名
		//structDatatype:struct类型的数据类型,由其它type所定义
		//datatype:普通数据类型,eg:int,string,rune
		type <structName> struct{
			<structArg> <datatype>
			<structArg> <structDatatype>	//组合:此处使用了其它结构体
		}
	struct的内嵌:
		//struct的内嵌:结构体---内部变量--->结构体,与struct的组合类似,“是struct组合的简写”
		//struct组合的声明
		//structName:struct结构体的名字
		//structArg:“struct结构体内”的变量名
		//structDatatype:struct类型的数据类型,由其它type所定义
		//datatype:普通数据类型,eg:int,string,rune
		type <structName> struct{
			<structArg> <datatype>
			<structDatatype>		//内嵌:此处简写变名,structDatatype既是“数据类型”又是“变量名”
			int						//内嵌:可以直接内嵌golang自带的“数据类型”int
			string					//内嵌:可以直接内嵌golang自带的“数据类型”string
		}

*/
package main

import (
	"fmt"
)

/*结构体声明区*/
//隐式声明
var kid struct {
	name string
	age  int
}

//type关键字定义struct
type location struct { //位置
	province string //省份
	city     string //市
}

type position struct { //坐标
	x int
	y int
}

type peopel struct { //人的信息
	name     string   //姓名
	age      int      //年龄
	loc      location //位置,组合
	position          //坐标,嵌入：直接使用“position结构体”
}

func main() {
	//逐一赋值
	kid.name = "小明"
	kid.age = 16
	fmt.Println("参数逐一赋值=>kid", kid)

	//关键字参数赋值
	var pe0 = peopel{
		name:     "小刚",
		age:      15,
		loc:      location{province: "湖北", city: "天门"}, //组合:赋值
		position: position{x: 222, y: 333},             //内嵌:赋值
	}
	fmt.Println("关键字参数赋值=>pe0", pe0)

	//结构体数组
	var provs = []location{
		{province: "湖北", city: "武汉"},
		{province: "湖北", city: "天门"},
		{province: "湖北", city: "潜江"},
		{province: "湖北", city: "仙桃"},
		{province: "湖北", city: "荆门"},
		{province: "湖北", city: "十堰"},
	}
	fmt.Println("结构体数组=>procs", provs)
}
