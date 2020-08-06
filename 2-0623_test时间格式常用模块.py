print ("你好")
import time #引入time模块
import pdb  #引入断点模块
#Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
#时间间隔是以秒为单位的浮点小数。
#每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
#Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳,

import datetime
print(datetime.datetime.today())            #输出当前时间

print(time.time())                  #从1970-1-1起到现在的时间戳
print(time.ctime())                 #当前日期
print(time.ctime(time.time()-86400))    #将时间戳转化成字符串
print(time.gmtime())                #将当前时间戳转化成struct_time格式
print(time.localtime())             #将本地时间戳转化成struct_time格式
print(time.mktime(time.localtime()))    #与localtime()相反
#time.sleep(3)                           #阻塞时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))    #将struct_time格式转换成指定格式
print(time.strptime('2012-12-12', '%Y-%m-%d'))

ticks =time.time()
print("当前时间为：",ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime1 = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime1)

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

#Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar

cal = calendar.month(2020, 6)
print ("以下输出2020年6月份的日历:")
print (cal)

str = 'Hello World!'

print (str) # 输出完整字符串
print (str[0]) # 输出字符串中的第一个字符
print (str[2:5]) # 输出字符串中第三个至第五个之间的字符串
print (str[2:]) # 输出从第三个字符开始的字符串
print (str * 2) # 输出字符串两次
print (str + "TEST") # 输出连接的字符串

#列表list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list) # 输出完整列表
print (list[0]) # 输出列表的第一个元素
print (list[1:3]) # 输出第二个至第三个的元素 
print (list[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) # 输出列表两次
print (list + tinylist) # 打印组合的列表
pdb.set_trace()  #设置断点
list.insert(3,'asd')
print(list)
list.append('orang')
print(list)
list.remove( 'john')
print(list)
list.reverse()  
print(list)
li =[2,7,4,10,32,5]
li.sort()  #小到大排序，数字跟字符串不能混用
print(li)


#字符串操作
pdb.set_trace()  #设置断点
name_old='ace,orange,bfmq   '
name=name_old.strip()           #去空格（默认）
name1=name.split(',')           #以，为分隔符切割后放入列表
print(name1)
name2='~'.join(name1)           #将列表中个元素以~为分隔符组合成一个字符串
print(name2)
print(name.capitalize())        #首字符大写
print(name.center(20,'*'))      #左右打印*,一共20个值，装逼加特效用
#name.isdigit()                 #检测是否为int类型，现在不是会报错，不执行了



#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print (tuple) # 输出完整元组
print (tuple[0]) # 输出元组的第一个元素
print (tuple[1:3]) # 输出第二个至第三个的元素 
print (tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2) # 输出元组两次
print (tuple + tinytuple) # 打印组合的元组

#Dictionary字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one']) # 输出键为'one' 的值
print (dict[2]) # 输出键为 2 的值
print (tinydict) # 输出完整的字典
print (tinydict.keys()) # 输出所有键
print (tinydict.values()) # 输出所有值

pdb.set_trace()  #设置断点
s1 = {'a','b','c','a','d',}
print(s1)                       #重复的元素只会出现一次哦
print(type(s1))                 #类型是set，集合类型
s1.add('w')                     #增加元素
s1.add('w')                     #重复增加并没有什么卵用
s1.add('w')                     #没什么卵用的用三遍
s1.add('w')
print(s1)
s1.remove('w')                  #删除元素，如果元素不存在会报错
s1.discard('dsds')              #删除元素，如果元素不存在不会报错
print(s1)
r1 = s1.pop()                   #随机移除一个元素并获取他
print(r1)
s1.clear()                      #全部清空
print(s1)
s1 = {'a','b','c','a','d',}
s2 = {'a','b','e','f',}
s = s1.difference(s2)           #s1s2中不同的元素
print(s)
#s1.difference_update(s2)        #与s2进行对比然后直接将不同的元素更新到s1中
s3 = s1.symmetric_difference(s2)#s1与s2的对称差集
print(s3)
s4 = s1.intersection(s2)        #交集
print(s4)
s5 = s1.union(s2)               #并集
print(s5)


f1 = lambda a1:a1 + 10      #简易函数跟上面一个意思
ret = f1(10)
print(ret)
