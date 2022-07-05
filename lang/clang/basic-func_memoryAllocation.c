//内存分配函数

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//void *memset(void *s, int c, size_t n);始化一段内存空间的值,一般用于初始化malloc分配的内存空间(eg:memset(arr,0,sizeof(arr)))
void func01(){
	char *p=malloc(10);
	memset(p,'H',10);
	p[9]='\0';
	printf("output:\n\t%s\n",p);
}

//void *memcpy(void *dest, const void *src, size_t n);内存拷贝
void func02(){
	char arr1[]="Hello Word!!!";
	char arr2[sizeof(arr1)];
	memcpy(arr2,arr1,sizeof(arr1));
	printf("output:\n\t%s\n",arr2);
}

//int memcmp(const void *s1, const void *s2, size_t n);内存内容比较
void func03(){
	char a1[]="Hello";
	char a2[]="Heloo";
	int result=0;
	result = memcmp(a1,a2,sizeof(a1)/sizeof(char));
	printf("memcmp_result:%d\n",result);
}

//void *malloc(size_t size);为指针分配内存空间
void func04(){
	char *p=malloc(3);//为p分配3个字节
	printf("input:\n\t"),scanf("%s",p);
	printf("output:\n\t%s\n",p);
	free(p);
}

//extern void *realloc(void *mem_address, unsigned int newsize);//重新分配内存空间(并拷贝原空间的内容)

void main(){
	// func01();
	// func02();
	// func03();
	func04();
}