//开发进度:球吃球bug

/*
宏定义:
    True    1   真
    False   0   假
    None    -1  不存在
    ScreenWidth     命令行宽度
    ScreenHeight    命令行长度
球球大作战:
    1.创建位置结构体        struct XY
            x值                默认为0
            y值                默认为0
        创建球结构体            struct Ball
            球中心位置          struct XY center
            球半径              int radius
            球状态              int alive(True:存在;False:不存在)
            球速度              struct XY speed
            球阴影像素坐标列表   struct XY *shadow
        创建墙结构体
            墙砖列表            int WallBlockList[]
    2.开始游戏
        0)光标移动                  void gotoxy(struct XY *position)
            光标颜色                void colcur(int num)
            光标隐藏                void delcur()
            打印直接打印struct XY   void showXY(struct XY *position,char block)
            打印球中的struct XY     void showBall(struct Ball *ball,char block)
            打印墙列表              void showWall(struct XY *wallList,char block)
        1)墙壁初始化                struct XY *initWall(int flag)
            直接打印墙壁砖块
        2)球球碰撞判断              int judgeCrashB2B(struct Ball *ballA,struct Ball *ballB)
            球墙碰撞判断            int judgeCrashB2W(struct Ball *ball)
        3)球阴影生成函数            struct Ball *getBallshadow(struct Ball *ball);
        4)初始化球                  struct Ball *ballInit(int x,int y,int radi)
            4.1)初始化player球      struct Ball *myBallInit(int x,int y,int radi)
                调用ballInit()
            4.2)初始化一个enemy球   struct Ball *enemyBallInit(int x,int y,int radi)
                调用ballInit()
            4.3)获取多个enemy球     struct Ball *getManyEnemyBall(int number,int minradi,int maxradi)
                调用enemyBallInit()
        5)移动球                    struct Ball *moveBall(struct Ball *ball,struct XY direction)
            5.1)player移动          struct Ball *myBallMove(struct Ball *ball)
                调用moveBall()
            5.2)一个enemy移动       struct Ball *enemyBallMove(struct Ball *ball)
                调用moveBall()
            5.3)多个enemy移动       struct Ball **manyEnemyBallMove(struct Ball **balllist)
                调用enemyBallMove
        10)死亡判断                 int judgeDie(struct Ball *ball)
        11)球吃球                   int bEatb(struct Ball *ballA,struct Ball *BallB)
        12)死亡效果                 void dieShow(struct Ball *ball)
*/

//头文件
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <malloc.h>
#include <windows.h>
#include <time.h>

//宏定义
#define True 1
#define False 0
#define None -1
#define ScreenWidth 100
#define ScreenHight 45
#define MyBallBlock '#'      //打印player球使用的字符
#define EnemyBallBlock '='   //打印enemy球使用的字符
#define WallBlock '{'        //墙砖字符
#define BackgroundBlock ' '       //填充字符,背景字符
#define RadiusRate 3         //画圆时的y:x的值,y比x长RadiusRate>1
#define BallSpeed  2         //球运动的速度(x,y速度)

//操作按键
#define Left 'a'            //左
#define Right 'd'           //右
#define Up 'w'              //上
#define Down 's'            //下
#define Apart ' '           //分裂

//结构体
struct XY{          //坐标
    int x;
    int y;
};
struct Ball{       //球
    struct XY center;//中心
    int radius;//半径
    int alive;//是否存活
    int speed;//球移动速度
    struct XY *shadow;//阴影列表
    struct XY direction;//最后操作方向
};

//函数声明
void gotoxy(struct XY *position);//0.1光标移动
void delcur();//0.2删除光标
void colcur(int num);//0.3调整光标颜色
void showXY(struct XY *position,char block);//0.4打印一个XY
void showShadow(struct Ball *ball,char block);//0.5打印整个球的区域(包括阴影)
void showMyBall(struct Ball *ball);//0.6打印player球
void showEnemyBall(struct Ball **enemyList);//0.7打印struct Ball **enemyList
void showWall(struct XY *position);//0.8打印墙壁
void showEmpty(struct Ball *ball);//0.9打印空格,球移动前的阴影位置
struct XY *initWall(int flag);//1.打印墙列表WallList
int judgeCrashB2B(struct Ball *ballA,struct Ball *ballB);//2.判断ballA和ballB是否碰撞
int judgeCrashB2W(struct Ball *ball,struct XY *wallList);//2.判断ball与wallList是否有重合的砖块(碰撞)
struct Ball *getBallshadow(struct Ball *ball);//3.获取指定center,radius圆的阴影
struct Ball *myBallInit(struct XY *center,int radi);//4.1.初始化player球
struct Ball *enemyBallInit(struct XY *center,int radi);//4.2.初始化一个enemy球
struct Ball **getManyEnemyBall(int number,int minradi,int maxradi);//4.3.获取number个最大半径为maxradi的圆
struct Ball *moveBall(struct Ball *ball,struct XY *direction);//5.球移动
struct Ball *myBallMove(struct Ball *ball);//5.1player球移动
void enemyBallMove(struct Ball **enemy);//5.2enemy球列表移动
void bEatb(struct Ball *player,struct Ball **enemyList);//6.球吃球

