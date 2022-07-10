C语言关键字:
	数据类型(12个):
		char ,short ,int ,long ,float ,double ,unsigned ,signed ,struct ,union ,enum ,void
	控制语句关键字(12个):
		if ,else ,switch ,case ,default ,for ,do ,while ,break ,continue ,goto ,return
	存储类关键字(5个):
		auto ,extern ,register ,static ,const
		sizeof ,typedef ,volatile

0宏说明:
	定义宏:
		define(都可用,无分号):
			#define 宏名 value
			eg:
				#define True 1
				#define False 0
		typedef(给数据类型起别名,有分号):
			typedef 原名 别名;
			eg:
				struct student{int id;char *name};
				typedef (struct student) stu;
				等价于:
					typedef struct student{int id;char *name} stu;
	常见c语言的宏:
		size_t	===>unsigned int
		NULL 	===>((void *)0)		//地址:0x000
		EOF		===>-1 				//文件尾
		FILE 	===>				//文件
			FILE* 	===>文件指针
			typedef struct
			{
				short           level;	//缓冲区"满"或者"空"的程度 
				unsigned        flags;	//文件状态标志 
				char            fd;		//文件描述符
				unsigned char   hold;	//如无缓冲区不读取字符
				short           bsize;	//缓冲区的大小
				unsigned char   *buffer;//数据缓冲区的位置 
				unsigned        ar;	 //指针,当前的指向 
				unsigned        istemp;	//临时文件,指示器
				short           token;	//用于有效性的检查 
			}FILE;
			C语言中有三个特殊的文件指针由系统默认打开,用户无需定义即可直接使用:
					stdin: 标准输入,默认为当前终端(键盘),我们使用的scanf、getchar函数默认从此终端获得数据.
					stdout:标准输出,默认为当前终端(屏幕),我们使用的printf、puts函数默认输出信息到此终端.
					stderr:标准出错,默认为当前终端(屏幕),我们使用的perror函数默认输出信息到此终端.
		stat 	===>				//文件状态(使用sys/types.h和sys/stat.h头文件)
			struct stat{
					dev_t         st_dev;       //文件的设备编号
					ino_t         st_ino;       //节点
					mode_t        st_mode;   	//文件的类型和存取的权限
					nlink_t       st_nlink;     //连到该文件的硬连接数目,刚建立的文件值为1
					uid_t         st_uid;       //用户ID
					gid_t         st_gid;       //组ID
					dev_t         st_rdev;      //(设备类型)若此文件为设备文件,则为其设备编号
					off_t         st_size;      //文件字节数(文件大小)
					unsigned long st_blksize;   //块大小(文件系统的I/O 缓冲区大小)
					unsigned long st_blocks;    //块数
					time_t        st_atime;     //最后一次访问时间
					time_t        st_mtime;    	//最后一次修改时间
					time_t        st_ctime;     //最后一次改变时间(指属性,Linux下有效)
				};


