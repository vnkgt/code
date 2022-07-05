/*
说明:
	*===>指针变量的修饰; 
	point===>指针变量名; 
	addr===>地址; 
	value===>数据值;
	var===>变量,可变值;
	index===>数组下标;
	list_name===>数组变量名;
1)数组与指针的关系:
	数组名可以视为指向首元素,的指针(一般情况下)
	数组可以视为一个特殊的指针
	list_name[index]===>*(list_name+index)===>index[list_name]
	list_name:数组名(数组指针)
	index:数组下标
	eg:
		int a[]={2,3,4};	//a[1]=*(a+1)=1[a]
2)const修饰指针:
	const修饰*		====>修饰指针的value
	const修饰pointer====>修饰指针的addr
	const修饰*,addr可读可写,value只读;
		eg:	const int *p;/int const *p;
	const修饰pointer,addr只读,value可读可写;
		eg:int * const p;
	const修饰*和pointer,addr只读,value只读;
		eg:int const * const p;
3)二级指针:
	指针  ===>  创建    ===>	value
	二级指针===>int **p;  ===>	一级指针的地址
	一级指针===>int *p;   ===>	普通变量的地址
4)指针数组:
	本质:数组,用来存放指针的数组
	eg:
		int num1=11,num2=22,num3=33;
		int *arr[]={&num1,&num2,&num3};
		printf("*arr[1]=%d\n",*arr[1]);
5)数组指针:
	本质:指针,指向一个数组,指针(创建的指针)指向指针(数组名)
	数组本质:指针
	eg:
		int num1=11,num2=22,num3=33;
		int arr[]={num1,num2,num3},*arrp;
		arrp = arr;
		printf("*(arrp+0)=arr[0]:%d\n",arrp[0]);
*/

#include<stdio.h>
void main()
{
	int num1 = 11, num2 = 22, num3 = 33;
	int arr[] = {num1,num2,num3};		//数组
	int *parr[] = {&num1,&num2,&num3};	//指针数组:数组,由指针组成的数组
	int *arrpointer = arr;				//数组指针:指针,指向数组的指针
	printf("数组arr[0]=%d\n",arr[0]);		//直接使用数组
	printf("指针数组**(parr+1)=%d,*parr[1]=%d\n",**(parr+1),*parr[1]);	//指针数组
	printf("数组指针*(arrpointer+2)=%d,arrpointer[2]=%d\n",*(arrpointer+2),arrpointer[2]);	//数组指针
}