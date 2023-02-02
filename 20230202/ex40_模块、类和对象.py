# 定义一个类Song，有一个属性lyrics。再类中定义了一个方法sing_me_a_song，执行对属性lyrics列表中元素的打印操作
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#类song创建一个实例happy_bday
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
#使用类song再创建一个实例bulls_on_parade
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
#输出实例
print("输出实例happy_bday:")
happy_bday.sing_me_a_song()
print("输出实例bulls_on_parade:")
bulls_on_parade.sing_me_a_song()
