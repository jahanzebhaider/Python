# public class 
class publicclass():
    def __init__(self,name,location,email):
        self.name=name
        self.location=location
        self.email=email
        print("{},{},{}".format(name,location,email))
    
    # def display(delf):
        # print("{},{},{}".format(delf.name,delf.location,delf.email))


q1=publicclass('jahanzeb','karachi','aliheider45@gmail.com')
q1.email="cs1812342"
# q1.display()
#accesing email outsite the classs
print(q1.email)
print(type(publicclass))