# 打印名字
my_name = "Zed A. Shaw"
# 我的年龄
my_age = 35 # not a lie
# 我的身高
my_height = 74 # inches
# 我的体重
my_weight = 180 # lbs
# 我的眼睛
my_eyes = "Blue"
# 我的牙齿
my_teeth = "White"
# 我的头发
my_hair = "Brown"

print("Let's talk about %s." %my_name)
print("He's %d inches tall." %my_height)
print("He's %d pound heavy." %my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee." %my_teeth)

# this line is tricky,try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight,my_age + my_height+my_weight))

