//文本编辑器
/*
	1.打开文本文件(demo_Text_edit.txt)
	2.字符串输入
	3.文件关闭
 */

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define True 1
#define False 0

//文本编辑器
void Text_edit(){
	//1.创建文件指针,打开文本文件(demo_Text_edit.txt)
	FILE *txt = fopen("demo_Text_edit.txt","w");

	//2.获取用户输入并写入文本文件
	char buffer[1024]={0};		//临时存放输入的字符串
	printf("please input the content of text(input===>':quit'<====to quit):\n");
	while(True){
		memset(buffer,0,sizeof(buffer));		//初始化buffer中的内容
		fgets(buffer,sizeof(buffer),stdin);		//获取输入的字符串
		if(strncmp(buffer,":quit",5)==0){		//退出
			break;
		}
		for(int i=0;buffer[i]!='\0';i++){		//写入文件
			fputc(buffer[i],txt);
		}
	}

	//3.关闭文件
	fclose(txt);
	printf("\t\tWRITE OVER!!!\n");
}

//读取文本内容
void Text_read(){
	//1.创建文件指针,打开文本文件(demo_Text_edit.txt)
	FILE *txt = fopen("demo_Text_edit.txt","r");

	//2.读取文本内容
	char buffer;
	printf("\n\nThe content of demo_Text_edit.txt:\n");
	while((buffer = fgetc(txt))!=EOF){
		//3.打印文本读取的信息
		fputc(buffer,stdout);
	}

	//4.关闭文件
	fclose(txt);
	printf("\t\tREAD OVER!!!\n");
}

//主函数
void main(){
	Text_edit();	//编辑文本
	Text_read();	//查看文本内容
}