/*
log:
	2022.06.22.21.37	v2.3优化md5的修改
	2022.06.21.12.41	v2.2优化菜单打印功能
	2022.06.19.18.20	v2.1完善菜单功能,bug:无法实现执行菜单功能后暂停命令行窗口
		menu01()-menu08()
	2022.06.18.17.41	v2.0添加菜单功能,命令行交互功能
		run()
		menu01()-menu08()
	2022.06.17.18:34	v1.0完成基础功能
		pathWalk()	//遍历文件及文件夹;参数为文件夹的路径
		moveFile()	//移动一个文件,修改一个文件名
		subString()	//正则匹配,替换对应的字符串
		addExt()	//添加一个文件后缀名;参数为文件名,不含路径
		subExt()	//删除一个文件后缀名;参数为文件名,不含路径
		showMd5()	//显示一个文件md5;参数含路径
		changeMd5()	//修改一个文件md5;参数含路径
		judgeEmptyDir()	//判断一个文件夹是否为空;参数为文件夹名,不含路径
		sortMapByKey()	//给map[string]string按key正序排序
	|=>
	|-path = root + file	path:路径	file:文件/文件夹	root:file所在的父路径
	|-file = name + ext		name:名称	ext:文件后缀名
		=>path = root + (name + ext)
os.FileInfo接口结构:
	type FileInfo interface {
		Name() string       // base name of the file
		Size() int64        // length in bytes for regular files; system-dependent for others
		Mode() FileMode     // file mode bits
		ModTime() time.Time // modification time
		IsDir() bool        // abbreviation for Mode().IsDir()
		Sys() any           // underlying data source (can return nil)
	}
	os.Stat(<path> string)	// 将path转换为FileInfo,只适用于文件
	os.Remove(<path>)
		//删除文件
		//删除空目录
		//如果待删除文件/目录不存在，则返回错误
	os.RemoveAll(<path>)
		//删除文件
		//删除目录，目录为空或者不为空，均可
		//如果待删除文件/目录不存在，不返回错误
	filepath.Base(<path>) //获取文件名,或文件夹名
	filepath.Dir(<path>)  //获取路径
*/

package main

import (
	"crypto/md5"    //md5计算
	"errors"        //错误处理
	"fmt"           //信息打印
	"io"            //文件读写操作
	"os"            //文件基本函数及数据结构
	"path"          //路径分割
	"path/filepath" //路径操作
	"regexp"        //正则匹配
	"sort"          //排序
	"strings"       //字符串匹配
)

//1->pathWalk:文件遍历
func pathWalk(srcPath string) (files, dirs []string, err error) {
	srcPathInfo, err := os.Stat(srcPath)
	if err != nil || srcPathInfo.IsDir() == false {
		fmt.Println("error...路径错误!!!")
		return nil, nil, errors.New("error...路径错误!!!")
	}
	//所有文件的路径及文件信息
	//map[文件/文件夹名路径]文件信息
	var allFileMap = make(map[string]os.FileInfo, 1)
	//遍历srcPath路径---->函数核心
	filepath.Walk(srcPath, func(path string, info os.FileInfo, err error) error {
		allFileMap[path] = info
		return nil
	})
	//创建返回的文件夹,文件字典
	// var fileMap = make(map[string]string, 0)	//内部不包含,重名文件
	// var dirMap = make(map[string]string, 0)	//内部不包含,重名文件夹
	var fileSlice = make([]string, 0) //内部包含,不同路径的重名文件
	var dirSlice = make([]string, 0)  //内部包含,不同路径的重名文件
	//获取所有的文件及文件夹
	for path, info := range allFileMap {
		// name := filepath.Base(path) //获取文件名,或文件夹名
		// root := filepath.Dir(path)  //获取路径
		if info.IsDir() == true { //判断为文件夹
			dirSlice = append(dirSlice, filepath.ToSlash(path)) //filepath.ToSlash(),将路径分割符转换为'/'
		}
		if info.IsDir() == false { //判断为文件
			fileSlice = append(fileSlice, filepath.ToSlash(path))
		}
	}
	return fileSlice, dirSlice, nil
}

//2->moveFile:文件移动
func moveFile(oldpath, newpath string) error {
	err := os.Rename(oldpath, newpath)
	return err
}

//3.1->subString:替换一个文件名中的某些部分为空字符串
func subString(file, aim, replor string) string {
	result, _ := regexp.Compile(aim)
	new := result.ReplaceAll([]byte(file), []byte(replor))
	return string(new)
}

//3.2->addExt:为一个文件添加后缀名
func addExt(file, ext string) string {
	return (file + ext)
}

//3.3->subExt:去掉一个文件后缀名
func subExt(file string) string {
	return file[:len(file)-len(path.Ext(file))] //path.Ext()获取文件后缀名
}

//4.1->showMd5:显示一个文件md5
func showMd5(path string) string {
	file, _ := os.Open(path)        //打开文件
	defer file.Close()              //关闭文件
	md5Handle := md5.New()          //创建 md5 句柄
	io.Copy(md5Handle, file)        //将文件内容拷贝到 md5 句柄中
	md := md5Handle.Sum(nil)        //计算 MD5 值，返回 []byte
	md5str := fmt.Sprintf("%x", md) //将 []byte 转为 string
	return md5str
}

