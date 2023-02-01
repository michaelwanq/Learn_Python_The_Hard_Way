# 导入ex25模块
import ex25

# 定义变量sentence
sentence = "All good things come to those who wait."
# 调用ex25模块中的break_words函数，传入实参sentence
words = ex25.break_words(sentence)
print(f"No1_words is {words}")
sorted_words = ex25.sort_words(words)
print(f"No2_sorted_words is {sorted_words}")
# print_first_word和print_last_word已经对保存在变量words中的数列进行了弹出元素的操作！
ex25.print_first_word(words)
ex25.print_last_word(words)
print(f"No3_now words is {words}")
# print_first_word和print_last_word已经对保存在变量sorted_words中的数列进行了弹出元素的操作！
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print(f'No4_now sorted_words is {sorted_words}')
# 对sentence进行排序处理，得到的结果重新给变量sorted_words赋值
sorted_words = ex25.sort_sentence(sentence)
print(f'No5_now sorted_words is {sorted_words}')
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
print(f'No6_now sorted_words is {sentence}')
