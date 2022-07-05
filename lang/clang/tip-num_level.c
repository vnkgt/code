//计算一个数的位数

#include <stdio.h>
void main(){
	//函数区
	int num_level(int num_value,int had_counted){
		int counter;
		counter = had_counted;
		if(num_value/10!=0){
			counter += 1;
			return num_level(num_value/10,counter);
		}
		else{
			return counter;
		}
	}
	//函数测试区
	printf("%d\n",num_level(1,1));
	printf("%d\n",num_level(10,1));
	printf("%d\n",num_level(100,1));
	printf("%d\n",num_level(1000,1));
	printf("%d\n",num_level(10000,1));
	printf("%d\n",num_level(100000,1));
	printf("%d\n",num_level(1000000,1));
}

