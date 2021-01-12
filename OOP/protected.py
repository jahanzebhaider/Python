class shape:
    def __init__(self,length,breath):
        self._length=length
        self._breath=breath

    def displaysize(self):

        print("Length:",self._length)
        print("Breath:",self._breath)


class rectangle(shape):

    def __init__(self, length, breath):
        # calling the constructor of supper class
        shape.__init__(self,length, breath)

    def calarea(self):
        print("Area is :",self._length*self._breath)


obj=rectangle(80,50)
obj.displaysize()
obj.calarea()
    