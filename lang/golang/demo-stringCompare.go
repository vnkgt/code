/*
	golang判断字符串中是否含有某个特殊字符串
*/

package main
import(
	"fmt"
	"strings"	//使用到的库
)

func main(){
	srcString := "Hello word!!!"
	compareString := "!"

	judge := strings.Contains(srcString,compareString)
	fmt.Printf("\"%v\" in \"%v\"?...",compareString,srcString,judge)
}