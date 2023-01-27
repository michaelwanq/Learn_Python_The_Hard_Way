# 定义车辆数量并赋值
cars = 100
# 定义车辆可搭载的旅客数量并赋值
# space_in_a_car = 4.0
space_in_a_car = 4
# 定义司机数量并赋值
drivers = 30
# 定义旅客人数并赋值
passengers = 90
# 定义没有驾驶员的车辆数量
cars_not_driven = cars - drivers
# 定义有驾驶员的车辆数量
cars_driven = drivers
# 定义车辆能装载的旅客人数
carpool_capacity = cars_driven * space_in_a_car
# 定义每车平均旅客人数
average_passengers_per_car = passengers / cars_driven

# 打印有多少辆可用的车辆
print("There are", cars, "cars available.")
# 打印驾驶员人数
print("There are only", drivers, "drivers available.")
# 打印没有驾驶员的汽车数量
print("There will be", cars_not_driven, "empty cars today.")
# 打印可运送的旅客人数
print("We can transport", carpool_capacity, "people today.")
# 打印今天共有多少乘客
print("We have", passengers, "to carpool today.")
# 打印需要今天每车平均运送的旅客人数
print("We need to put about", average_passengers_per_car, "in each car.")