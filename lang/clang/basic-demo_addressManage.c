//通讯录管理系统
/*
单通讯录文件
    通讯录文件:demo_Address_manage.txt
    总控函数                                    void Allcontrol();
    0.系统开始菜单                              void menu();
    1.初始化通讯录,读取通讯录文件的数据           void InitAddr();
    2.添加联系人                                void AddPerson();
    3.查看某个联系人                            void FindPerson();
      查看所有联系                              void FindAllPerson();
      查看联系人的个数                          void FindNumPerson();
    4.修改联系人                                void ChangePerson();
    5.删除联系人                                void DelPerson();
    6.退出系统                                  void ExitSystem();
    中间函数:
        确认函数                                int Confirm();
        判断联系人是否存在                       int IsExist();
*/
//头文件
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#define True 1              //真
#define False 0             //假
#define AddrMax 1024        //单个通讯录的最大长度
#define FileName "demo_Addr_manage.txt"         //保存数据的文件名
#define NameSize 10         //名字列表的长度

//函数声明
void Allcontrol();      //总控函数
void colcur(int num);   //颜色控制
void load();            //读取文件到列表
void save();            //列表保存到文件
void AddPerson();       //添加联系人
void FindAllPerson();   //查询所有人
void FindPerson();    //查询某个人
void ChangePerson();    //修改某个人
void DelPerson();       //删除某个
void DelAllPerson();    //删除所有

//通讯录
struct Addr{
    char name[NameSize];                  //名字
    int age;                        //年龄
    int gender;                     //性别(man:0,famale:1)
};
struct Addr AddrBook[AddrMax];      //创建临时存储数组
int Num_Person = 0;                 //人的个数



//0.总控函数                                    
void Allcontrol()
{
    while(True)
    {
        system("cls");
        load();//加载通讯录文件
        colcur(14);//切换颜色
        printf("**********************************\n");
        printf("***********1.Add Person***********\n");
        printf("********2.Find one Person*********\n");
        printf("********3.Find all Person*********\n");
        printf("*****4.Find number of Person******\n");
        printf("*******5.Change one Person********\n");
        printf("*******6.Delete one Person********\n");
        printf("*******7.Delete all Person********\n");
        printf("**********0.Exit System***********\n");
        printf("**********************************\n\n");
        printf("please input your option:\n\t");
        char user_option='\0';//用户选项
        user_option=getchar();
        switch(user_option){
            case '1'://添
                AddPerson();
                break;
            case '2'://查找一个
                FindPerson();
                break;
            case '3'://查找所有
                FindAllPerson();
                break;
            case '4'://查询人数
                printf("Number of Person:%d\n",Num_Person);
                system("pause");
                break;
            case '5'://修改信息
                ChangePerson();
                break;
            case '6'://删除某个
                DelPerson();
                break;
            case '7'://删除所有
                DelAllPerson();
                break;
            default:
                break;
        }
        save();//保存通讯录文件
        if(user_option=='0'){colcur(13);printf("Goodbey!\n");break;}//退出
    }
    colcur(15);//切换颜色
    system("pause");
}

//光标颜色控制(15号为白色)
void colcur(int num)//num:颜色色号
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),num);
}

//0.读取文件到列表
void load()
{
    Num_Person=0;
    FILE *fp = fopen(FileName,"r");
    if(fp==NULL){FILE *fp=fopen(FileName,"w");fclose(fp);return;}//文件打开失败则创建
    while(True)
    {
        int flag,age,gender;
        char name[NameSize];
        flag=fscanf(fp,"%s -- %d -- %d\n",name,&age,&gender);
        if(flag==-1){break;}
        strcpy(AddrBook[Num_Person].name,name);
        AddrBook[Num_Person].age = age;
        AddrBook[Num_Person].gender = gender;
        Num_Person++;   //人数加一
    }
    fclose(fp);
}

//0.将列表保存到文件
void save()
{
    FILE *fp = fopen(FileName,"w");
    for(int i=0;i<Num_Person;i++)
    {
        fprintf(fp,"%s -- %d -- %d\n",AddrBook[i].name,AddrBook[i].age,AddrBook[i].gender);
    }
    fclose(fp);
}

//0.确认判断
int Confirm()
{
    fflush(stdin);
    printf("Are you confirm[yes is '1'/no is random char]:\n\t");
    char user_option=getchar();
    if(user_option=='1'){return True;}
    else{return False;}
}

