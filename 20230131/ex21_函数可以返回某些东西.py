# 定义加减乘除4个函数，通过函数返回值将计算结果返回
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")
# 将加减乘除的返回值分别赋予变量
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
# 调用函数进行混合运算，注意计算优先级
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = 35+(74-(180*25))

print("That becomes: ", what, "Can you do it by hand?")