#include<stdio.h>

int main(int argn,char *argv[]){
    //获取第1-3行的输入
    int qNum,qChangePos,qValue[100];
    printf("question number=>");
    scanf("%d",&qNum);
    printf("question id=>");
    for(int counter=0;counter<qNum;counter++){
        int tmp;
        scanf("%d",&tmp);
        qValue[counter] = tmp;
    }
    printf("question aim postion=>");
    scanf("%d",&qChangePos);
    //交换位置
    int tmp = qValue[qChangePos-1];
    qValue[qChangePos-1] = qValue[qNum-1],qValue[qNum-1]=tmp;
    //打印输出
    for(int counter=0;counter<qNum;counter++){printf("%d ",qValue[counter]);}
    printf("\nprogram over!!!");
    return 0;
}