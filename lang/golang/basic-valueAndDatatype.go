/*
	golang的常量与变量:
		//无论是常量还是变量使用前必选先声明
		常量:
			const <argName>=<value>
				eg:
					const index=100
		变量:
			//声明变量是要么表明"数据类型<datatype>",要么"赋值<value>"
				var <argName> <datatype>
				var <argName>=<value>
				var <argName> <datatype>=<value>
					eg:
						var index int64
						var index=100
						var index int64 = 100
			//短声明,在"{}"内起作用
				<argName> := <value>
					eg:
						index := 2
		参数传递"占位符"=>"_":
			//多用来接受“函数多个返回值”中的“无用返回值”
			eg:
				index := new(big.Int)
				newindex,_ := index.SetString("321321321321321321321321321321321321321321321",10)



	golang的数据类型:
		基本类型：boolean，numeric，string类型的命名实例是预先声明的。
		复合类型：array，struct，指针，function，interface，slice，map，channel类型(可以使用type构造)
			int32:有符号整型(有正负号)
			uint32:无符号整型(无正负号)
			float64:有符号浮点型,数值类型不声明多为float64(有正负号)
			string:字符串
		1.几点说明:
			1)int类型中哪些支持负数
			    有符号（负号）：int8 int16 int32 int64
			    无符号（负号）：uint8 uint16 uint32 uint64
			2)浮点类型的值有float32和float64(没有 float 类型)
			3)byte和rune特殊类型是别名
			    byte就是unit8的别名
			    rune就是int32的别名
			4)int和uint取决于操作系统（32位机器上就是32字节，64位机器上就是64字节）
			    uint是32字节或者64字节
			    int和uint是一样的大小
			5)为了避免可移植性问题，除了byte（它是uint8的别名）和rune（它是int32的别名）之外，
				所有数字类型都是不同的。 在表达式或赋值中混合使用不同的数字类型时，需要转换。
				例如，int32和int不是相同的类型，即使它们可能在特定架构上具有相同的大小。
			6)数字类型的数字特别大时,可以导入"math/big"
				import( "math/big")
				方法一:
					<argName> = big.NewInt(<value>)
				方法二:
					<argName> = new(big.Int)
					//函数返回两个值
					//numString:大数的字符串,用双引号
					//baseSystem:进制,常用二，八，十，十六进制
					<argName>.SetString(<numString>,<baseSystem>)

		2.数据类型间的强制转换:
			// []byte -> other type
				[]byte => string : string([]byte)
				[]byte => int : binary包处理, 查看下面
			// int -> other type
				int => string : s = strconv.Itoa(i)
				int => int32  : i32 = int32(num)
				int => int64 : i64 = int64(num)
				int64/int32 => int : i = int(num)
				int64 => string : strconv.FormatInt(int64, 10)
				int64 => time.Duration : time.Duration(int64)
				int32 => byte : bytes.NewBuffer() 看上面 int 和 byte 互转
				int => float64 : float64(num)
			// other type -> int
				i = int(int32/int64)
				float64/float32 => int(int64/int32)
			// string -> other type
				string => int :  i, err = strconv.Atoi(s)
				string => bool : strconv.ParseBool("true")
				string => float32 : strconv.ParseFloat(s, 32)
				string => float64 : strconv.ParseFloat(s, 64)
				string => uint : strconv.ParseUint()
				string => int32/int64 : strconv.ParseInt(s, 10, 32/64)
				string => []byte : []byte(string)
				string(16进制) => int32/int64 : strconv.ParseInt(s, 0, 32/64)
			// other type -> string
				int,int32,int64 => string : str1 := fmt.Sprintf("%d", i)             // i可以是int/int32/int64
				                        或  str2 := strconv.Itoa(i)                  // i为int
				                        或  str3 := strconv.FormatInt(int64(i), 10)  // i可以是int/int32/int64
				uint64 => string : strconv.FormatUint(unit64, 10)
				bool => string : strconv.FormatBool(true)
				float64 => string : strconv.FormatFloat(float64(12), 'f', -1, 64)
				                        或  fmt.Sprintf("%.2f", float64)
			// array -> slice :
				1) copy(array[:], slice[0:4])  | 全部 copy(array[:], slice)
				2) for
				for index, b := range someSlice {
				    array[index] = b
				}
			// slice -> array
				slice=>array :    array[:]
*/

package main

import (
	"fmt"
	"math/big"
)

func main() {
	println("big int handle...大数处理方法")
	//短声明
	index := new(big.Int)
	// 10:10进制
	// _:变量占位符
	newindex, _ := index.SetString("987654321987654321987654321987654321987654321", 10)
	fmt.Println(newindex)
}
