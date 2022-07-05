//动态字符串

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//动态字符串
void *varstring(){
	char *var=(char *)malloc(1);	//为动态字符串分配空间
	int var_len=0;			//动态字符串的长度
	char temp_get_char;//临时获取的字符
	printf("please input string:\n\t");
	while((temp_get_char=getchar())!='\n'){
		var[var_len++] = temp_get_char;
		var =(char *)realloc(var,var_len+1);	//再次为动态字符串分配空间
	}
	var[var_len]='\0';
	return var;
}

void main(){
	char *temp=varstring();
	printf("result:\n\t%s\n",temp);
}