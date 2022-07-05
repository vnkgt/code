/*
=>golang实现多任务/并发
	goroutine多用来解决“并发任务”,而非“时序任务”
	goroutine与线程、进程、协程之间有所不同,可以把goroutine理解成为线程
	开启线程->goroutine
		//开启一个线程
		//func/methon:函数或者方法
			go <func/methon>
	线程通信->通道channel
		//把通道理解为堆栈,元素只能够push和pop,值被pop出后,就不再保存在堆栈中,除非重新push一个值进去
		//通道(channel)更为特殊,通道两端的goroutine一般不同,从而实现两个goroutine直接的通信
			eg:
				//"main"goroutine<---ch通道--->"main"goroutine,通道连接两端的goroutine相同,不合法
				func main() {
					var ch = make(chan int)
					ch <- 11				//会直接报错,"该通道的声明"与"给该通道push推值"在同一个goroutine内
				}
				//"main"goroutine<---ch通道--->"giveValue"goroutine,通道两端的goroutine不同,合法
				var ch chan int
				go func giveValue() {ch <- 13}()		//单独开启一个goroutine,声明一个函数后立即调用
				fmt.Println(<-ch)

		注意点:
			1)只有goroutine存在时,通道才能使用
			2)通道中的值被取走后,通道重新变为空
			3)等待空通道会发生阻塞
				eg:
					fatal error: all goroutines are asleep - deadlock!	->	该错误信息,通常由等待空通道阻塞导致
			4)只要使用"<- <chanName>",就会取走通道中的值,使通道为空,无论是打印还是取走通道中的值给一个新变量
		//创建通道变量
		//chanName:通道变量名
		//chanDatatype:通道中允许传输的数据类型
			var <chanName> chan <chanDatatype>
			var <chanName> = make(chan <chanDatatype>)
		//获取通道中的值
		//把通道chanName中的值传给argName
			var <argName> = <- <chanName>
		//给通道传值
		//将value值传给chanName
			<chanName> <- <value>
		//关闭通道,通道关闭后给通道传值会报错.获取通道的值是对应类型的零值
			close(<chanName>)
		//判断通道是否关闭
		//chanValue:通道的值
		//chanCondition:通道是否关闭,若已经关闭则为false
			var <chanValue>,<chanCondition> = <- <chanName>
	互斥锁mutual->保证线程能够运行完成
		//关闭互斥锁
			sync.Mutex.Lock()

		//打开互斥锁
			sync.Mutex.Unlock()
	多通道处理->select
		//select作用:使多个goroutine运行逻辑清晰,使用select语句可以
		//基本写法
			select{									//每个select只会执行一个case,哪个通道先有值就执行哪个case
				case <arg> := <- <chanNameA>:		//等待chanNameA的值,并将值赋给arg
					<sentence>						//根据通道的值,执行相应的语句
				case <-<chanNameB>:					//等待chanNameB通道的值
					<sentence>
				default:							//默认任务,case中通道中均没有值时
					<sentence>
			}

	通道等待时间->实现限时任务,超时即放弃
		//实现限时任务
			<timeLimitChan> = time.After(<timeLimit>)	//创建一个最高等待时长为timeLimit的通道
			select{
				case <arg> := <- <chanName>:		//在timeLimit限制时间内,获取到了chanName的值
					<sentence>	//准时任务
				case <- <timeLimitChan>:			//超过timeLimit,执行下列语句
					<sentence>	//超时任务,可以什么都不做
				default:							//case都不成立时,执行default
					<sentence>	//默认任务
			}
		//时间对象time.Duration
			time.Sleep(time.Duration(rand.Intn(4000))*time.Millisecond)
*/

//以工厂为例,“打螺丝/涂漆/组装”是同时进行的
//分配任务,打螺丝/涂漆/组装,通过mainChan主流水线进行通信,统计加工总件数
package main

import (
	"fmt"
	"sync"
	"time"
)

var mu sync.Mutex

func main() {
	var mainChan = make(chan int)
	var logList = make([]int, 2) //记录任务的执行者
	var totalWorkpiece = 0
	var aimWorkpiece = 10 //目标总工件数
	//开启分配任务
	fmt.Println("task distribute...")
	for i := 0; i < 10; i += 1 {
		go hitScrew(mainChan) //开启goroutine
		go paint(mainChan)
		go assemble(mainChan)
	}
	//任务分配结束,等待统计任务执行结果
	fmt.Println("task statistic...")
	for {
		timeLimitChan := time.After(time.Second) //限时通道
		select {                                 //select等待加工函数运行完成
		case getWorkpieceNum := <-mainChan:
			{
				logList = append(logList, getWorkpieceNum)
				totalWorkpiece += getWorkpieceNum
			}
		case <-timeLimitChan:
			{
				fmt.Println("task out of time...")
			}
		default:
			{
			} //默认不做任何处理
		}
		if totalWorkpiece == aimWorkpiece { //达到目标工件数,跳出等待
			break
		}
	}
	fmt.Println("task finisher log...", logList)
	fmt.Println("\n\n all task finish...")
}

//打螺丝
func hitScrew(mainChan chan int) { mainChan <- 1 }

//涂漆
func paint(mainChan chan int) { mainChan <- 2 }

//组装
func assemble(mainChan chan int) { mainChan <- 3 }
