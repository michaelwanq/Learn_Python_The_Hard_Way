# 定义3个列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 使用for循环分别打印3个列表中的元素
# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# 定义一个空列表
# we can also build lists, first start with an empty one
elements = []

将0-5依次插入列表elements中
then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
# elements = range(0,6)

# 使用循环打印elements中的元素
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")