#include <stdio.h>
#include "myfunc.h"		//导入自定义头文件

int main(int argc,char *argv[]){
	int temp;
	temp =myAdd(12,13);
	printf("myfunc.h_success_import:%d\n",temp);
	return 0;
}