/*
system函数:
	1)包含头文件:#include <stdlib.h>
	2)格式:system("命令");
	3)作用:使用操作系统的命令行模式执行命令
	4)常用命令:
		system("pause");	//中断,等待系统输入
*/

#include <stdio.h>
#include <stdlib.h>

void main()
{
	printf("Hello Word!\n");
	system("pause");
}