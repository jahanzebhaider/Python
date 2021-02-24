# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
# print(peggy.whoisThis())
Bird.whoisThis(peggy)



#Multiple inheritance
class ali1():
    def m(self):
        print('in class 1')

class ali2(ali1):
    def m(self):
        print('in class 2')

class ali3(ali1):
    def m(self):
        print('in class 3')

class ali4(ali2,ali3):
    def m(self):
        print('in class 4')
q1=ali4()
q1.m()


#mETHOD RESOLUTION ORDER

class a():
    def display(self):
        print('In class A')

class b():
    def display(self):
        print('In class B')

class Demo(a,b):
    def demo(self):
        print('in demo')

q1=Demo()
q1.display()