1数据(变量指针等):
	格式:数据类型修饰 数据类型 变量修饰 变量名(=初始值);
	1.数据类型:
		1.1.1整型:
			short/int/long/long long
			eg:
				unsigned short a=10;
				int a[]={1,2,3};
				long a;
		1.1.2字符型:
			char
			eg:
				char a='y';	//必须使用单引号
				char str[]={'a','b','g'};
				char str[]="HelloWord!";
		1.1.3浮点型:
			float/double
			eg:
				float a=1.123;
				double a;
		1.1.4结构体/共用体:
			结构体:
				struct
			联合体(共用体):
				union
			eg:
				struct Stu{
					int id;
					char *name;
				};
				union Data{
					int a;
					short b;
					char c;
				};
		1.1.5枚举类型:
			enum
			eg:
				enum{one,two,three};	//每个对象都有数字对应(one=0,two=1,three=2)
				enum week{Mon,Trues,Wen};
		1.1.6void类型:
			eg:
				void a;				//无类型,不可以直接赋值,必须经过强制转换赋值
				void *pointer;		//万能指针
		1.1.7其它:
			数据类型/变量修饰:
				有符号与无符号:signed(有符号,默认有该修饰)/unsigned(无符号)
				静态变量:static	
				数据存储(类型限定符):					//可以修饰指针和数组
					1)extern	声明一个变量,extern声明的变量没有建立存储空间
						eg:extern int a;				//a不能够赋值,直到下面代码出现int a;
					2)const	定义一个常量,常量的值不能修改
						eg:const int num=100;/int const num=100;
					3)volatile	防止编译器优化代码
						eg:volatile int a=0;
					4)register	定义寄存器变量,提高效率;register是建议型的指令,而不是命令型的指令,如果CPU有空闲寄存器,那么register就生效,如果没有空闲寄存器,那么register无效
		eg:register int a;
			变量修饰:
				数组:[]
					eg:int a[10];
				指针:*
					eg:char *p;	
			文件指针:
				FILE *
				FILE 	===>				//文件
					typedef struct
					{
						short           level;	//缓冲区"满"或者"空"的程度 
						unsigned        flags;	//文件状态标志 
						char            fd;		//文件描述符
						unsigned char   hold;	//如无缓冲区不读取字符
						short           bsize;	//缓冲区的大小
						unsigned char   *buffer;//数据缓冲区的位置 
						unsigned        ar;	 	//指针,当前的指向 
						unsigned        istemp;	//临时文件,指示器
						short           token;	//用于有效性的检查 
					}FILE;
				C语言中有三个特殊的文件指针由系统默认打开,用户无需定义即可直接使用:
					stdin: 标准输入,默认为当前终端(键盘),我们使用的scanf、getchar函数默认从此终端获得数据.
					stdout:标准输出,默认为当前终端(屏幕),我们使用的printf、puts函数默认输出信息到此终端.
					stderr:标准出错,默认为当前终端(屏幕),我们使用的perror函数默认输出信息到此终端.
		强制转换数据类型:
			隐式转换:遵循一定的规则,由编译系统自动完成
			强制转换:把表达式的运算结果强制转换成所需的数据类型
				格式方法:(数据类型 变量修饰) 表达式;	//变量修饰只可以写指针,变量修饰可有可无
				eg:
					a = (float) a;						//强制转换变量类型
					a = (void *) a;						//强制转换指针类型
	2.变量/常量:
		变量:
			变量声明:
				1)自动声明:变量定义在使用前
					eg:int a=10;
				2)显示声明:变量定义在使用后,关键字:extern
					eg:
						void main(){
							extern int a;
							printf("a=%d\n",a);
						}
						int a=10;
			局部变量(在"{}"内的变量):
				只能在作用域内起作用(一对"{}"内)
			全局变量(不在"{}"内的变量):
				可以在任意的两个源文件中任意引用;其它源文件可以通过extern进行说明引用
			静态变量(用static修饰的变量):
				不能在任意的两个源文件中任意引用;只能初始化一次;静态函数不能被其它源文件引用
		常量:
			常见的常量类型:
				1)数值常量(整数型常量/实数型常量):
					eg:整数型常量:1,22 ,3 ,4 ,8
					   实数型常量:2.13 ,5.7 ,7.0
				2)字符类型:
					eg:'a','b','y','0','-'
				3)字符串类型:
					eg:"Hello Word" ,"FUCK"
				4)符号常量(宏常量):
					eg:#define Week 7
				5)const修饰的变量:
					eg:const a=100;
	3.数组与指针:
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


2控制语句:
	2.1判断:
		if判断:
			if(条件){语句}
			else if(条件){语句}
			else if(条件){语句}
			...
			else{语句}
		switch判断:
			switch(表达式){
				case 取值1:执行语句; break;
				case 取值2:执行语句; break;
				……
				default:执行语句
			}
	2.2循环:
		for循环:
			for(最开始执行的表达式;条件判断;每循环后一次执行的表达式){语句}
		while循环:
			while(循环条件){语句}
		do_while循环:
			do{语句}while(循环条件)
	2.3跳转:
		无条件跳转:
			跳转点:语句;	//跳转点既可以在goto前,也可在goto后
			goto 跳转点;
		break:
			switch语句中:作用是终止某个case并跳出switch结构
			循环语句中:作用是跳出当前内循环语句,执行后面的代码(只能跳出一层循环)
		contiune:
			循环语句中:终止本次循环,并执行下一次循环(并不会终止整个循环,只是跳过本次循环)