//4.2->changeMd5:修改一个文件的md5
func changeMd5(path string) {
	// 以只写的模式，打开文件
	file, _ := os.OpenFile(path, os.O_WRONLY, 0644)
	// 查找文件末尾的偏移量
	n, _ := file.Seek(0, os.SEEK_END)
	// 从末尾的偏移量开始写入内容
	file.WriteAt([]byte("vgt"), n) //在文件末尾写入"vgt",以此来修改md5
	defer file.Close()             //关闭文件
}

//5->judgeEmptyDir:判断一个文件夹是否为空文件夹,true:空,false:非空;本函数基于main.pathWalk()函数
func judgeEmptyDir(path string) bool {
	sonfiles, _, _ := pathWalk(path) //sonfiles:path及path子文件夹下的所有文件
	if len(sonfiles) == 0 {
		return true
	}
	return false
}

//对map按key(键进行排序),map类型:map[string]string
func sortMapByKey(srcMap map[string]string) []string {
	tempSlice := make([]string, 1) //排序slice
	for key, _ := range srcMap {
		if key != "" { //排除空值的影响
			tempSlice = append(tempSlice, key)
		}
	}
	sort.Strings(tempSlice) //对tempSlice进行排序
	return tempSlice
}

//run->主控函数,获取命令行参数并运行相应的命令
func run() error {
	//程序开始执行
	fmt.Println("program starting...")
	fmt.Println("本程序包含的功能:\n\t1.批量修改文件名\n\t2.批量移动文件\n\t3.批量修改md5")
	//获取源文件夹路径
	var srcPath string
	fmt.Printf("输入文件或文件夹路径(相对或绝对路径):\n\t=>")
	fmt.Scan(&srcPath)
	srcPath = filepath.ToSlash(srcPath) //将路径中的'\'全部转换为'/'
	//判断是文件还是文件夹
	srcPathInfo, err := os.Stat(srcPath)
	dirFlag := (err != nil || srcPathInfo.IsDir()) //存在该路径,并且为文件夹
	//打印文件夹操作菜单
	if dirFlag == true {
		dirHandleMenu(srcPath)
	}
	//打开单个文件操作菜单
	if dirFlag == false {
		singleHandleMenu(srcPath)
	}
	fmt.Println("program ending...")
	return nil
}

//文件夹批处理程序
func dirHandleMenu(srcPath string) error {
	//打印菜单
	files, dirs, err := pathWalk(srcPath) //重新遍历路径
	if err != nil {
		return err
	} //文件遍历出现错误
	fmt.Println("-------------------------文件的批量处理------------------------")
	fmt.Println("*****[01]打印遍历的文件,文件路径")
	fmt.Println("*****[02]去掉文件的后缀名")
	fmt.Println("*****[03]为文件添加一个后缀名")
	fmt.Println("*****[04]修改文件的后缀名")
	fmt.Println("*****[05]修改所有文件的md5值")
	fmt.Println("*****[06]将所有文件移动到同一个路径")
	fmt.Println("*****[07]删除该文件下的所有空文件夹")
	fmt.Printf("请输入选项\n\t=>")
	var choiceFlag int
	fmt.Scan(&choiceFlag)
	switch choiceFlag {
	case 1:
		menu01(files, dirs)
	case 2:
		menu02(files)
	case 3:
		menu03(files)
	case 4:
		menu04(files)
	case 5:
		menu06(files)
	case 6:
		menu07(files)
	case 7:
		menu08(dirs)
	default:
		fmt.Println("没有该选项...")
	}
	return nil
}

func singleHandleMenu(srcPath string) error {
	fmt.Println("-------------------------单个文件的处理------------------------")
	fmt.Println("*****[01]修改md5")
	fmt.Println("*****[02]显示md5")
	fmt.Printf("请输入选项\n\t=>")
	var choiceFlag int
	fmt.Scan(&choiceFlag)
	switch choiceFlag {
	case 1:
		changeMd5(srcPath)
		fmt.Println("md5 change sucess...", srcPath)
	case 2:
		fmt.Printf("%v--->%v\n", srcPath, showMd5(srcPath))
	}
	return nil
}

//菜单功能的实现
//[01]打印遍历的文件,文件路径
func menu01(files, dirs []string) {
	fmt.Println("all file and filepath")
	for index := range files {
		path := files[index]
		fmt.Println("\t", path)
	}
	fmt.Println("all dir and dirpath")
	for index := range dirs {
		path := dirs[index]
		fmt.Println("\t", path)
	}
}

//[02]去掉文件的后缀名
func menu02(files []string) {
	for index := range files {
		oldfpath := files[index]
		name := filepath.Base(oldfpath)
		root := filepath.Dir(oldfpath)
		newf := subExt(name)
		newfpath := filepath.Join(root, newf)
		os.Rename(oldfpath, newfpath) //修改文件名
		fmt.Println("修改完成")
		fmt.Println("\toldpath...", oldfpath)
		fmt.Println("\tnewpath...", newfpath)
	}
}

