/*
	统计字符串长度:
		//只适合统计ascii码
			len(<string>)
		//可统计unicode码
			import(
				"unicode/utf8"
			)
			utf8.RuneCountInString(<string>)

*/
package main
import(
	"fmt"
	"unicode/utf8"
)

func main(){
	var str = "你好 english!"
	size := utf8.RuneCountInString(str)
	fmt.Println("size...",size)
}