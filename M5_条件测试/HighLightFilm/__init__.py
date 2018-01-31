array = ["Kirk", "Tom", "Booker", "Curry"]

user = "marry"
if user.title() not in array:
    print(user.title()+"用户并不存在！")
else:
    print(user.title()+"用户存在！")

admin = "curry"
if admin.title() in array:
    print(admin.title()+"用户存在！")
else:
    print(admin.title()+"用户不存在！")