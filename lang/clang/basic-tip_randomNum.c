//生成随机数
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//随机数生成器
//随机数范围[base_num,base_num+range_num)
int random(int min,int max){
	int base_num=min;
	int range_num=max-min;
	return (base_num+rand() % range_num); 
}

//主函数
void main(){
	//随机数种子
	srand((unsigned int) time(NULL));
	//测试随机数函数
	int random_num = random(10,20);
	printf("random_num:%d\n",random_num );
}