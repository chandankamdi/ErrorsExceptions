class TeaHotException(Exception):
    def __init__(self,arg):
        self.arg=arg
class TeaColdException(Exception):
    def __init__(self,arg):
        self.arg=arg

class Tea:
    def __init__(self,temperature):
        self.__temperature=temperature

    def drink_tea(self):
        if self.__temperature>85:
            raise TeaHotException("Hot to drink")
        elif self.__temperature<65:
            raise TeaColdException("Cold to drink")              
        else:
            print("Tea OK to drink")

cup=Tea(100)
cup.drink_tea()