struct XY *wallList;//墙列表
//函数
//主函数
void main(int argc,char *argv)
{
    srand((unsigned)time(NULL));              //0.时间戳种子(确保每次运行的随机数不同),仅需要设置一次
    struct XY origin,lastpoint;
    origin.x = origin.y = 0;//原点
    lastpoint.x = 0,lastpoint.y = ScreenHight+1;//墙的下一行起点
    struct Ball player;struct XY center;      //4.初始化player球
    wallList = initWall(0);                         //1.获取初始化的墙砖列表
    center.x = center.y = 13;                
    player = *myBallInit(&center,2);          //4.player初始化
    struct Ball **enemy;
    system("cls");
    enemy = getManyEnemyBall(5,1,4);
    delcur();
    colcur(9);
    showWall(wallList);
    while(True)
    {
        colcur(3);
        showEnemyBall(enemy);
        enemyBallMove(enemy);
        colcur(4);
        showMyBall(&player);
        myBallMove(&player);
        bEatb(&player,enemy);
        Sleep(200);
    }
    
    
    // while(True)
}       

//0通用函数
//0.1光标移动函数
void gotoxy(struct XY *position)
{
    COORD coord;
	coord.X = position->x;
	coord.Y = position->y;
	//设置控制台光标位置
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),coord);
}

//0.2去掉控制台光标
void delcur(){
 	CONSOLE_CURSOR_INFO cci;
 	cci.bVisible = False;
 	cci.dwSize = sizeof(cci);
 	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE),&cci);
}

//0.3切换光标颜色
void colcur(int num)//num:颜色色号
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),num);
}

//0.4直接打印struct XY
void showXY(struct XY *position,char block)
{
    gotoxy(position);printf("%c",block);
    for(int i=0;i<_msize(wallList)/sizeof(struct XY);i++)//如果位置与墙重合,则重新打印墙
    {
        if((wallList+i)->x==position->x && (wallList+i)->y==position->y)
        {
            gotoxy(position),printf("%c",WallBlock);
        }
    }
}

//0.5打印struct Ball中的struct XY *shadow
void showShadow(struct Ball *ball,char block)
{
    if(ball->alive==True)//球存活则打印
    {
        struct XY *templist=ball->shadow,oldposition;
        int flag=False;//flag=True:在以前的阴影中   flag=False:不在以前的阴影中
        for(int i=0;i<_msize(templist)/sizeof(struct XY);i++)//如果老位置不是阴影,将老位置用背景字符代替
        {
            oldposition.x = (templist+i)->x-(ball->direction.x)*(ball->speed);
            oldposition.y = (templist+i)->y-(ball->direction.y)*(ball->speed);
            for(int j=0;j<_msize(templist)/sizeof(struct XY);j++)
            {
                if(oldposition.x==(templist+j)->x && oldposition.y==(templist+j)->y){flag=True;break;}
            }
            if(flag==False)
            {
                showXY(&oldposition,BackgroundBlock);
            }
            flag=False;//将标志复位
        }
        for(int i=0;i<_msize(templist)/sizeof(struct XY);i++)//打印新位置,_msize查看指针分配内存的大小
        {
            showXY(templist+i,block);
        }
    }
}

//0.6打印player球
void showMyBall(struct Ball *ball)
{
    showShadow(ball,MyBallBlock);
}

//0.6打印struct Ball **enemy
void showEnemyBall(struct Ball **enemyList)
{
    for(int i=0;i<_msize(enemyList)/sizeof(struct Ball *);i++)
    {
        showShadow(enemyList[i],EnemyBallBlock);
    }
}

//0.7打印墙列表中的元素
void showWall(struct XY *wallList)
{
    for(int i=0;i<_msize(wallList)/sizeof(struct XY);i++)
    {
        showXY(wallList+i,WallBlock);
    }
}

