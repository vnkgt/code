/*
变量声明:
	1)自动声明:变量定义在使用前
		eg:
			void main()
			{
				int a=10;
				printf("a=%d\n",a);
			}
	2)显示声明:变量定义在使用后
		关键字:extern
		eg:
			void main()
			{
				extern int a;
				printf("a=%d\n",a);
			}
			int a=10;
 */

#include <stdio.h>
void main()
{
	extern int a;
	printf("a=%d\n",a);
}
int a=10;