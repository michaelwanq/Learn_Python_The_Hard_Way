from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# 使用open函数读取文件，将文件作为操作对象赋值给变量in_file
in_file = open(from_file)
#对对象in_file使用read()读操作，读取的内容赋值给变量indata
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 使用open()打开to_file，采用写入方式操作
out_file = open(to_file, 'w')
# 对out_file对象进行写入操作，写入内容为从from_file读取的内容
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# 方法二、省略文件读写对象赋值给变量，直接针对对象进行方法的处理
# open(to_file, 'w').write(open(from_file))
