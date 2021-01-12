# defining private classs
class private():

    # private altributes
    __Name=None
    __location=None
    __email=None

    def __init__(self, name,location,email):
        self.__Name=name
        self.__location=location
        self.__email=email
    
    # private function
    def __displayprivmembers(self):
        print("Name:{}\n Location:{} \n Email:".format(self.__Name,self.__location,self.__email))
     #accesing private function by defining it inside the public function
    def accesprivfunction(self):
        self.__displayprivmembers()

# passing value to the constructor
q1=private('jahanzeb','kaeachi','aliheider45')

# printying privare altribute name value (object._class__variable)
print(q1._private__Name)
q1._private__displayprivmembers()
# acessing throgh public function
q1.accesprivfunction()
# q1.__displayprivmembers()

