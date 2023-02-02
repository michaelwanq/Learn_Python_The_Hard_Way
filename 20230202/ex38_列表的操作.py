# 定义列表ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# 对对象ten_things调用函数split进行分隔，以“ ”为分隔符，将处理后的对象列表赋值给stuff
stuff = ten_things.split(' ')
# 定义列表more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
# 定义循环，判断依据是变量stuff的值不为10
while len(stuff) != 10:
    # 从变量more_stuff取值并插入到stuff列表中
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

# 打印处理后的变量stuff，包含10个元素的列表
print("There we go: ", stuff)

print("Let's do some things with stuff.")

# 打印stuff列表中的第二个元素
print(stuff[1])
# 打印stuff列表中的倒数第一个元素
print(stuff[-1])  # whoa! fancy
# 打印从stuff列表中弹出的最后一个元素
print(stuff.pop())
# 以“ ”为分隔符，将stuff列表打印成字符串
print(' '.join(stuff))  # what? cool!
# 以“#”为分隔符，将stuff列表的第4个、第5个字符打印成字符串
print('#'.join(stuff[3:5]))  # super stellar!
