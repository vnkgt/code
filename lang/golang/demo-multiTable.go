/*
	九九乘法表
*/

package main
import(
	"fmt"
)

func main(){
	for i:=1;i<=9;i++{
		for j:=1;j<=i;j++ {
			fmt.Printf("%d*%d=%0.2d\t",i,j,i*j)
		}
		println()
		// i++
	}
}