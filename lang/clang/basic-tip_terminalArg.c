/*
获取命令行(终端)参数:
	格式:
		数据类型 main(int argc,char *argv[])
		{
			//main函数
		}
	说明:
		argc--->获取的(终端)参数个数
		argv--->获取的(终端)参数字符串列表
*/

#include <stdio.h>

//生成main.exe可执行文件后输入
//main aa bb cc dd ee ff
void main(int argc,char *argv[])
{
	printf("The number of Terminal_arg:%d\n\n",argc);
	printf("The value of Terminal_arg:\n");
	int i;
	for(i=0;i<argc;i++)
	{
		printf("\t%s\n", argv[i]);
	}
}