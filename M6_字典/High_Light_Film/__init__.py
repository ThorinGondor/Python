#创建一个字典：
UltraMan = {
    "color": ["red", "white"],
    "address": "M78星云",
    "height": 60,
    "age": 15000
}

print(UltraMan["color"])
print(UltraMan["address"])
print(UltraMan["height"])
print(UltraMan["age"])

#添加一对键值：
UltraMan["名字"] = "赛文奥特曼"
UltraMan["人间体"] = "凤森正辉"
print(UltraMan)

#安全删除一对键值：
if UltraMan["height"] == 60:
    del UltraMan["height"]
    print(UltraMan)

#遍历字典的键和值 此处语法不熟，为重点
for key, value in UltraMan.items():
    print(key)
    print(value)
print("遍历字典的键和值结束！")

#遍历字典所有的值value
for value in UltraMan.values():
    print(value)
print("遍历字典的值结束！")

#遍历字典所有的键key
for key in UltraMan.keys():
    print(key)
print("遍历字典的键结束！")