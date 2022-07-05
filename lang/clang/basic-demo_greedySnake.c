//贪吃蛇精简版
/*
    1.游戏菜单
    2.开始游戏
        初始化墙
        初始化蛇
        初始化食物
        显示食物
        蛇移动/蛇获取方向
            方向误操作判断
        食物随机更新/蛇长度增加
        死亡判断
            蛇碰墙
            蛇咬尾
        分数/时间显示
    3.退出游戏
*/

//头文件/宏定义
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <windows.h>
#define True 1
#define False 0
#define WIDTH 45		//墙宽
#define HEIGHT 25		//墙高
#define Walltype '#'    //画墙的字符
#define Snakehead '@'   //蛇头的字符
#define Snakebody '#'   //蛇身的函数
#define Foodtype 'o'    //食物字符

//结构体(初始化物体)/物体初始化属性
struct position{int x;int y;};                          //位置坐标

struct snake{
    struct position body[(WIDTH-2)*(HEIGHT-2)];         //蛇身位置坐标列表
    struct position tail;                               //蛇尾位置
    int size;                                           //蛇身结数
    int life;                                           //蛇生命
    char snake_last_option;                             //蛇的最后一次操作记录
    int offset_x;                                       //移动时的偏移量
    int offset_y;
    int start_time;                                     //开始时间
    int over_time;                                      //结束时间
    int score;                                          //分数
};

struct position Food;                                    //食物
struct snake Snake;                                     //蛇


//函数声明区
void Allcontrol();              //全局控制
void gotoxy(int x,int y);       //光标移动
void delcur();                  //不显示光标
void colcur(int num);           //切换光标的颜色
void ShowWall();                //显示墙
void updata();                  //更新显示
void InitGame();                //初始化游戏
void SnakeMove();               //蛇移动
void RandomFood();              //随机食物
void DieJudge();                //死亡检测
void Scoring();                 //的分统计
//函数实现区
//0.光标移动函数
void gotoxy(int x,int y){
	if(x==0 && y==0){return;}
	COORD coord;
	coord.X = x;
	coord.Y = y;
	//设置控制台光标位置
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),coord);
}

//0.去掉控制台光标
void delcur(){
 	CONSOLE_CURSOR_INFO cci;
 	cci.bVisible = False;
 	cci.dwSize = sizeof(cci);
 	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE),&cci);
}

//0.切换光标颜色
void colcur(int num)//num:颜色色号
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),num);
}

//0.总控制函数
void Allcontrol(){
    delcur();//关闭光标
    while(True){
        colcur(14);//切换颜色
		system("cls");
		char user_option;
		printf("************************************\n");
		printf("******press 's' to start game*******\n");
		printf("******press 'q' to  quit game*******\n");
		printf("************************************\n");
		user_option =  getchar();
		if(user_option == 's'){ //开始游戏
            system("cls");      //清屏
            InitGame();         //初始化游戏
            while(Snake.life){
                updata();       //游戏更新显示
            }
        }
		else if(user_option == 'q'){break;}    
		else{system("cls");continue;}            //输入错误
		fflush(stdin);                           //清空缓冲区                            
	}
    printf("Welcome play next time!!!\n");
    system("pause");
    colcur(15);
}

//1.显示墙
void ShowWall(){
    //显示墙
    gotoxy(0,0);//移动光标
    colcur(9); //切换颜色
    for(int i=0;i<HEIGHT-1;i++){
        for(int j=0;j<WIDTH-1;j++){
            if(i==0 || j==0 || i==HEIGHT-2 || j==WIDTH-2){printf("%c",Walltype);}
            else{printf(" ");}
        }
        printf("\n");//结束换行
    }
    //游戏说明
    colcur(30);//切换颜色
    gotoxy(WIDTH,HEIGHT/5-2);
    printf("\t\tGreedy Snake");
    gotoxy(WIDTH,HEIGHT/5-1);
    printf("\t\tup:w");
    gotoxy(WIDTH,HEIGHT/5);
    printf("\t\tdown:s");
    gotoxy(WIDTH,HEIGHT/5+1);
    printf("\t\tleft:a");
    gotoxy(WIDTH,HEIGHT/5+2);
    printf("\t\tright:d");
    colcur(15);//切换颜色
}

//1.游戏更新显示的函数
void updata(){
    //蛇尾补空格
    gotoxy(Snake.tail.x,Snake.tail.y); //移动光标到蛇尾处
    printf(" ");//补充空格
    colcur(10);//切换颜色
    //蛇移动
    SnakeMove();
    //显示蛇
    for(int i=0;i<Snake.size;i++){
        gotoxy(Snake.body[i].x,Snake.body[i].y);
        if(i==0){printf("%c",Snakehead);}
        else{printf("%c",Snakebody);}
    }
    colcur(13);//切换颜色
    //显示食物
    gotoxy(Food.x,Food.y);
    printf("%c",Foodtype);
    //蛇吃食物蛇的身长加1,食物重新定位
    if(Snake.body[0].x==Food.x && Snake.body[0].y==Food.y){
        RandomFood();
        Snake.size+=1;      //蛇身
        Snake.score +=1;    //分数
    }
    //显示分数
    Scoring();
    //结束更新显示时置光标到游戏框下部
    gotoxy(0,HEIGHT);
    colcur(14);//切换颜色
    //死亡判断
    DieJudge();
    //睡眠
    Sleep(100);     //睡眠100ms
}

