result=None
x=int(input("Number 1:"))
y=int(input("Number 2:"))

try:                                 #try:{Run this code}; except:{Executet this code when there is an exception}
    result=x/y                       
except Exception as e:               # with except we can use base Exception class to print out the reason
    print("Error with our code : ",e)
    print(type(e))                   #prints class of error
    
print("Result =",result)