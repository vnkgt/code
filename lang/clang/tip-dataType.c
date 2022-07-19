/*
	c语言的数据类型:
		0.创建某数据类型的变量:
			修饰基础类型 基本类型 变量名;
			eg:
				long int a;
		1.基础类型:
			1.1.普通:
				int(整型)\float(单精度浮点)\double(双精度浮点类型)\char(字符)\
			1.2.构造:
				enum(枚举类型)\struct(结构体)\union(共用体)\
			1.3.特殊:
				void--->其指针可以指向任意数据类型
				数组--->一段连续的内存空间,数组默认返回第一个元素的引用
				指针--->一个特殊的数字,可以指向任意一个内存空间(该空间可以是低级指针),&用于取指针本身的值,*用来取指针所指内存空间的值
					指针数组:
						意义:本质是数组,数组中存放的是指针
						格式:数据类型* 数组名[数组大小]; 
					数组指针:
						意义:本质是指针,指针指向一个存放数据的数组
						格式:数据类型 (*指针名)[数组大小];						
				内存空间相当于房子(房子里可以是某个特定的数据,也可以是一个门牌号);指针相当于房子的门牌号
				void(无定义)\*(指针)\[](数组)
		2.修饰基本类型
			unsigned\long\short\long long

	eg:
		int a;
		short int a;
		long int a;
		unsigned int a;
		int *a;---->指针
		int **a;---->二级指针(指向一级指针的地址
		int ***a;---->三级指针(指向二级指针的地址)
		int *.....*a;---->N级指针(指向N-1级指针)
		int a[10];---->一维数组
		int a[9][10];---->二维数组
		int a[8][9][10];---->三维数组
		int *a[10];---->一级指针数组,用来储存一级int指针
		int **a[10];---->二级数组指针,用来储存二级或一级int指针(其实一级指针数组可以用来存储二级指针,但是在使用*取值是会报错)
		int (* a)[10];---->指针数组,相当于int *a,temp[10];a=temp;
			eg:
				char (* p)[20],temp[2][20]={"fsdfsd\n","dsf\n"};
				p=temp;
				p++;
				printf(p);


		float a;
		long float a;
		float *a;
		float a[10];

		double a;
		long double a;
		double *a;
		double a[10];

		char a;
		char *a;---->可以指向一个字符串
		char a[20];---->可以储存一个字符串(字符串以'\0'结尾，但打印时不显示'\0')
		char *a[20];---->指针数组,用来存放char指针

		void a;
		void *a;---->可以指向任意类型的数据(使用时需要强制转换)
			eg:
				void *a;					void *a;
				int b=10;					a = "aabbcc\n";
				a = (int *)b;				printf(a);
				printf("%d\n",a);

		struct 结构体名
		{
			结构体中的数据
		};
			eg:
				struct Node
				{
					int ID;
					char *name;
					struct Node *next,*front;---->在结构体内部使用自己的结构体
				};

		union 共用体名
		{
			共用体中的数据
		};
			eg:
				union Node
				{
					int ID;
					char *name;
					struct Node *next,*front;---->在结构体内部使用自己的结构体
				};
	
	  enum	枚举变量名
	  {
		枚举变量---->每个枚举变量对应一个数值
	  };
			eg:
				enum kk{a,b,aa,bb};
				enum kk temp;
				temp = b;
				printf("temp = %d\n",temp);---->结果temp = 1

*/
void main(int argc, char const *argv[])
{
	/* code */
}

void main(){
	
}