//0.8打印空格,球移动前的阴影
void showEmpty(struct Ball *ball)
{
    struct XY *blank;
    blank = ball->shadow;
    for(int i=0;i<_msize(blank)/sizeof(struct XY);i++)
    {
        gotoxy(blank+i);
        printf(" ");
    }
}

//1.初始化墙
struct XY *initWall(int flag)
{
    int index=0;
    struct XY *wallList;//wallList:墙砖列表
    wallList = (struct XY *)malloc(sizeof(struct XY)*index);//给墙列表分配内存空间
    if(flag==0)//长方形墙壁(ScreenWidth*ScreenHeight)
    {
        for(int y=0;y<ScreenHight;y++)//生成墙列表中的元素
        {
            for(int x=0;x<ScreenWidth;x++)
            {
                if(y==ScreenHight-1 || y==0 || x==ScreenWidth-1 || x==0)
                {
                    wallList = (struct XY *)realloc(wallList,sizeof(struct XY)*(index+1));//给墙列表重新分配内存空间
                    wallList[index].x = x,wallList[index].y = y,index++;//wallList列表元素赋值
                }
            }
        }
    }
    return wallList;
}

//2.1.球碰球判断
int judgeCrashB2B(struct Ball *ballA,struct Ball *ballB)
{
    //两球存活,并且符合相撞公式
    if(ballA->alive==True && ballB->alive==True)
    {
        for(int i=0;i<_msize(ballA->shadow)/sizeof(struct XY);i++)
        {
            for(int j=0;j<_msize(ballB->shadow)/sizeof(struct XY);j++)
            {
                if(ballA->shadow[i].x==ballB->shadow[j].x && ballA->shadow[i].y==ballB->shadow[j].y)
                {
                    return True;
                }
            }
        }
    }
    return False;
}

//2.2.球碰墙判断
int judgeCrashB2W(struct Ball *ball,struct XY *wallList)
{
    if(ball->alive==True)//球存活
    {
        int v1,v2;
        for(int b_index=0;b_index<_msize(ball->shadow)/sizeof(struct XY);b_index++)//球阴影列表
        {
            for(int w_index=0;w_index<_msize(wallList)/sizeof(struct XY);w_index++)
            {
                v1 = ball->shadow[b_index].x-wallList[w_index].x;
                v2 = ball->shadow[b_index].y-wallList[w_index].y;
                if(v1==0 && v2==0){return True;}
            }
        }
    }
    return False;
}

//3.球阴影生成函数
struct Ball *getBallshadow(struct Ball *ball)//生成球的阴影
{
    struct Ball *returnBall;
    struct XY *shadowlist,cent = ball->center;//圆中心
    int radi=ball->radius;//圆半径
    // printf("running %d======%d=======%d\n",radi,cent.x,cent.y);
    int space = 0;//shadowlist空间的大小
    shadowlist = (struct XY *)malloc(sizeof(struct XY)*space);//给指针分配空间
    for(int x=cent.x-radi-1;x<=cent.x+radi;x++)//生成shadow内存空间
    {
        for(int y=cent.y-radi-1;y<=cent.y+radi;y++)
        {
            if(((x-cent.x)*(x-cent.x)+(y-cent.y)*(y-cent.y)*RadiusRate)<=radi*radi)
            {
                space+=1,shadowlist = (struct XY *)realloc(shadowlist,sizeof(struct XY)*space);//重新分配空间大小
                (shadowlist+space-1)->x = x;
                (shadowlist+space-1)->y = y;
            }
        }
    }
    ball->shadow = (struct XY *)malloc(sizeof(struct XY)*space);
    ball->shadow = shadowlist;
    return ball;//返回初始位置
}

//4.初始化球
struct Ball *ballInit(struct XY *center,int radi)
{
    struct Ball *ball;
    ball = (struct Ball *)malloc(sizeof(struct Ball));//为指针分配空间
    ball->radius = radi;//半径
    ball->center.x = center->x;//圆心位置
    ball->center.y = center->y;//圆心位置
    ball->alive = True;//圆存活
    ball = getBallshadow(ball);//阴影
    ball->speed = BallSpeed;//速度
    ball->direction.x = ball->direction.y = 0;//最后操作移动方向
    return ball;//返回
}

//4.1.初始化一个player球
struct Ball *myBallInit(struct XY *center,int radi)
{
    return ballInit(center,radi);
}

//4.2.初始化一个enemy球
struct Ball *enemyBallInit(struct XY *center,int radi)
{
    return ballInit(center,radi);
}

