/*
C4996错误解决:
	方法一:
		程序中添加一行:
		#define _CRT_SECURE_NO_WARNINGS
	方法二:
		程序中添加一行:
		#pragma warning(disable:4996)
	方法三(vs编辑器):
		在项目属性-->配置属性-->预处理器-->预处理定义-->编辑添加:_CRT_SECURE_NO_WARNINGS

*/