//冒泡排序

#include <stdio.h>

void main(){
	int a[]={7,5,6,3,4,2,1};
	int list_len = sizeof(a)/sizeof(int);
	//原数组
	printf("source_list:\n");
	for(int i=0;i<list_len;i++){
		printf("%d\t",a[i]);
	}
	printf("\n");


	//重新排序
	for(int i=0;i<list_len;i++){
		for(int j=0;j<list_len-1;j++){
			if(a[j]>a[j+1]){
				int temp;
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp; 
			}
		}
	}


	//打印对比
	printf("result_list:\n");
	for(int i=0;i<list_len;i++){
		printf("%d\t",a[i]);
	}
}