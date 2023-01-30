from sys import argv    # 从sys模块中导入argv函数
# “argv” 即 “argument value” 是一个列表对象。其中存储的是在命令行调用python脚本时提供的“命令行参数”。

#sys.argv可以用来获取命令行参数，其中sys.argv[0]为脚本名，即python文件名，列表中的其他值为传入的参数值，
# 一般定义方式为:script, arg1, arg2, arg3 = argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 采用写入方式打开用户输入的文件，将文件对象赋值给变量。特别注意，是将对象赋值给target，不是文件中的内容！
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
# 对文件对象采用truncate方法，truncate方法作用是清空文件对象的内容。
target.truncate()

print("Now I'm going to ask you for three lines.")

# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")
#
# print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

i = 1
while True:
    linei = input("line i: ")
    if linei == 'quit':
        break
    else:
        target.write(linei + '\n')
        #target.write('\n')
        i += 1

print("And finally, we close it.")
target.close()
