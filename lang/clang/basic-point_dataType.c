//数据类型
#include <stdio.h>


//1)整型
void test_int(){
	int a=100;
	printf("test_int:%d\n",a);
}

//2)字符型
void test_char(){
	char a='Q';
	printf("test_char:%c\n",a);
}

//3)浮点型
void test_float(){
	double PI=3.1415926;	//float最多输出6位小数
	printf("test_float:%0.7f\n",PI);
}

//4)数组
void test_list(){
	char str[]="Hello Word!";
	printf("test_list:%s\n",str);
}

//5)指针
void test_pointer(){
	char *str = "Hello C!";
	printf("test_pointer:%s\n",str);
}



//主函数
void main(){
	test_int();
	test_char();
	test_float();
	test_list();
	test_pointer();
}