//2.初始化游戏物体的属性
void InitGame(){            
    //蛇
    Snake.size = 3;
    Snake.body[0].x = WIDTH/2;      //头
    Snake.body[0].y=HEIGHT/2;
    Snake.body[1].x = 1+WIDTH/2;    //第二节蛇身
    Snake.body[1].y=HEIGHT/2;
    Snake.body[2].x = 2+WIDTH/2;    //第三节蛇身
    Snake.body[2].y=HEIGHT/2;
    Snake.snake_last_option = 'a';  //最后移动时的方向记录
    Snake.offset_x = -1;            //移动时的偏移量(向右移动)
    Snake.offset_y = 0;
    Snake.tail.x = Snake.body[Snake.size-1].x;      //蛇尾位置
    Snake.tail.y = Snake.body[Snake.size-1].y;
    Snake.life = True;                              //蛇的生命
    Snake.score = 0;                                //分数
    Snake.start_time = time(NULL);                  //游戏开始时间
    //食物
    RandomFood();
    //显示墙
    ShowWall();
}

//2.蛇移动
void SnakeMove(){
    char key;   //获取用户输入的蛇的方向
    if(_kbhit()){key = _getch();//_kbhit()如果没有键盘输入返回0,有输入返回真
        //判断方向操作是否违法
        if(Snake.snake_last_option=='a' && key=='d'){key = Snake.snake_last_option;}
        if(Snake.snake_last_option=='d' && key=='a'){key = Snake.snake_last_option;}
        if(Snake.snake_last_option=='w' && key=='s'){key = Snake.snake_last_option;}
        if(Snake.snake_last_option=='s' && key=='w'){key = Snake.snake_last_option;}
    }
    //合法操作修改移动偏移量
    switch(key){
        case 'a'://右
            Snake.offset_x =-1;Snake.offset_y=0;Snake.snake_last_option = key;break;
        case 'd'://左
            Snake.offset_x =1;Snake.offset_y=0;Snake.snake_last_option = key;break;
        case 'w'://上
            Snake.offset_x =0;Snake.offset_y=-1;Snake.snake_last_option = key;break;
        case 's'://下
            Snake.offset_x =0;Snake.offset_y=1;Snake.snake_last_option = key;break;
    }
    // //保存最后一次的操作
    // Snake.snake_last_option = key;
    //蛇身从后向前移动
    for(int i=Snake.size;i>0;i--){
        Snake.body[i].x = Snake.body[i-1].x;
        Snake.body[i].y = Snake.body[i-1].y;
    }
    //蛇头移动
    Snake.body[0].x += Snake.offset_x;
    Snake.body[0].y += Snake.offset_y;
    //更新蛇尾位置
    Snake.tail.x = Snake.body[Snake.size-1].x;
    Snake.tail.y = Snake.body[Snake.size-1].y;
}

//2.随机食物
void RandomFood(){
    srand(time(NULL));              //时间戳种子(确保每次运行的随机数不同)
    Food.x = 1+rand()%(WIDTH-3);    //食物位置
    Food.y = 1+rand()%(HEIGHT-3);
}

//2.死亡判断()
void DieJudge(){
    //死亡判断检测
	//判断是否撞墙
	if(Snake.body[0].x==WIDTH-2 || Snake.body[0].x==0 || Snake.body[0].y==0 || Snake.body[0].y==HEIGHT-2){
		Snake.life = False;
	}
	//判断是否蛇咬尾
	for(int i=1;i<Snake.size;i++){
		if(Snake.body[0].x==Snake.body[i].x && Snake.body[0].y==Snake.body[i].y){
			Snake.life = False;
		}
	}
	//死亡效果
	if(!Snake.life){
		//死亡时显示蛇头
		gotoxy(Snake.body[0].x,Snake.body[0].y);
		printf("%c",Snakehead);
		_getch();
		system("cls");	//清屏
		//打印死亡信息
		printf("Game Over!!!\n");
		printf("Score:%d\n",Snake.score);
		printf("Time:%ds\n",Snake.over_time-Snake.start_time);
        system("pause");
		system("cls");
	}
}

//2.分数计算
//游戏时
void Scoring(){
    gotoxy(WIDTH,(HEIGHT/5)*3+0);
    printf("\t\tScore:%d",Snake.score);
    gotoxy(WIDTH,(HEIGHT/5)*3+1);
    Snake.over_time = time(NULL);   //获取当前时间
    printf("\t\tTime:%ds",Snake.over_time-Snake.start_time);
}

//主函数
void main(){
    Allcontrol();
}