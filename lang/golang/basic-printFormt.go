/*
	golang有严格的“格式要求”:
		func main(){
			sentence
		}
	golang打印信息:
		//打印不换行
			print()			//内置函数
			fmt.Print()
		//打印并且换行
			println()		//内置函数
			fmt.Println()
		//打印
			fmt.Printf()


	golang格式化输出:
		//必须使用fmt.Printf()函数
		//placeHolder:占位符
		//placeHolder_value:占位符的值
		fmt.Printf("<placeHolder>",<placeHolder_value>)
			placeHolder:
				%v=>通用占位符
				%f=>浮点型占位符
				%d=>整型占位符
				%T=>数据类型
*/

package main

import (
	"fmt"
)

func main() {
	println("normal print-------------------------------------------")

	fmt.Println("line00--->")
	fmt.Print("line01--->hello word!")
	fmt.Printf("line02--->")

	println("\n\nplaceHolder print----------------------------------------")
	fmt.Printf("%-20v--->%7v\n", "transport-way", "price")
	fmt.Printf("%-20v--->%0.7d\n", "airport", 1300)
	fmt.Printf("%-20v--->%0.7d\n", "car", 1000)
	fmt.Printf("%-20v--->%0.7d\n", "subway", 800)

}
