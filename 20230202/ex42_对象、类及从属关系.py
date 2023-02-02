## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## 定义animal类的一个子类dog,同时初始了子类Dog的属性name
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## 定义animal类的一个子类Cat,同时初始了子类Cat的属性name
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## 定义Person类，并初始化了属性name和pet
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind

        self.pet = None


## 定义Person类的一个子类Employee，从Person类继承了属性name，并初始化了属性salary
class Employee(Person):

    def __init__(self, name, salary):
        ## 从父类Person继承了属性name
        super(Employee, self).__init__(name)
        ## 初始化子类Employee属性salary
        self.salary = salary


## 定义fish类
class Fish(object):
    pass


## 定义fish类的子类Salmon
class Salmon(Fish):
    pass


## 定义fish类的子类Halibut
class Halibut(Fish):
    pass


## 使用Dog类创建了一个实体rover
rover = Dog("Rover")
print(rover.name)

## 使用Cat类创建了一个实体satan
satan = Cat("Satan")

## 使用Person类创建了一个实体mary
mary = Person("Mary")

## 给实例mary的属性pet赋值satan
mary.pet = satan

## 使用Employee类创建实例，初始化属性name和salary
frank = Employee("Frank", 120000)
print(frank.salary)

## 将实例rover赋值给frank属性pet
frank.pet = rover

## 使用Fish类创建了一个实例flipper
flipper = Fish()

## 使用Salmon类创建实例crouse
crouse = Salmon()

## 使用Halibut类创建实例harry
harry = Halibut()
