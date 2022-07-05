//字符串操作函数测试
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//char *gets(char *s);获取输入的字符
void func01(){
	char str[100]={0};
	printf("gets:\n"),gets(str);
	printf("%s\n", str);
}

//char *fgets(char *s,int size,FILE *stream);获取输入的字符
void func02(){
	char str[100]={0};
	printf("fgets:\n"),fgets(str,10,stdin);
	printf("%s\n",str);
}

//int puts(const char *s);输出字符串
void func03(){
	char str[]="aksdjlfaks";
	char *p = "lsjdlfjsd";
	printf("str[]:\n"),puts(str);
	printf("*p:\n"),puts(p);
}

//int fputs(const char * str,FILE * stream);字符串写入
void func04(){
	char str[]="fuck funck\n";
	char *p = "klfsjld\n";
	printf("str[]:\n"),fputs(str,stdout);
	printf("*p:\n"),fputs(p,stdout);
}

//unsigned int strlen(const char *s);字符串长度
void func05(){
	char str[]="flaksjdlfajl";
	char *p  = "Hello Word";
	printf("strlen(str):%d\n",strlen(str));
	printf("strlen(p):%d\n",strlen(p));
}

//char *strcpy(char *dest,const char *src);拷贝字符串
void func06(){
	char str[]="Hello Word";
	char str1[20];
	strcpy(str1,str);
	printf("src_str:%s\n",str);
	printf("dest_str1:%s\n",str1);
}

//char *strncpy(char *dest,const char *src,size_t n);拷贝n个字符,size_t:unsigned int
void func07(){
	char str[]="Hello Word";
	char str1[20];
	strncpy(str1,str,4);
	printf("src_str:%s\n",str);
	printf("dest_str1:%s\n",str1);
	printf("strncpy_size:%d\n",4);
}

//char *strcat(char *dest,const char *src);字符串拼接
void func08(){
	char str1[]="Hello\0";
	char str2[]="Word\0";
	strcat(str1,str2);
	printf("str1:%s\n",str1);
	printf("str2:%s\n",str2);
}

//char *strncat(char *dest,const char *src,size_t n);src字符的n个字符与dest拼接
void func09(){
	char str1[]="Hello";
	char str2[]="Word";
	strncat(str1,str2,2);
	printf("str1:%s\n",str1);
	printf("str2:%s\n",str2);
}

//int strcmp(const char *s1,const char *s2);字符串比较
void func10(){
	char str1[]="Hello";
	char str2[]="Hallo";
	int result;
	result =  strcmp(str1,str2);
	if(result==0){
		printf("str1 equal str2\n");
	}
	else{
		printf("str1 unequal str2\n");
	}
}

//int strncmp(const char *s1,const char *s2,size_t n);比较n个字符的大小
void func11(){
	char str1[]="Hello";
	char str2[]="Hallo";
	int result;
	result =  strncmp(str1,str2,1);
	if(result==0){
		printf("str1 equal str2 in %d\n",1);
	}
	else{
		printf("str1 unequal str2\n");
	}
}

//int sprintf(char *str ,const char *format,...);格式化数据并保存
void func12(){
	char result[100];
	sprintf(result,"%s---%d","Hello",7);
	printf("result:%s\n",result);
}

//int sscanf(const char *str,const char *format,...);按格式拆解字符串,并保存
void func13(){
	char src[] = "email:1234567@vmkgt.com";
	char mail_addr[10];
	int mail_num;
	sscanf(src,"email:%d@%s",&mail_num,mail_addr);
	printf("result:\n");
	printf("mail_num:%d\n",mail_num);
	printf("mail_addr:%s\n",mail_addr);
}

//char *strchr(const char *s,int c);查找字符c
void func14(){
	char src[]="HelloWord";
	char *index=strchr(src,'f');
	if(index!=NULL){
		printf("Success\n");
	}
	else{
		printf("False\n");
	}
}

//char *strstr(const char *haystack,const char *needle);查找字符串needle
void func15(){
	char src[]="HelloWord";
	char *index=strstr(src,"ll");
	if(index!=NULL){
		printf("Success\n");
	}
	else{
		printf("False\n");
	}
}

//char *strtok(char *str,const char *delim);字符串切割
void func16(){
	char src[]="Hello:Word&haha|123";
	char *result = strtok(src,":&|");	//第一次分割
	printf("result:%s\n",result);		
	result=strtok(NULL,":&|");			//第二次分割
	printf("result:%s\n",result);
	result=strtok(NULL,":&|");			//第三次分割
	printf("result:%s\n",result);
	result=strtok(NULL,":&|");			//第四次分割
	printf("result:%s\n",result);
}

//int atoi(const char *nptr);转换字符串为数字
void func17(){
	char src[]="444Hello Word";
	int result = atoi(src);
	printf("result:%d\n",result);
}



void main(){
	// func01();
	// func02();
	// func03();
	// func04();
	// func05();
	// func06();
	// func07();
	// func08();
	// func09();
	// func10();
	// func11();
	// func12();
	// func13();
	// func14();
	// func15();
	// func16();
	func17();
}