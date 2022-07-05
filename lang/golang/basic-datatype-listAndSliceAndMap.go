/*
=>golang中的列表list,切片slice,表map:
	length长度 <= capacity容量,长度和容量不是同一个含义
	几点注意:
		1)传递“列表类的参数”给函数时,一般不使用“列表list”,而使用“切片slice”;
			slice可以传递任意长度的数据,list传递参数的长度是固定的“且list效率低下”
		2)map:储存数据是以“键值对”的形式
		3)理解三者之间的差异:
			golang中“list”	=>	python中“固定长度list”	=>	clang中“列表list”
			golang中“slice”	=>	pyhton中“任意长度list”	=>	clang中“链表linkTable”结构数据体
			golang中“map”	=>	pyhton中“字典dict”		=>	clang中“节点有别名的链表linkTable”结构数据体
	1.内置函数:
		len(<obj>)		//查看对象长度,查看字符串长度时会有bug
			//只适合统计ascii码
				len(<string>)
			//可统计unicode码
				import(
					"unicode/utf8"
				)
				utf8.RuneCountInString(<string>)
		cap(<obj>)		//查看对象容量

	2.列表list:
		创建列表:
			//listName:列表名
			//listLen:列表长度
			//datatype:列表的数据类型
			var <listName> [<listLen>]<datatype>
			//创建并初始化
			var <listName> = [<listLen>]<datatype>{<arg>,}
			//列表长度不定,创建时自动计算列表的长度
			var <listName> = [...]<datatype>{<arg>,}
		增加列表元素:
			//固定长度列表中的元素只能修改,不能添加增加列表的长度
		修改列表元素:
			<listName>[<index>] = <newArg>
		删除列表元素:
			//无删除操作,只能将元素覆盖
		调用列表元素:
			//index:列表中元素的索引
			<listName>[<index>]
		切片操作:
			//startIndex:开始元素索引,可以不写
			//endIndex:结束元素索引,可以不写
			//切片后newListName中包含原来列表中的"[startIndex,endIndex)"元素,“是一个左闭右开的区间”
			<newListName> := <listName>[<startIndex>:<endIndex>]




===>切片slice:
		创建切片:
			//创建切片
			var <sliceName> []<datatype>
			//创建并初始化
			var <sliceName> = []<datatype>{<arg>,}
		添加切片元素:
			//sliceName:切片对象
			//listObj/sliceObj:列表对象
			<sliceName> = append(<listObj/sliceObj>,<arg>,)
		删除切片元素:
			//无删除操作,只能将元素覆盖
		修改切片元素:
			<sliceName>[<index>] = <newValue>
		调用切片元素:
			<sliceName>[<index>]
		切片操作:
			//三索引切片
			//sliceObj/listObj:切片对象,或者列表对象
			//startIndex:开始元素索引,可以不写
			//endIndex:结束元素索引,可以不写
			//capacityLimit:当切片自动重新分配容量时,容量的限制
			//切片后newListName中包含原来列表中的"[startIndex,endIndex)"元素,“是一个左闭右开的区间”
			var <sliceName> = <sliceObj/listObj>[<startIndex>:<endIndex>:<capacityLimit>]


===>映射map:
		创建map映射:
			//映射map储存数据的形式,键值对:"key:value"
			//mapName:映射
			//keyDatatype:键key的数据类型,与python不同,可以是float/int型
			//valueDatatype:值value的数据类型
			var <mapName> map[<keyDatatype>]<valueDatatype>
		添加映射元素键值对:
			//newKey:添加新的键名
			//newValue:新键对应的值
			<mapName>[<newKey>] = <newValue>
		删除映射元素:
			delet(<mapName>,<key>)
		修改映射元素

===>for-range循环遍历list,slice,map
	说明:
		range变量map时不会按照特定的先后顺序遍历,是无序的
	//traverObj:可遍历对象,包括“列表list,切片slice”
	//用trv遍历traverObj
	for <trv> := range <traverObj>{
		sentence
	}

===>make函数,创建list,slice,map
	//创建list,并分配listLen长度的空间
	var <listName> = make([]<datatype>,<listLen>)
	//创建slice,并预分配sliceCap长度的空间
	var <sliceName> = make([]<datatype>,<sliceCap>)
	//创建map,并预分配mapCap长度的空间
	var <mapName> = make(map[<keyDatatype>]<valueDatatype>,<mapCap>)
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

//for-range遍历map映射
var rangePrintMap = func(mapSrc map[string]string) {
	//使用for-range遍历,map映射的“键”=>“值”
	fmt.Printf("\tmapSrc%5v=>%5v\n	and len of map:%0.3d\n",
		"key", "value", len(mapSrc))
	for key := range mapSrc {
		fmt.Printf("\tmapSrc%5v=>%5v\n", key, mapSrc[key])
	}
}

//list/slice闭包与解包
var unpackList = func(arg ...string) {
	fmt.Println("\t解包=>", arg)
	for i := range arg {
		fmt.Println("\t\t", arg[i])
	}
}

var slice2func = func(arg []string) {
	fmt.Println("\tslice2func...", arg)
}

func main() {
	//声明
	//"周一": "Mon", "周二": "Tue", "周三": "Wed", "周四": "Thu", "周五": "Fri", "周六": "Sat", "周日": "Sun"
	var listSrc = [8]string{"周一", "周二", "周三", "周四", "周五", "周六", "周日"} //创建list对象
	var sliceSrc = make([]string, 0)                                  //创建切片slice对象,并预分配0的空间
	var mapSrc = make(map[string]string, 1)                           //创建map映射,并预分配1的空间

	//初始化,append函数,为切片slice对象添加元素
	sliceSrc = append(sliceSrc, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") //给切片sliceSrc赋值
	min := len(listSrc)                                                          //找到listSrc与sliceSrc中较短的一个
	if len(listSrc) > len(sliceSrc) {
		min = len(sliceSrc)
	}
	for index := 0; index < min; index++ { //给map映射赋值
		mapSrc[sliceSrc[index]] = listSrc[index]
	}

	fmt.Println("\n\nabout map........................................")
	//使用for-range遍历,map映射的“键”=>“值”
	fmt.Println("初始化map")
	rangePrintMap(mapSrc) //打印mapSrc
	//删除map元素
	fmt.Println("删除map中的周一至周五")
	delete(mapSrc, "Mon")
	delete(mapSrc, "Tue")
	delete(mapSrc, "Wed")
	delete(mapSrc, "Thu")
	delete(mapSrc, "Fri")
	rangePrintMap(mapSrc) //打印mapSrc
	//覆盖list/slice元素
	fmt.Println("\n\nabout list.......................................")
	fmt.Println("初始化的list:", listSrc)
	listSrc[0] = "0"
	listSrc[1] = "1"
	listSrc[2] = "2"
	fmt.Println("覆盖修改周一至周三后的list:", listSrc)
	//切片操作
	listSrcSlice := listSrc[3:6] //对listSrc切片
	fmt.Println("对listSrc进行切片操作获取listSrcSlice:", listSrcSlice)
	//解包
	fmt.Println("闭包与解包")
	unpackList(listSrcSlice...)
	//切片传给函数
	fmt.Println("切片对象传递参数")
	slice2func(sliceSrc)

}
