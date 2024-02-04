class Tea:
    def __init__(self,temperature):
        self.__temperature=temperature

    def drink_tea(self):
        if self.__temperature>85:
            print("Hot to drink")
        elif self.__temperature<65 and self.__temperature>=0:
            print("Cold to drink")
        elif self.__temperature<0: 
            raise Exception("Tea too cold")                  #we can raise exception whereever or whenever we like
        else:                                                #instead of writing Exception we can write VaueError or any other bult in exception
            print("Tea OK to drink")

cup=Tea(-2)
cup.drink_tea()
        