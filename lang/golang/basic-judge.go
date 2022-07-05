/*
	golang判断语句:
		if判断:
			if(<condition>){
				sentence01
			}else if(判断条件){
				sentence02
			}else if(判断条件){
				sentence03
			}else{
				sentenceEnd
			}
		switch判断:
			switch{
				case(<condition01>):
					sentence01
				case(<condition02>):
					sentence02
				case(<condition03>){
					sentence03
					fallthrough		//贯穿：关键词,无视后续判断条件,继续执行后续语句
				...
				default:
					setenceEnd
			}
		switch判断:
			switch <value>{
				case(<value01>):
					sentence01
				case(<value01>):
					sentence02
				case(<value01>){
					sentence03
					fallthrough		//贯穿：关键词,无视后续判断条件,继续执行后续语句
				...
				default:
					setenceEnd
			}



*/

package main
import(
	"fmt"
)

func main(){
	fmt.Println("sample 01 if----------------------------->")
	var index=2

	if(index==0){
		fmt.Println("index value is...",0)
	}else if(index==1){
		fmt.Println("index value is...",1)
	}else{
		fmt.Println("I do not know the value of index!")
	}


	fmt.Println("\n\nsample 02 switch----------------------------->")
	var char="a"
	switch{
		case(char=="a"):
			fmt.Println("index value is...","a")
		case(char=="b"):
			fmt.Println("index value is...","b")
			fallthrough		//贯穿：无视后续判断条件,继续执行后续语句
		case(char=="c"):
			fmt.Println("index value is...","c")
		default:
			fmt.Println("The \"switch\" default value... ")
	}


	fmt.Println("\n\nsample 03 switch----------------------------->")
	char = "c"
	switch char{
		case("a"):
			fmt.Println("index value is...","a")
		case("b"):
			fmt.Println("index value is...","b")
			fallthrough		//贯穿：无视后续判断条件,继续执行后续语句
		case("c"):
			fmt.Println("index value is...","c")
		default:
			fmt.Println("The \"switch\" default value... ")
	}

}