//4.3.获取多个enemy球
struct Ball **getManyEnemyBall(int number,int minradi,int maxradi)
{
    struct XY origin;
    origin.x = origin.y = 0;//原点
    struct Ball **enemyballlist,*enemyball;//指向"指向球的指针",相当于球列表
    enemyballlist = (struct Ball **)malloc(sizeof(struct Ball*)*number);//分配空间
    for(int list_index=0;list_index<number;)
    {
        struct XY center;
        int radi = minradi+rand()%(maxradi-minradi);
        center.x = rand()%(ScreenWidth-radi),center.y = rand()%(ScreenHight-radi);//随机圆心
        enemyball = enemyBallInit(&center,radi);
        if(list_index==0){enemyballlist[list_index++]=enemyball;}
        for(int i=0;i<list_index;i++)
        {
            int B2Bresult = judgeCrashB2B(enemyball,enemyballlist[i]),B2Wresult=judgeCrashB2W(enemyball,wallList);
            if(B2Bresult==True || B2Wresult==True){break;}//球与球有碰撞,球与墙有碰撞,跳出循环
            else if(B2Bresult==False && B2Wresult==False && i==list_index-1){enemyballlist[list_index++]=enemyball;}//不碰撞,并且是列表中的最后一个元素
        }
    }
    return enemyballlist;
}

//5.球移动
struct Ball *moveBall(struct Ball *ball,struct XY *direction)
{
    ball->center.x += direction->x;//重新获取中心
    ball->center.y += direction->y;
    for(int i=0;i<_msize(ball->shadow)/sizeof(struct XY);i++)//重新获取阴影坐标
    {
        ball->shadow[i].x += direction->x*ball->speed;
        ball->shadow[i].y += direction->y*ball->speed;
    }
    return ball;
}

//5.1.player球移动
struct Ball *myBallMove(struct Ball *ball)
{
    struct XY direction;//方向,球的原方向
    direction.x =ball->direction.x;
    direction.y =ball->direction.y;//不操作则按原方向移动
    if(ball->alive==True)//如果球存活
    {
        char key1;//获取用户输入
        if(_kbhit())//_kbhit()如果没有键盘输入返回0,有输入返回真
        {
            key1 = _getch();//_getch()获取一个字符
            if(key1==Left){direction.x=-1;direction.y=0;}
            if(key1==Right){direction.x=1;direction.y=0;}
            if(key1==Up){direction.y=-1;direction.x=0;}
            if(key1==Down){direction.y=1;direction.x=0;}
        }
    }
    ball = moveBall(ball,&direction);//移动球
    int B2Wflag;
    B2Wflag = judgeCrashB2W(ball,wallList);//判断是否撞墙
    if(B2Wflag==True)//撞墙反向移动
    {
        direction.x -= direction.x*2,direction.y -= direction.y*2;
        ball = moveBall(ball,&direction);
    }
    ball->direction.x = direction.x,ball->direction.y=direction.y;//记录最后位置记录,保证球打印正常
    return ball;
}

//5.2.enemy球移动
void enemyBallMove(struct Ball **enemy)
{
    struct XY direction;
    for(int i=0;i<_msize(enemy)/sizeof(struct Ball *);i++)
    {
        direction.x = -1+rand()%3;//随机方向
        direction.y = -1+rand()%3;
        if(enemy[i]->alive==True)//敌方球存活
        {
            enemy[i] = moveBall(enemy[i],&direction);//移动球
            int B2Wflag;
            B2Wflag = judgeCrashB2W(enemy[i],wallList);//判断是否撞墙
            if(B2Wflag==True)//撞墙反向移动
            {
                direction.x -= direction.x*2,direction.y -= direction.y*2;
                enemy[i] = moveBall(enemy[i],&direction);
            }
            enemy[i]->direction.x=direction.x,enemy[i]->direction.y = direction.y;//记录最后一次移动记录,保证打印球正常
        }
    }
}

//6.球吃球
void bEatb(struct Ball *player,struct Ball **enemyList)
{
    for(int i=0;i<_msize(enemyList)/sizeof(struct Ball *);i++)
    {
        if(judgeCrashB2B(player,enemyList[i])==True)//两球相撞
        {
            if(player->radius>enemyList[i]->radius)//player吃enemy
            {
                player->radius += 1;//player变大
                player = getBallshadow(player);
                enemyList[i]->alive = False;//修改enemy存活状态
                for(int j=0;j<_msize(enemyList[i]->shadow)/sizeof(struct XY);j++)//enemy位置打印背景
                {
                    gotoxy(enemyList[i]->shadow+j);
                    printf("%c",BackgroundBlock);
                }
            }
            if(player->radius<enemyList[i]->radius)//enemy吃player
            {
                player->alive = False;
                system("pause");
            }
        }
    }
}