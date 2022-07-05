/*
不定长度字符串:
    1)直接赋值不定长度的字符串
    2)输入获取不定长度的字符串
*/
#include <stdio.h>
#include <stdlib.h>


//函数声明
void *var_string();


//主函数
void main()
{
  //1)直接赋值不定长度的字符串
  printf("1)直接赋值不定长度的字符串\n");
  char *var_init_get;
  var_init_get = "var string of inital get!\n\n";
  printf("var_init_get:%s\n", var_init_get);

  //2)输入获取不定长度的字符串
  printf("2)输入获取不定长度的字符串\n");
  void *var_input_get;   //也可以为char *var_input_get;
  printf("input var_input_get:\n");
  var_input_get = var_string();
  printf("output var_input_get:\n");
  printf("%s\n", var_input_get);
}


//输入不定长度的字符串
void *var_string(){
  char *var=NULL;
  int counter=0,var_value;
  //给初始空间
  var = (void *)malloc(1);
  //判断字符是否为"\n"
  while((var_value = getchar())!='\n')
  {
  //给var_string数组赋值
  var[counter++] = var_value;
  //重新分配内存,realloc(指针)
  var=(void *)realloc(var, counter);
  }
  //赋值完成时,给最后一个地址赋值
  var[counter] = 0;
  //首地址返回
  return var;
}