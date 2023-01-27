# 定义变量我的名字
name = 'Zed A. Shaw'
# 定义变量我的年龄
age = 35  # not a lie
# 定义变量我的身高
height = 74  # inches
# 定义变量我的体重
weight = 180  # lbs
# 定义变量我眼睛的颜色
eyes = 'Blue'
# 定义变量我的牙齿颜色
teeth = 'White'
# 定义变量我头发的颜色
hair = 'Brown'

# 使用格式化字符串打印方式
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
# 使用变量名计算我的年龄、身高、体重的总和
total = age + height + weight
# 使用格式化字符串输出以上结果
print(f"If I add {age}, {height}, and {weight} I get {total}.")
