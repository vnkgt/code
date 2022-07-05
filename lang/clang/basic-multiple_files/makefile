aim = main.exe
obj = myfunc_true.o test.o

# 将所有的.o文件链接成为可执行文件
$(aim):$(obj)
	gcc $(obj) -o $(aim)

# 将所有的.c文件生成.o文件
# myfunc_main.o:myfunc_main.c
# 	gcc -c myfunc_main.c -o myfunc_main.o

# test.o:test.c
# 	gcc -c test.c -o  test.o
%.o:%.c
	gcc -Wall -O -g -c $< -o $@
