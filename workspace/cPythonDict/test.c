#include<stdio.h>
void main(int argc,char *argv[]){
	int index=0;
	while(index<argc){
		printf("argv%0.2d:%s\n",index,argv[index]);
		index++;
	};
}
