//文件四则运算
/*
    1.随机数算数式子生成并写入文件(demo_file_Calculation.txt)
    2.读取文件,计算结果,结果写入文件(demo_file_Calculation_result.txt)
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NUM_RAM_NUM 20

//1.生成算式文件
void getrandom()
{
    srand(time(NULL));
    char calc_sign[] = {'+','-','*','/'};
    FILE *write_file = fopen("demo_file_Calculation.txt","w");
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        fprintf(write_file,"%d %c %d =\n",1+rand()%100,calc_sign[rand()%4],1+rand()%100);
    }
    fclose(write_file);
}

//2.计算结果并写入
void getresult()
{
    FILE *write_file = fopen("demo_file_Calculaiton_result.txt","w");
    FILE *read_file = fopen("demo_file_Calculation.txt","r");
    int front[NUM_RAM_NUM],back[NUM_RAM_NUM];
    char sign[NUM_RAM_NUM];
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        fscanf(read_file,"%d %c %d =\n",&front[i],&sign[i],&back[i]);
    }
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        int temp;
        if(sign[i]=='+'){temp=front[i]+back[i];};
        if(sign[i]=='-'){temp=front[i]-back[i];};
        if(sign[i]=='*'){temp=front[i]*back[i];};
        if(sign[i]=='/'){temp=front[i]/back[i];};
        fprintf(write_file,"%d %c %d = %d\n",front[i],sign[i],back[i],temp);
    }
    printf("Finish!\n");
    system("pause");
}


void main()
{
    getrandom();
    getresult();
}