3运算符:
	3.1算术运算符:
		+	正号
		-	负号
		+	加	
		-	减	
		*	乘	
		/	除	
		%	取模(取余)	
		++	前自增		格式:++变量
		++	后自增		格式:变量++
		--	前自减		格式:--变量
		--	后自减		格式:变量--
	3.2赋值运算符:
		=	赋值	
		+=	加等于	
		-=	减等于	
		*=	乘等于	
		/=	除等于	
		%=	模等于
	3.3比较运算符:
		==	相等于	
		!=	不等于	
		<	小于	
		>	大于	
		<=	小于等于	
		>=	大于等于	
	3.4逻辑运算符:
		!	非
		&&	与
		||	或
	3.5三目运算符:
		表达式1?表达式2:表达式3--->表达式1为真,计算表达式2;否则计算表达式3
	3.6运算符优先级:
			运算符	===>含义	===>使用格式
		1级:
			[]		=====>数组下标				==>数组名[常量表达式]
			()		=====>圆括号				==>(表达式)/函数名(形参表)	
			. 		====>成员选择(对象)			==>对象.成员名	
			->		=====>成员选择)指针)		==>对象地址->成员名
		2级:	
			-		=====>负号运算符	  		==>表达式
			~		=====>按位取反运算符		==>~表达式
			++		=====>自增运算符			==>++变量名/变量名++
			--		=====>自减运算符			==>--变量名/变量名--
			*		=====>取值运算符			==>*指针变量
			&		=====>取地址运算符			==>&变量名
			!		=====>逻辑非运算符			==>!表达式
			(类型)	=====>强制类型转换			==>(数据类型)表达式
			sizeof	=====>长度运算符			==>sizeof(表达式)
		3级:
			/		=====>除					==>表达式/表达式
			*		=====>乘					==>表达式*表达式
			%		=====>余数(取模)			==>整型表达式%整型表达式
		4级:
			+		=====>加					==>表达式+表达式
            -		=====>减					==>表达式-表达式
        5级:
        	<<		=====>左移					==>变量<<表达式
			>>		=====>右移					==>变量>>表达式
		6级:
			>		=====>大于					==>表达式>表达式
			>=		=====>大于等于				==>表达式>=表达式
			<		=====>小于					==>表达式<表达式
			<=		=====>小于等于				==>表达式<=表达式
		7级:
			==		=====>等于					==>表达式==表达式
			!=		=====>不等于				==>表达式!= 表达式
		8级:
			&		=====>按位与				==>表达式&表达式
		9级:
			^		=====>按位异或				==>表达式^表达式
		10级:
			|		=====>按位或				==>表达式|表达式
		11级:
			&&		=====>逻辑与				==>表达式&&表达式
		12级:
			||		=====>逻辑或				==>表达式||表达式
		13级:
			?:		=====>条件运算符			==>表达式1?表达式2:表达式3
		14级:
			=		=====>赋值运算符			==>变量=表达式
			/=		=====>除后赋值				==>变量/=表达式
			*=		=====>乘后赋值				==>变量*=表达式
			%=		=====>取模后赋值			==>变量%=表达式
			+=		=====>加后赋值				==>变量+=表达式
			-=		=====>减后赋值				==>变量-=表达式
			<<=		=====>左移后赋值			==>变量<<=表达式
			>>=		=====>右移后赋值			==>变量>>=表达式
			&=		=====>按位与后赋值			==>变量&=表达式
			^=		=====>按位异或后赋值		==>变量^=表达式
			|=		=====>按位或后赋值			==>变量|=表达式
		15级:
			,		=====>逗号运算符			==>表达式,表达式,…


4内存:
	4.1内存结构:
		cpu===>寄存器(register)===>内存(RAM)===>缓冲区(buffer)===>硬盘
	4.2内存空间:
		1)代码区
			存放所写代码的二进制内容
		2)全局区
			bbs:未初始化的全局变量,静态变量
			data:已经初始化的全局变量,静态变量,常量
		3)栈区
			存放区部变量,函数中的形参,函数的返回值,
		4)堆区
			c语言申请的内存空间在该处(malloc函数申请的空间)
	4.3类型限定符:									//可以修饰指针和数组
		1)extern:声明一个变量,extern声明的变量没有建立存储空间
			eg:extern int a;				//a不能够赋值,直到下面代码出现int a;
		2)const:定义一个常量,常量的值不能修改
			eg:const int num=100;/int const num=100;
		3)volatile:防止编译器优化代码
			eg:volatile int a=0;
		4)register:定义寄存器变量,提高效率;register是建议型的指令,而不是命令型的指令,如果CPU有空闲寄存器,那么register就生效,如果没有空闲寄存器,那么register无效
			eg:register int a;
		5)static:静态变量
			eg:static int a;


