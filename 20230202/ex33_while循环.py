# 给while循环设定判断变量的初值
i = 0
# 定义一个空列表numbers
numbers = []

max = 8
# 循环判断变量i<6时
while i < max:
    print(f"At the top i is {i}")
    numbers.append(i)
# 判断标识+1
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
