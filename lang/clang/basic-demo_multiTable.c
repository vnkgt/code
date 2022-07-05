//9x9乘法表

#include <stdio.h>

void main(){
	//外循环
	for(int i=1;i<=9;i++){
		//内循环
		for(int j=1;j<=i;j++){
			printf("%dx%d=%d\t",i,j,i*j);
		}
		//内循环结束换行
		printf("\n");
	}
}