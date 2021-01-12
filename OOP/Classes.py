# Simple class to print age and name passing value throgh constructor
class ali():
    Name=None
    Age=None
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    
    def display(self):
        print("My name is :{0} my age is {1}".format(self.Name,self.Age))
        print("My name is :"+ str(self.Name.title()) + "I am "+str(self.Age))

q1=ali('jahanzeb',20)
q1.display()

# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user
class user():
    def __init__(mot,fname,lname,school,country):
        mot.fname=fname
        mot.lname=lname
        mot.country=country 
        mot.school=school
    def def_user(mot):
        print("My first name :{0} last name :{1} i live in {2} i have done my schooling from {3}".format(mot.fname,mot.lname,mot.school,mot.country))
    
    def des_user(mot):
        print("Hello MR {} {} ".format(mot.fname.title(),mot.lname.title()))

q1 = user('jahanzeb','haider','st patricks','Pakistan')
q1.def_user()
q1.des_user()

