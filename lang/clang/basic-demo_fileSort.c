//文件排序
/*
    1.随机数生成
    2.随机数按一定格式写入文件(demo_file_sort.txt)
    3.文件随机数读取
    4.排序
    5.排序结果写入新的文件(demo_file_sort_result.txt)
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NUM_RAM_NUM 20      //随机数个数

//1.数据生成与写入
void getrandom()
{
    FILE *write_txt = fopen("demo_file_sort.txt","w");
    srand(time(NULL));    //随机数时间戳
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        fprintf(write_txt,"%d\n",(rand() % 100));
    }
    fclose(write_txt);
}

//2.读取排序并写入新的文本文件
void getresult()
{
    FILE *read_file = fopen("demo_file_sort.txt","r");
    // rewind(read_file);
    FILE *write_file = fopen("demo_file_sort_result.txt","w");
    int num_list[NUM_RAM_NUM];  //存放读取数据的数组
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        fscanf(read_file,"%d\n",&num_list[i]);
    }
    //排序
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        for(int j=i;j<NUM_RAM_NUM;j++)
        {
            if(num_list[i]>num_list[j])
            {
                int temp;
                temp = num_list[i];
                num_list[i]=num_list[j];
                num_list[j]=temp;
            }
        }
    }
    for(int i=0;i<NUM_RAM_NUM;i++)
    {
        fprintf(write_file,"%d <",num_list[i]);
        if(i==5){printf("\n");};
    }
    printf("Finish!\n");
    fclose(write_file);
    fclose(read_file);
    system("pause");
}

void main()
{
    getrandom();
    getresult();
}