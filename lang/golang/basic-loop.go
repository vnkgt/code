/*
	中英文对照:
		sentence:执行语句
		condition:条件
	golang循环语句:
		条件循环:
			//initCondition:初始化条件
			//judgeCondition:循环条件
			//endSentence:每次循环结束时执行
			for initCondition; judgeCondtion; endSentence{
				sentence
			}
			特别注意错误写法(不能写小括号):
				for(initCondition; judgeCondtion; endSentence){
					sentence
				}
		条件循环:
			//judgeCondtion:判断条件,可以为空(不写)
			for(<judgeCondtion>){
				sentence
			}
		条件循环:
			for{
				//中断条件
				if(<condtion>){
					break
				}
				sentence
			}
		死循环:
			for{
				sentence
			}
*/
package main

import (
	"fmt"
)

func main() {
	var index = 0
	for index < 10 {
		fmt.Println("index...", index)
		index++
	}
}
