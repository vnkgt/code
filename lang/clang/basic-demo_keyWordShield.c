//关键字屏蔽
/*
	1.获取用户字符串
	2.对比获取屏蔽词
	3.屏蔽词替换
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void keyword_shield(){
	char user_string[1024];			//用户字符串
	char *ret=NULL;
	//1.获取用户输入字符串
	printf("please input string:\n\t");
	fgets(user_string,sizeof(user_string),stdin);
	//2.寻找并替换关键字fuck/sb
	while((ret = strstr(user_string,"sb"))!=NULL){
		strncpy(ret,"**",2);
	}
	while((ret = strstr(user_string,"fuck"))!=NULL){
		strncpy(ret,"****",4);
	}
	//打印结果
	printf("result:\n\t%s\n",user_string);
}


void main(){
	keyword_shield();
}