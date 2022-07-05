//数组逆序

#include <stdio.h>

void main(){
	int a[]={7,6,5,4,3,2,1};
	int list_len = sizeof(a)/sizeof(int);	//数组长度
	int front_index=0;						//前元素下标
	int back_index=list_len-1;				//后元素下标

	//原数组
	printf("source_list:\n");
	for(int i=0;i<list_len;i++){
		printf("%d\t",a[i]);
	}
	printf("\n");

	while(1){
		//交换
		int temp;
		temp = a[front_index];
		a[front_index] = a[back_index];
		a[back_index] = temp;
		//下标移动
		front_index++;
		back_index--;
		//判断下标是否相遇
		if(front_index>=back_index){
			break;
		}
	}

	//新数组
	printf("source_list:\n");
	for(int i=0;i<list_len;i++){
		printf("%d\t",a[i]);
	}
	printf("\n");
}