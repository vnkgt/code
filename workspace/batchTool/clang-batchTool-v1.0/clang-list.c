/*
=>clang双链表
    功能:
        1.初始化list    listInit
        2.打印list      listPrint
        3.获取list长度  listLen
        4.增    listAppend
        5.删    listDel
        6.改    listChange
        7.查    listFind
        8.插入  listInsert
        8.拷贝  listCopy
        9.排序  listSort
*/
#include<stdio.h>
#include<malloc.h>
//列表长度
int listLen(char *list[]){
    int listlen=0;
    for(;*(list+listlen)!=NULL;listlen++){}
    return listlen;
}
//列表打印
void listPrint(char *list[]){
    if(listLen(list)==0){printf(">>>list:node:value\tnil\n");}
    for(int index=0;*(list+index);index++){printf(">>>list:node:value\t%p\t%p\t%s\n",list,*(list+index),*(list+index));}
}
//检查列表溢出
int checkOutRange(char *list[],int index){
    if(index>=listLen(list)){printf(">>>out of range\t%p\n",list);return 1;}//列表溢出
    return 0;
}

//1.增
char **listAppend(char *list[],char *string){
    int listlen = listLen(list);
    *(list+listlen) = string;
    *(list+listlen+1) = NULL;   //防止溢出
    return list;
}
//2.删
char **listDel(char *list[],int index){
    if(checkOutRange(list,index)){return list;}//列表溢出
    for(;*(list+index);index++){*(list+index)=*(list+index+1);}
    *(list+index) = NULL;   //防止溢出
    return list;
}
//3.改
char **listChange(char *list[],int index,char *string){
    if(checkOutRange(list,index)){return list;}//列表溢出
    *(list+index) = string;
    return list;
}
//4.查
char *findList(char *list[],int index){
    if(checkOutRange(list,index)){return NULL;}//列表溢出
    return *(list+index);
}