//c双链表实现pyton列表list
/*
listNode结构体:
	int index;	//索引序号
	char *content;	//内容,全部以字符串存储,content内存大小根据所给字符串大小而定
list的函数方法:
	list();		//创建空列表;
*/


#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<string.h>

#define True 1
#define Flase 0
#define None -1

struct listNode{
	int index;	//索引
	void *content;	//内容
	struct listNode *before,*after;	//前一个节点,后一个节点
};

//函数声明
struct listNode *list(void *argv[]);

void main(int argc,char *argv[])	//argc:命令行参数个数		argv:命令行参的值
{
	void *targv[] = {"aaa","bbb","ccc"};
	list(targv);
	printf("over");
}

struct listNode *list(void *argv[])//创建数组 argv:数组的内容
{
	printf("start\n");
	int argvLen = sizeof(argv)/sizeof(void *);//列表长度
	struct listNode *head,*before_node_pointer;
	before_node_pointer = NULL;//指向前一个节点,锚
	for(int index = 0; index<argvLen; index++)//argv中的值赋给链表	index:列表索引下标
	{
		struct listNode *node;
		// node->content = malloc(_msize(argv[index]));//给节点内容分配内存,_msize查看指针指向内存的大小
		if(before_node_pointer==NULL){head=node;}//前一个节点为空时,创建的节点为头节点
		if(before_node_pointer!=NULL){before_node_pointer->after=node;}//前一个节点连接后一个节点
		node->before=before_node_pointer;//后一个节点连接前一个节点
		memcpy(argv[index],node->content,_msize(argv[index]));//内容赋值
		node->index = index;//索引复制
		before_node_pointer = node;//锚后移
		printf(argv[index]);
		printf("\n");
	}
	(head+argvLen)->after = NULL;//尾节点的下一个节点
	return head;
}