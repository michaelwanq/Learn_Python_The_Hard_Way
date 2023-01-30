from sys import argv      # 从sys模块中导入argv函数
# “argv” 即 “argument value” 是一个列表对象。其中存储的是在命令行调用python脚本时提供的“命令行参数”。

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
