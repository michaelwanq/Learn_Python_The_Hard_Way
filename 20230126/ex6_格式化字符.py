# 定义变量人的类型并赋值
types_of_people = 10
# 给变量X赋值，赋值中包含格式化字符
x = f"There are {types_of_people} types of people."

# 定义变量binary并赋值
binary = "binary"
# 定义变量do_not并赋值
do_not = "don't"
# 给变量Y赋值，赋值中包含格式化字符
y = f"Those who know {binary} and those who {do_not}."

# 打印变量X、y
print(x)
print(y)

# 打印包含格式化字符的句子
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 定义变量hilarious并赋值
hilarious = False
# 定义变量joke_evaluation并赋值
joke_evaluation = "Isn't that joke so funny?! {}"

# 打印包含格式化字符的句子，格式化字符使用变量传入
print(joke_evaluation.format(hilarious))

# 打印句子
w = "This is the left side of..."
e = "a string with a right side."
# 将变量W和e合并字符串，然后输出。
print(w + " " + e)
