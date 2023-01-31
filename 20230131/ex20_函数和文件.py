# 从模块sys导入argv函数
from sys import argv

# 定义argv函数的输入参数
script, input_file = argv

#定义函数print_all，打印读取文件的全部内容
def print_all(f):
    print(f.read())

# 使用seek（0）方法，将文件指针指向文件头位置
def rewind(f):
    f.seek(0)

# 使用readline方法对文件逐行读取，每次读取一行
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

for i in range(1,4):
    current_line = i
    print_a_line(current_line, current_file)
    i += 1