//[03]为文件添加一个后缀名
func menu03(files []string) {
	fmt.Printf("输入添加的后缀(以.开头)\n\t=>")
	var ext string
	fmt.Scan(&ext)
	if strings.HasPrefix(ext, ".") {
		for index := range files {
			oldfpath := files[index]
			name := filepath.Base(oldfpath)
			root := filepath.Dir(oldfpath)
			newf := addExt(name, ext)
			newfpath := filepath.Join(root, newf)
			os.Rename(oldfpath, newfpath) //修改文件名
			fmt.Println("修改完成")
			fmt.Println("\toldpath...", oldfpath)
			fmt.Println("\tnewpath...", newfpath)
		}
	} else {
		fmt.Println("输入的后缀名格式有误")
	}
}

//[04]修改文件的后缀名
func menu04(files []string) {
	fmt.Printf("输入添加的后缀(以.开头)\n\t=>")
	var ext string
	fmt.Scan(&ext)
	if strings.HasPrefix(ext, ".") {
		for index := range files {
			oldfpath := files[index]
			name := filepath.Base(oldfpath)
			root := filepath.Dir(oldfpath)
			newf := addExt(subExt(name), ext)
			newfpath := filepath.Join(root, newf)
			os.Rename(oldfpath, newfpath) //修改文件名
			fmt.Println("修改完成")
			fmt.Println("\toldpath...", oldfpath)
			fmt.Println("\tnewpath...", newfpath)
		}
	} else {
		fmt.Println("输入的后缀名格式有误")
	}
}

//[05]修改一个文件的md5值
func menu05() {
	var path string
	fmt.Println("输入要修该md5的文件路径")
	fmt.Scan(&path)
	fmt.Println("\tbefore change md5...", showMd5(path))
	changeMd5(path) //修改md5
	fmt.Println("\tafter change md5...", showMd5(path))
}

//[06]修改所有文件的md5值
func menu06(files []string) {
	var flag int
	fmt.Printf("是否显示文件修改前后的md5?(数字1开启,其它关闭)\n\t=>")
	fmt.Scan(&flag)
	for index := range files {
		path := files[index]
		fmt.Println("md5修改完成...", path)
		if flag == 1 {
			fmt.Println("\tbefore change md5...", showMd5(path))
		}
		changeMd5(path) //修改md5值
		if flag == 1 {
			fmt.Println("\tafter change md5...", showMd5(path))
		}
	}
}

//[07]将所有文件移动到同一个路径
func menu07(files []string) {
	var aimpath string //移动的目标文件夹
	fmt.Printf("所有文件要移动到哪个文件夹(不存在的话需要自行创建)...\n\t=>")
	fmt.Scan(&aimpath)
	for index := range files {
		oldfpath := files[index]
		name := filepath.Base(oldfpath) //文件全名
		frontname := subExt(name)       //文件名
		ext := filepath.Ext(name)       //后缀名
		newfpath := filepath.Join(aimpath, name)
		//不存在文件或者源路径与目标路径一致,则移动
		_, err := os.Stat(newfpath)
		for err == nil && filepath.ToSlash(oldfpath) != filepath.ToSlash(newfpath) { //存在同名文件
			frontname = frontname + "-vgt" //文件名添加"-vgt",以免报错
			name = frontname + ext
			newfpath = filepath.Join(aimpath, name)
			_, err = os.Stat(newfpath)
		}
		os.Rename(oldfpath, newfpath)
		fmt.Println("移动完成")
		fmt.Println("\toldpath...", oldfpath)
		fmt.Println("\tnewpath...", newfpath)
	}
}

//[08]删除该文件下的所有空文件夹
func menu08(dirs []string) {
	emptydir := make([]string, 0) //空文件夹的路径
	for index := range dirs {
		path := dirs[index]
		finfo, err := os.Stat(path)
		if err == nil && finfo.IsDir() == true {
			sonfiles, _, _ := pathWalk(path) //文件夹下及其子文件夹下的所有文件
			if len(sonfiles) == 0 {
				emptydir = append(emptydir, path)
			}
		}
	}
	//去掉相互包含的路径
	if len(emptydir) != 0 {
		sort.Strings(emptydir) //排序
		// sort.Reverse(emptydir)	//逆序排列
		for index := len(emptydir); index > 0; index += 1 {
			fmt.Println("\tempty dir...", emptydir[index])
		}
		//确认删除空文件夹
		var delFalg string
		fmt.Printf("\t再次确认,是否删除所有空文件夹?(y/n)\n\t=>")
		fmt.Scan(&delFalg)
		if delFalg == "y" || delFalg == "yes" {
			for index := range emptydir {
				path := emptydir[index] //路径
				os.Remove(path)
				fmt.Println("\tdel empty dir success...", path)
			}
		}
	} else {
		fmt.Println("没有空文件夹...")
	}
}

//-----------------------------------main函数------------------------------------->
func main() {
	run()
}
