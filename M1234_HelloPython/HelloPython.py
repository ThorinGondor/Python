message = "hello!"+"python!"+'\n'
print(message*5)
print(message.title())
print(message.upper())
print(message.lower())

########################################################

#列表：可存储不同类型的数据，列表可修改（可变），使用方括号
array = ["Rose",23,17.69305,True,[False,"Curry",57.81]]
print(array)
array[0] = "James"  #修改列表的元素
print("array[0]:"+array[0])
print(array[4])

array.append("Durant") #向列表添加元素
print(array)
array.insert(2,True) #向列表添加元素
print(array)

del array[3] #删除元素的三个方法
array.remove(23)
print(array)
array.pop()
print(array)

array.reverse() #倒着输出array
print(array)

#列表sort() 排序
list0 =["Durant","Curry","Thompson","Green","Livingston","West"]
list0.sort()
print(list0)
print(list0.__len__())

########################################################

#遍历列表
for buff in array:
    print(buff)
print("遍历结束！\n")

for buff in list0:
    print(buff)
print("遍历结束！\n")

#随机生成数： range() 函数的使用
for buff in range(1,10,2):
    print(buff)
print("遍历结束！\n")

#随机生成数列表化
numArray = list(range(2,12,2))
print(numArray)

buffers = []
for arr in range(10,30,2):
    arr = arr*2
    buffers.append(arr)
print("遍历结束！\n")

#对数字列表统计计算
print(buffers)
print(max(buffers))
print(min(buffers))
print(sum(buffers))

#使用列表的一部分
print(buffers[:3])
print(buffers[1::2])

#复制列表
newBuffers = buffers[:]
print(newBuffers)

########################################################

#元祖tuple：不可修改（不可变）,使用圆括号
dimensions = (19,81.7145,"Durant","James",True)
print(dimensions)

for buff in dimensions:
    print(buff)
print("遍历结束！")

#元祖虽然不可修改，但是可以重新赋值
dimensions = (1,2,3)
print(dimensions)