//1.添加
void AddPerson()
{
    fflush(stdin);
    int age,gender;
    colcur(1);
    printf("input name:\n"),scanf("%s",AddrBook[Num_Person].name);   //名字
    while(True)                                 //年龄
    {
        fflush(stdin);
        printf("input age:\n");
        scanf("%d",&age);
        if(age>108 || age<0){printf("age outside!!!\n");continue;}
        AddrBook[Num_Person].age = age;
        break;
    } 
    while(True)
    {           
        fflush(stdin);   
        printf("input gender:\n");                                              //性别
        scanf("%d",&gender);
        if(gender!=0 && gender!=1){printf("gender outside!!!\n");continue;}
        AddrBook[Num_Person].gender=gender;
        break;
    }
    Num_Person++;            //人数加一
    colcur(15);
}

//2.查询某个人
void FindPerson()
{
    colcur(2);
    char name[NameSize];
    printf("Who you want to find please input name:\n\t");
    scanf("%s",name);
    for(int i=0;i<Num_Person;i++)
    {
        if(strcmp(name,AddrBook[i].name)==0)
        {
            printf("name:%s\tage:%d\tgender:%s\n",AddrBook[i].name,AddrBook[i].age,AddrBook[i].gender==0?"man":"female");
            break;
        };
        if(i==Num_Person-1){printf("Find failed Not found a person who called %s!!!\n",name);}
    }
    system("pause");
}

//3.查询所有人
void FindAllPerson()
{
    colcur(2);
    int count=0;
    for(int i=0;i<Num_Person;i++)
    {
        printf("name:%s\tage:%d\tgender:%s\n",AddrBook[i].name,AddrBook[i].age,AddrBook[i].gender==0?"man":"female");
        count++;
    }
    if(count==0){printf("There is a empty address book!!!\n");}
    system("pause");
}

//5.修改
void ChangePerson()
{
    fflush(stdin);
    colcur(11);
    char name[NameSize];
    printf("Who you want to find please input name:\n\t");
    scanf("%s",name);
    for(int i=0;i<Num_Person;i++)//找人
    {
        if(strcmp(name,AddrBook[i].name)==0)//找到修改
        {
            int gender,age;
            printf("Change name:\n"),scanf("%s",AddrBook[i].name);   //名字
            while(True)                                 //年龄
            {
                fflush(stdin);
                printf("Change age:\n");
                scanf("%d",&age);
                if(age>108 || age<0){printf("age outside!!!\n");continue;}
                AddrBook[i].age = age;
                break;
            } 
            while(True)
            {           
                fflush(stdin);   
                printf("Change gender:\n");                                              //性别
                scanf("%d",&gender);
                if(gender!=0 && gender!=1){printf("gender outside!!!\n");continue;}
                AddrBook[i].gender=gender;
                break;
            }
            printf("Have Changed %s!!!\n",name);
            break;
        };
        if(i==Num_Person-1){printf("Change Failed not found %s!!!\n",name);}//没有找到
    }
    system("pause");
}


//6.删除某个人
void DelPerson()
{
    colcur(12);
    char name[NameSize];
    printf("Who you want to find please input name:\n\t");
    scanf("%s",name);
    int user_option = Confirm();//用户再次确定
    if(user_option!=True){printf("Have cancel the operation Delete %s!!!\n");system("pause");return;}
    for(int i=0;i<Num_Person;i++)
    {
        if(strcmp(name,AddrBook[i].name)==0)
        {
            Num_Person--;//人数减一
            for(int j=i;j<Num_Person;j++)//找到要删除的人
            {
                strcpy(AddrBook[j].name,AddrBook[j+1].name);
                AddrBook[j].age = AddrBook[j+1].age;
                AddrBook[j].gender = AddrBook[j+1].gender;
            }
            printf("Del %s successed!!!\n",name);
            break;
        };
        if(i==Num_Person-1){printf("Del failed Not found a person who called %s!!!\n",name);}
    }
    system("pause");
}

//7.删除所有
void DelAllPerson()
{
    colcur(12);
    int user_option=Confirm();
    if(user_option==True){Num_Person=0;printf("Have del all!!!\n");}
    else{printf("Have cancel the operation to Delete All!!!\n");};
    system("pause");
}

//主函数/函数入口
void main(int argc,char *argv[])
{
    Allcontrol();
}
