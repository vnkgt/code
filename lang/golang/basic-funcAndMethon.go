/*
=>golang的type:
	//相当于c语言中的"typedef",相当于起别名
	//srcojb---别名--->aimobj
	//aimobj:目标对象
	//srcobj:源对象
	type <aimobj> <srcobj>
=>golang函数和方法:
	1.函数:
		1)函数的声明
			1.1)"单个参数,单个返回值"
				//funcName:函数名
				//funcName:		小写开头=>只能同一个文件中调用,大写开头=>可以在不同的文件中调用
				//arg:传递给函数的参数
				//retDatatype:返回值类型
				//datatype:数据类型
				func <funcName>(<arg> <datatype>) (<retDatatype>){
					sentence
				}
			1.2)"多个个参数"
				func <funcName>(<arg01> <datatype01>,<arg02> <datatype02>) (<retDatatype>){
					sentence
				}
			1.3)"多个返回值",多个返回值时必须用相同个数的变量接收
				func <funcName>(<arg> <dataType>) (<retDatatype01>,<retDatatype02>)(
					sentence
				)
			1.4)闭包:参数个数不定函数
				//"...":表示参数的个数不定,可以有一个也可以有多个
				func <funcName>(arg ...<datatype>) <retDatatype>{
					sentence
				}
				eg:
					//interface{}:表示“空接口”,具体类型由实参而定
					func Println(a ...interface{}) (n int,err error)
			1.5)函数作为参数
				//funcPoint:指向函数的一个变量,或者就是“函数名”本身
				func <funcName>(<funcPoint> func() <funcRetType>)	<retDatatype>{
					sentence
				}
			1.6)函数作为返回值
				//retFuncDatatype:返回函数的数据类型
				func <funcName>(<arg> <datatype>) func() <retFuncDatatype>{
					pass
				}
			1.7)匿名函数
				//argName:变量名,“指向一个函数”
				var <argName> = func(<arg> <datatype>){
					sentence
				}

		2)函数的调用
			2.1)直接调用,“把函数执行的值返回”
				//argName:接受的变量名
				var <argName> = <funcName>(<arg>)
			2.2)赋值给变量,“返回函数本身”
				//argName:变量名
				//funcName:函数名
				var <argName> = <funcName>
				<argName> := <funcName>
			2.3)“函数返回的值”是“函数”
				var <argName> = <funcName>(<arg>)
		3)其它注意点
			3.1)函数的内部不能有函数的嵌套:即函数里面不能够声明函数
				eg:	//该代码会报错
					fun funcOut() {
						fun funcIn(){<sentence>}
					}



	2.方法:
		//相当于class对象中封装的方法
		//对"type定义的变量类型"起作用,不允许对int,float,string等预声明定义方法
		1)方法的声明
			1.1)"单个参数,单个返回值"
				//mainCustomDatatype:被操作的对象类型,一般是自定义的数据类型
				//obj:被操作对象
				//methonName:方法名
				//arg:方法的参数
				//datatype:数据类型,可以是内置类型(int,string等),也可以是自定义的数据类型(eg:type tenBase int--->tenBase)
				//retDatatype:返回的对象类型,可以是内置对象,也可以是自定义对象
				//mainCustomDatatype对象---methonName方法---datatype参数--->retDatatype
				func(<obj> <mainCustomDatatype>)<methonName>(<arg> <datatype>) (<retDatatype>){
					sentence
				}
			1.2)"多个参数arg"
				func(<obj> <mainCustomDatatype>)<methonName>(<arg01> <datatype>,<arg02> <datatype>){
						sentence
					}
			1.3)无返回值
				func(<obj> <mainCustomDatatype>)<methonName>(<arg> <datatype>){
						sentence
					}
				eg:
					type num int
					func(n1 num) addNum(n2 num) num{
						return n1+n2
					}
		2)方法的调用
				//mainCustomDatatype:被操作的对象类型,一般是自定义的数据类型
				//retDatatype:返回的对象类型
				<retDatatype> = <mainCustomDatatype>.<methon>(<arg>)

===>解包:	将"列表list/切片slice"中的“每一个元素传递给函数”,而非列表本身传递给函数
	闭包:	将多个参数以“列表list/切片slice的形式”整合成一个整体传递
	传递参数时解包:
		//funcName:要调用的函数名
		//traverObj:可遍历对象,包括“列表list,切片slice”
		//"...":表示解包
		<funcName>(<traverObj> ...)
	函数中解包:
		//使用for-range进行遍历解包
		//arg:变量名
		//datatype:变量arg的数据类型
		//retDatatype:函数返回值
		func(<arg> ... <datatype>)<retDatatype>{
			for <trvObj> := <arg>{
				index := <trvObj>		//列表的索引
				value := <arg>[trvObj]	//列表的值
			}
		}

*/
package main

import (
	"fmt"
)

//1.1)函数:单个参数单个返回值
func noHandle(s string) string {
	return (s + "=>The ext")
}

//1.2)函数:多个参数
func add2Num(n1 int, n2 int) int {
	return (n1 + n2)
}

//1.3)函数:多个返回值
func divNum(n int) (int, int) {
	return n / 2, n % 2
}

//1.5)函数:函数作为参数
func funcArg(s string, funcName func() string) string {
	return funcName() + "=>" + s
}

func funcArgAssist() string {
	return "retfuncArg"
}

//1.6)函数:函数做返回值
func funcAsRet() func() string {
	return funcAsRetAssist
}

func funcAsRetAssist() string {
	return "函数作返回值"
}

//1.7)函数:匿名函数
var hidefunc = func(s string) string {
	return s + "<=this is hidefunc"
}

//方法
type num int //自定义数据类型"num"
func (n num) addNum(n1 num) num {
	return n + n1
}

//main函数
func main() {
	//函数调用
	rf1 := noHandle("你好") //1.1)
	fmt.Println("func01 noHandle...", rf1)

	rf2 := add2Num(2, 7) //1.2)
	fmt.Println("func02 add2Num...", rf2)

	rf3_1, rf3_2 := divNum(7) //1.3)
	fmt.Println("func03 divNum...", rf3_1, rf3_2)

	funcpoint := funcArgAssist                    //1.5)	funcpoint:“指向”函数的变量
	rf4 := funcArg("aaa", funcpoint)              //funcpoint:传递变量指向的函数,函数做参数
	fmt.Println("func05 函数作参数", funcpoint(), rf4) //funcpoint():调用funcpoint指向的函数

	rf6 := funcAsRet
	fmt.Println("func06 函数作返回值", rf6(), "执行结果:", rf6()())

	rf7 := hidefunc("func07 这是匿名函数") //1.7)
	fmt.Println(rf7)

	//方法调用
	var rm1 num = 9
	rm1 = rm1.addNum(2)
	fmt.Println("methon addNUm...", rm1)

}
