/*
=>clang实现批量处理
    文件操作
        1.显示md5
        2.修改md5
        3.判断文件类型(使用16进制表示)
    文件夹操作
        1.遍历文件夹下的所有文件及子文件夹
        2.批量删除空文件夹
        3.批量修改文件名(添加后缀,删除后缀,文件名中的特殊字符串)
        4.批量文件名中的特殊字符串
        5.批量修改md5
        6.每n个文件移动到一个文件夹
*/

#include <stdio.h>
#include <io.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include "clang-list.c"


int main(int argc,char *argv[]){
    char *srcPathName = "D:/entertain/img"; //源文件路径
    DIR *srcPath = opendir(srcPathName);    //打开源文件夹
    struct dirent *sonDir = readdir(srcPath);   //子文件夹
    struct stat *statinfo;
    int staterr = stat("./clang-list.c",statinfo);
    printf("main info>>>%s\n",staterr);
    return 0;
}