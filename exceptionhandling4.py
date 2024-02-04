result=None
x=int(input("Number 1:"))
y=int(input("Number 2:"))

try:                                 #try:{Run this code}
    result=x/y                       #except:{Run this code when there is an exception}                
except Exception as e:               #else:{No exceptions? Run this code}
    print(e)                         #finally:{Always run this code}
else:
    print("Inside Else")
finally:
    print("Inside Finally")
            
    
print("Result =",result)