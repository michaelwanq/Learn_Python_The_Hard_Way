# 定义一个变量cars，赋值
cars = 100
# 定义一个变量，车内空间，浮点数类型
space_in_a_car = 4.0
# 定义变量drivers，司机
drivers = 30
# 定义变量passengers，乘客
passengers = 90
# 定义变量car_not_driven,有车没司机
car_not_driven = cars - drivers
# 定义变量car_driven，有司机
car_driven = drivers
# 定义变量carpool_capacity，定义车场容量
carpool_capacity = space_in_a_car * drivers
# 定义变量average_passengers_per_car，平均每车乘客数量
average_passengers_per_car = passengers / car_driven
# 打印总共有多少车辆
print("There are " + str(cars) + " available.")
# 打印有多少位司机
print("There are only " + str(drivers) +" available.")
# 打印有多少辆空车
print("There will be " + str(car_not_driven) +" empty cars today.")
# 打印可装载旅客量
print("We can transport " + str(carpool_capacity) +" people today.")
# 打印我们今天能载多少旅客
print("We have " + str(passengers) + " to carpool today.")
# 打印平均每车
print("We nded to put about " + str(average_passengers_per_car) +" in each car.")