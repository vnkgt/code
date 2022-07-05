//打字游戏
/*
流程:
	生成随机字母===>获取用户输入字符===>对比显示===>统计时间级正确率
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
//随机字母的个数
#define WORD_NUM 15


void main()
{
	srand((unsigned int) time(NULL));	//确保每次游戏的随机字符串不同
	int success_num=0;				//玩家正确输入的个数
	//1生成随机字母
	char str[WORD_NUM];
	printf("string:\n\t");
	for(int i=0;i<WORD_NUM;i++){
		str[i] = rand() % 25+'a';
		printf("%c",str[i]);
	}
	printf("\nplace input string above:\n\t");
	int start_time = time(NULL);	//开始时间
	//2获取用户输入的数据并对比
	char gamer_get_char;
	for(int i=0;i<WORD_NUM;i++){
		gamer_get_char = _getch();	//获取玩家输入的数据,并且不需要回车就可以显示(getchar回车才能显示字符)
		if(gamer_get_char==str[i]){	//输入正确
			printf("%c",str[i]);
			success_num++;
		}
		else{						//输入错误
			printf("*");
		}
	}
	int end_time = time(NULL);		//完成时间
	printf("\n");
	//3统计时间级正确率
	printf("total_game_time:%ds\n",end_time-start_time);
	printf("success_percentage:%0.2f%%\n",((double) success_num/(double) WORD_NUM)*100);
}