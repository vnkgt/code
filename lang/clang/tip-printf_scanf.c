// printf函数和scanf函数

#include <stdio.h>

void main(){
	//可以输入任意长度的字符串
	void *p[1];
	printf("input:\n");
	scanf("%s",p);
	printf("output:\n%s\n",p);
}