5常用函数:
	常见的头文件及作用:
		alloc.h	说明内存管理函数(分配、释放等)。
		assert.h	定义 assert调试宏。
		bios.h	说明调用IBM—PC ROM BIOS子程序的各个函数。
		conio.h	说明调用DOS控制台I/O子程序的各个函数。
		ctype.h	包含有关字符分类及转换的名类信息(如 isalpha和toascii等)。
		dir.h	包含有关目录和路径的结构、宏定义和函数。
		dos.h	定义和说明MSDOS和8086调用的一些常量和函数。
		error.h	定义错误代码的助记符。
		fcntl.h	定义在与open库子程序连接时的符号常量。
		float.h	包含有关浮点运算的一些参数和函数。
		graphics.h	说明有关图形功能的各个函数，图形错误代码的常量定义，正对不同驱动程序的各种颜色值，及函数用到的一些特殊结构。
		io.h	包含低级I/O子程序的结构和说明。
		limit.h	包含各环境参数、编译时间限制、数的范围等信息。
		math.h	说明数学运算函数，还定了 HUGE  VAL 宏， 说明了matherr和matherr子程序用到的特殊结构。
		mem.h	说明一些内存操作函数(其中大多数也在STRING.H中说明)。
		process.h	说明进程管理的各个函数，spawn…和EXEC …函数的结构说明。
		setjmp.h	定义longjmp和setjmp函数用到的jmp buf类型，说明这两个函数。
		share.h	定义文件共享函数的参数。
		signal.h	定义SIG[ZZ(Z]  [ZZ)]IGN和SIG[ZZ(Z]  [ZZ)]DFL常量，说明rajse和signal两个函数。
		stddef.h	定义读函数参数表的宏。(如vprintf,vscarf函数)。
		stddef.h	定义一些公共数据类型和宏。
		stdio.h	定义Kernighan和Ritchie在Unix System V 中定义的标准和扩展的类型和宏。还定义标准I/O 预定义流：stdin,stdout和stderr，说明 I/O流子程序。
		stdlib.h	 说明一些常用的子程序：转换子程序、搜索/ 排序子程序等。
		string.h	说明一些串操作和内存操作函数。
		sys\stat.h	定义在打开和创建文件时用到的一些符号常量。
		sys\types.h	说明ftime函数和timeb结构。
		sys\time.h	定义时间的类型time[ZZ(Z]  [ZZ)]t。
		time.h	定义时间转换子程序asctime、localtime和gmtime的结构，ctime、 difftime、 gmtime、 localtime和stime用到的类型，并提供这些函数的原型。
		value.h	定义一些重要常量，包括依赖于机器硬件的和为与Unix System V相兼容而说明的一些常量，包括浮点和双精度值的范围。
	5.1输入输出函数
		1)输出函数:
			printf("<format>",[<var>,...]);			//常用输出函数;
			puts(<list>/<point>);						//输出字符串,自带换行;
			fputs(<list>,stdout);						//输出字符串;stdout标准输出设备,默认是屏幕;
		2)输入函数:
			scanf("<format>",&<var>);				//数组直接写变量名,获取字符串时遇到空格或换行结束;
				注意:当两个scanf连用时,在两个scanf中间,"清除缓冲区数据"或使用"getchar();"获取换行字符'\n';
			gets(<list>);							//获取字符串;遇到换行结束;输入越界时报错;
			fgets(<list>,<stringLen>,stdin);		//获取字符串;越界时不报错;stdin标准输入设备,默认是键盘;
			getchar();								//从缓存区获取一个字符,字符会显(会显:敲会车显示);
			_getch();								//输入一个字符,字符不会显(会显:敲会车显示);位于conio.h头文件;
	5.2文件操作
		1)文件数据类型:
			FILE 	===>				//文件结构体
				typedef struct
				{
					short           level;	//缓冲区"满"或者"空"的程度 
					unsigned        flags;	//文件状态标志 
					char            fd;		//文件描述符
					unsigned char   hold;	//如无缓冲区不读取字符
					short           bsize;	//缓冲区的大小
					unsigned char   *buffer;//数据缓冲区的位置 
					unsigned        ar;	 //指针,当前的指向 
					unsigned        istemp;	//临时文件,指示器
					short           token;	//用于有效性的检查 
				}FILE;
			FILE* 	===>文件指针
			C语言中有三个特殊的文件指针由系统默认打开,用户无需定义即可直接使用:
				stdin: 标准输入,默认为当前终端(键盘),我们使用的scanf、getchar函数默认从此终端获得数据.
				stdout:标准输出,默认为当前终端(屏幕),我们使用的printf、puts函数默认输出信息到此终端.
				stderr:标准出错,默认为当前终端(屏幕),我们使用的perror函数默认输出信息到此终端.
		2)FILE * fopen(const char * filename, const char * mode);	//打开文件
			功能:打开文件
			参数:
				filename:需要打开的文件名,根据需要加上路径
				mode:打开文件的模式设置
				文件打开模式:
					r或rb	以只读方式打开一个文本文件(不创建文件,若文件不存在则报错)
					w或wb	以写方式打开文件(如果文件存在则清空文件,文件不存在则创建一个文件)
					a或ab	以追加方式打开文件,在末尾添加内容,若文件不存在则创建文件
					r+或rb+	以可读、可写的方式打开文件(不创建新文件)
					w+或wb+	以可读、可写的方式打开文件(如果文件存在则清空文件,文件不存在则创建一个文件)
					a+或ab+	以添加方式打开文件,打开文件并在末尾更改文件,若文件不存在则创建文件
			返回值:
				成功:文件指针
				失败:NULL
		3)int fclose(FILE * stream);								//文件关闭
			功能:关闭先前fopen()打开的文件.此动作让缓冲区的数据写入文件中,并释放系统所提供的文件资源.
			参数:
				stream:文件指针
			返回值:
				成功:0
				失败:-1
		4)int feof(FILE * stream);									//判断文件是否读取到了文件结尾
			功能:检测是否读取到了文件结尾.判断的是最后一次“读操作的内容”,不是当前位置内容(上一个内容).
			参数:
				stream:文件指针
			返回值:
				非0值:已经到文件结尾
				0:没有到文件结尾
		5)int fputc(int ch, FILE * stream);							//按字符写入文件
			功能:将ch转换为unsigned char后写入stream指定的文件中
			参数:
				ch:需要写入文件的字符
				stream:文件指针
			返回值:
				成功:成功写入文件的字符
				失败:返回-1
		6)int fgetc(FILE * stream);									//按字符读取文件
			功能:从stream指定的文件中读取一个字符
			参数:
				stream:文件指针
			返回值:
				成功:返回读取到的字符
				失败:-1
		7)int fputs(const char * str, FILE * stream);				//按字符串写入文件
			功能:将str所指定的字符串写入到stream指定的文件中,字符串结束符 '\0'  不写入文件. 
			参数:
				str:字符串
				stream:文件指针
			返回值:
				成功:0
				失败:-1
		8)char * fgets(char * str, int size, FILE * stream);		//按字符串读取文件
			功能:从stream指定的文件内读入字符,保存到str所指定的内存空间,直到出现换行字符、读到文件结尾或是已读了size - 1个字符为止,最后会自动加上字符 '\0' 作为字符串结束.
			参数:
				str:字符串
				size:指定最大读取字符串的长度(size - 1)
				stream:文件指针
			返回值:
				成功:成功读取的字符串
				读到文件尾或出错: NULL
		9)int fprintf(FILE * stream, const char * format, ...);		//按格式写入文件
			功能:根据参数format字符串来转换并格式化数据,然后将结果输出到stream指定的文件中,指定出现字符串结束符 '\0'  为止.
			参数:
				stream:已经打开的文件
				format:字符串格式,用法和printf()一样
			返回值:
				成功:实际写入文件的字符个数
				失败:-1
		10)int fscanf(FILE * stream, const char * format, ...);		//按格式读取文件
			功能:从stream指定的文件读取字符串,并根据参数format字符串来转换并格式化数据.
			参数:
				stream:已经打开的文件
				format:字符串格式,用法和scanf()一样
			返回值:
				成功:参数数目,成功转换的值的个数
				失败: - 1
		11)size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);		//按数据块写入文件
			功能:以数据块的方式给文件写入内容
			参数:
				ptr:准备写入文件数据的地址
				size: size_t 为 unsigned int类型,此参数指定写入文件内容的块数据大小
				nmemb:写入文件的块数,写入文件数据总大小为:size * nmemb
				stream:已经打开的文件指针
			返回值:
				成功:实际成功写入文件数据的块数目,此值和nmemb相等
				失败:0
		12)size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);			//按数据块读取文件
			功能:以数据块的方式从文件中读取内容
			参数:
				ptr:存放读取出来数据的内存空间
				size: size_t 为 unsigned int类型,此参数指定读取文件内容的块数据大小
				nmemb:读取文件的块数,读取文件数据总大小为:size * nmemb
				stream:已经打开的文件指针
			返回值:
				成功:实际成功读取到内容的块数,如果此值比nmemb小,但大于0,说明读到文件的结尾.
				失败:0
		13)int fseek(FILE *stream, long offset, int whence);		//移动文件光标位置
			功能:移动文件流(文件光标)的读写位置.
			参数:
				stream:已经打开的文件指针
				offset:根据whence来移动的位移数(偏移量),可以是正数,也可以负数,如果正数,则相对于whence往右移动,如果是负数,则相对于whence往左移动.如果向前移动的字节数超过了文件开头则出错返回,如果向后移动的字节数超过了文件末尾,再次写入时将增大文件尺寸.
				whence:其取值如下:
					SEEK_SET:从文件开头移动offset个字节
					SEEK_CUR:从当前位置移动offset个字节
					SEEK_END:从文件末尾移动offset个字节
			返回值:
				成功:0
				失败:-1
		14)long ftell(FILE *stream);								//获取文件光标位置
			功能:获取文件流(文件光标)的读写位置.
			参数:
				stream:已经打开的文件指针
			返回值:
				成功:当前文件流(文件光标)的读写位置
				失败:-1
		15)void rewind(FILE *stream);								//移动文件光标到开头
			功能:把文件流(文件光标)的读写位置移动到文件开头.
			参数:
				stream:已经打开的文件指针
			返回值:
				无返回值
		16)int stat(const char *path, struct stat *buf);			//获取文件状态(使用sys/types.h和sys/stat.h头文件)
			功能:获取文件状态信息
			参数:
			path:文件名
			buf:保存文件信息的结构体
			返回值:
			成功:0
			失败-1
				struct stat{
					dev_t         st_dev;		//文件的设备编号
					ino_t         st_ino;       //节点
					mode_t        st_mode;   	//文件的类型和存取的权限
					nlink_t       st_nlink;     //连到该文件的硬连接数目,刚建立的文件值为1
					uid_t         st_uid;       //用户ID
					gid_t         st_gid;      	//组ID
					dev_t         st_rdev;      //(设备类型)若此文件为设备文件,则为其设备编号
					off_t         st_size;      //文件字节数(文件大小)
					unsigned long st_blksize;   //块大小(文件系统的I/O 缓冲区大小)
					unsigned long st_blocks;    //块数
					time_t        st_atime;     //最后一次访问时间
					time_t        st_mtime;    	//最后一次修改时间
					time_t        st_ctime;     //最后一次改变时间(指属性,Linux下有效)
				};
		17)int remove(const char *pathname);						//删除文件
			功能:删除文件
			参数:
				pathname:文件名
			返回值:
				成功:0
				失败:-1
		18)int rename(const char *oldpath, const char *newpath);	//重命名文件
			功能:把oldpath的文件名改为newpath
			参数:
				oldpath:旧文件名
				newpath:新文件名
			返回值:
				成功:0
				失败: - 1
		19)int fflush(FILE *stream);								//清空缓冲区
			功能:更新缓冲区,让缓冲区的数据立马写到文件中.
			参数:
				stream:文件指针
			返回值:
				成功:0
				失败:-1
	5.3字符串操作
		绝大部分处理函数,遇到'\0'结束
		1)char *gets(char *s);										//获取输入的字符
			功能:从标准输入读入字符,并保存到s指定的内存空间,直到出现换行符或读到文件结尾为止.
			参数:
				s:字符串首地址
			返回值:
				成功:读入的字符串
				失败:NULL
		2)char *fgets(char *s,int size,FILE *stream);					//获取size个输入的字符
			功能:从stream指定的文件内读入字符,保存到s所指定的内存空间,直到出现换行字符、读到文件结尾或是已读了size - 1个字符为止,最后会自动加上字符 '\0' 作为字符串结束.
			参数:
				s:字符串
				size:指定最大读取字符串的长度(size - 1)
				stream:文件指针,如果读键盘输入的字符串,固定写为stdin
			返回值:
				成功:成功读取的字符串
				读到文件尾或出错: NULL
		3)int puts(const char *s);									//输出字符串
			功能:标准设备输出s字符串,在输出完成后自动输出一个'\n'.
			参数:
				s:字符串首地址
			返回值:
				成功:非负数
				失败:-1
		4)int fputs(const char * str,FILE * stream);				//字符串写入
			功能:将str所指定的字符串写入到stream指定的文件中,字符串结束符 '\0'  不写入文件. 
			参数:
				str:字符串
				stream:文件指针,如果把字符串输出到屏幕,固定写为stdout
			返回值:
				成功:0
				失败:-1
		5)size_t strlen(const char *s);								//字符串长度
			功能:计算指定指定字符串s的长度,不包含字符串结束符‘\0’
			参数:
				s:字符串首地址
			返回值:字符串s的长度,size_t为unsigned int类型
		6)char *strcpy(char *dest,const char *src);					//拷贝字符串
			功能:把src所指向的字符串复制到dest所指向的空间中,'\0'也会拷贝过去
			参数:
				dest:目的字符串首地址
				src:源字符首地址
			返回值:
				成功:返回dest字符串的首地址
				失败:NULL
		7)char *strncpy(char *dest,const char *src,size_t n);		//拷贝n个字符,size_t:unsigned int
			功能:把src指向字符串的前n个字符复制到dest所指向的空间中,是否拷贝结束符看指定的长度是否包含'\0'.
			参数:
				dest:目的字符串首地址
				src:源字符首地址
				n:指定需要拷贝字符串个数
			返回值:
				成功:返回dest字符串的首地址
				失败:NULL
		8)char *strcat(char *dest,const char *src);					//字符串拼接
			功能:将src字符串连接到dest的尾部,‘\0’也会追加过去
			参数:
				dest:目的字符串首地址
				src:源字符首地址
			返回值:
				成功:返回dest字符串的首地址
				失败:NULL
		9)char *strncat(char *dest,const char *src,size_t n);		//src字符的n个字符与dest拼接
			功能:将src字符串前n个字符连接到dest的尾部,‘\0’也会追加过去
			参数:
				dest:目的字符串首地址
				src:源字符首地址
				n:指定需要追加字符串个数
			返回值:
				成功:返回dest字符串的首地址
		10)int strcmp(const char *s1,const char *s2);				//字符串比较
			功能:比较 s1 和 s2 的大小,比较的是字符ASCII码大小.
			参数:
				s1:字符串1首地址
				s2:字符串2首地址
			返回值:
				相等:0
				大于:>0
				小于:<0
				失败:NULL
		11)int strncmp(const char *s1,const char *s2,size_t n);		//比较n个字符的大小
			功能:比较 s1 和 s2 前n个字符的大小,比较的是字符ASCII码大小.
			参数:
				s1:字符串1首地址
				s2:字符串2首地址
				n:指定比较字符串的数量
			返回值:
				相等:0
				大于:> 0
				小于:< 0
		12)int sprintf(char *str ,const char *format,...);			//格式化数据并保存
			功能:根据参数format字符串来转换并格式化数据,然后将结果输出到str指定的空间中,直到出现字符串结束符 '\0'  为止.
			参数:
				str:字符串首地址
				format:字符串格式,用法和printf()一样
			返回值:
				成功:实际格式化的字符个数
				失败:- 1
		13)int sscanf(const char *str,const char *format,...);		//按格式拆解字符串,并保存
			功能:从str指定的字符串读取数据,并根据参数format字符串来转换并格式化数据.
			参数:
				str:指定的字符串首地址
				format:字符串格式,用法和scanf()一样
			返回值:
				成功:参数数目,成功转换的值的个数
				失败:- 1
		14)char *strchr(const char *s,int c);							//查找字符c
			功能:在字符串s中查找字母c出现的位置
			参数:
				s:字符串首地址
				c:匹配字母(字符)
			返回值:
				成功:返回第一次出现的c地址
				失败:NULL
		15)char *strstr(const char *haystack,const char *needle);		//查找字符串needle
			功能:在字符串haystack中查找字符串needle出现的位置
			参数:
				haystack:源字符串首地址
				needle:匹配字符串首地址
			返回值:
				成功:返回第一次出现的needle地址
				失败:NULL
		16)char *strtok(char *str,const char *delim);					//字符串切割
			功能:来将字符串分割成一个个片段.当strtok()在参数s的字符串中发现参数delim中包含的分割字符时,则会将该字符改为\0 字符,当连续出现多个时只替换第一个为\0.
			参数:
				str:指向欲分割的字符串
				delim:为分割字符串中包含的所有字符(可以有多个字符)
			返回值:
				成功:分割后字符串首地址
				失败:NULL
		17)int atoi(const char *nptr);									//转换数字字符串为数字
			功能:atoi()会扫描nptr字符串,跳过前面的空格字符,直到遇到数字或正负号才开始做转换,而遇到非数字或字符串结束符('\0')才结束转换,并将结果返回返回值.
			参数:
				nptr:待转换的字符串
			返回值:成功转换后整数
		18)atof();														//把一个小数形式的字符串转化为一个浮点数.
		19)atol();														//将一个字符串转化为long类型
	5.4内存操作
		1)void *memset(void *s, int c, size_t n);						//初始化一段内存空间的值,一般用于初始化malloc分配的内存空间(eg:memset(arr,0,sizeof(arr)))
				功能:将s的内存区域的前n个字节以参数c填入
				参数:
					s:需要操作内存s的首地址
					c:填充的字符,c虽然参数为int,但必须是unsigned char , 范围为0~255
					n:指定需要设置的大小
				返回值:s的首地址
		2)void *memcpy(void *dest, const void *src, size_t n);		//内存拷贝
			功能:拷贝src所指的内存内容的前n个字节到dest所值的内存地址上.
			参数:
				dest:目的内存首地址
				src:源内存首地址,注意:dest和src所指的内存空间不可重叠
				n:需要拷贝的字节数
			返回值:dest的首地址
		3)int memcmp(const void *s1, const void *s2, size_t n);		//内存内容比较
			功能:比较s1和s2所指向内存区域的前n个字节
			参数:
				s1:内存首地址1
				s2:内存首地址2
				n:需比较的前n个字节
			返回值:
				相等:=0
				大于:>0
				小于:<0
		4)void *malloc(size_t size);									//为指针分配内存空间
			功能:在内存的动态存储区(堆区)中分配一块长度为size字节的连续区域,用来存放类型说明符指定的类型.分配的内存空间内容不确定,一般使用memset初始化.
			参数:
				size:需要分配内存大小(单位:字节)
			返回值:
				成功:分配空间的起始地址
				失败:NULL
		5)void *calloc(unsigned int num,unsigned int size);			//为指针分配内存空间并初始化
			功能:在内存的动态存储区中分配num个长度为size的连续空间
			参数:
				num:size空间的个数
				size:需要分配内存大小(单位:字节)
			返回值:
				成功:分配空间的起始地址
				失败:NULL
		6)extern void *realloc(void *mem_address, unsigned int newsize);//重新分配内存空间(并拷贝原空间的内容)
			功能:改变mem_address所指内存区域的大小为newsize长度.
			参数:
				mem_address:指针mem_address必须为指向堆内存空间的指针,即必须由malloc函数和calloc函数或者realloc函数分配空间的指针.
				newsize:新空间大小
			返回值:
				成功:分配空间的起始地址
				失败:NULL
		7)void free(void *ptr);										//释放分配的内存空间
			功能:释放之前调用calloc/malloc/realloc所分配的内存空间
			参数:
				ptr:指针指向一个要释放内存的内存块		
			返回值:
				函数不返回任何值	
		8)int fflush(FILE *stream);								//清空缓冲区
			功能:更新缓冲区,让缓冲区的数据立马写到文件中.
			参数:
				stream:文件指针
			返回值:
				成功:0
				失败:-1
		9)size_t _msize(void * memblock);					//查看内存分配内存空间的大小
	5.5常见的库函数(用法形式,非函数原型)
		#include <stdio.h>:
			system("Terminal命令");													//使用操作系统的终端执行Terminal命令
			exit();																	//退出程序,终止程序的执行
			fflush(FILE *stream);													//清空缓冲区
			perror(提示字符串);														//在"提示字符串"后输出上一个函数的异常信息
		#include <stdlib.h>
			rand()%(num);															//生成[0,num)的随机数
		#include <time.h>:
			time(NULL);																//获取时间戳(当前时间距离1970/0:0:0的秒数);
			srand(unsigned int) time(NULL);											//随机数种子,一般搭配rand函数使用,只用写一次,保证同一个文件每次生成的随机数不会相同;
		#include <malloc.h>
			(DataType *)malloc(SpaceSize)											//分配内存空间		
			(DataType *)realloc(pointer,NewSpaceSize)								//重新分配内存空间,返回新空间的第一个地址
			_msize(pointer)															//查看指针指向分配内存空间的大小
	5.6其它函数
		随机数:
			rand() % range_num + base_num; 			//生成一个随机数,范围是[base_num,base_num+range_num);
			rand() % base_num; 						//生成一个随机数,范围是[0,base_num);
				一般写法:	srand((unsigned int) time(NULL));	//随机数种子,仅需要设置一次,需要使用time.h头文件
							base_num + rand() % range_num;		//生成一个随机数,需要stdlib.h头文件
 6其它
 	分文件编写代码:
 		MyHeadFile.h 	===>自定义头文件;不写main函数,只写自定义算法文件中的函数声明;
 		MyFunction.c 	===>自定义算法文件;不写main函数,用双引号导入自定义的头文件,编写函数功能;
 		other.c         ===>其它源文件;用双引号导入自定义的头文件,使用自定义头文件中的函数;
 		注意:
 			多文件使用gcc编译时,先让所有的.c文件生成.o文件,再将.o文件链接生成可执行文件.



函数详解:
	
