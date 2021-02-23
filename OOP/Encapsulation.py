class zuper():
    
    def __init__(self):
        self.__maxprice=900


    def sell(self):
        print("We are selling at {}".format(self.__maxprice))

    def changemaxprice(self,newprice):
        self.__maxprice=newprice

q1=zuper()
q1.sell()
q1.__maxprice=1200
q1.changemaxprice(1200)
q1.sell()