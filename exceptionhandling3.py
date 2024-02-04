result=None
x=int(input("Number 1:"))
y=int(input("Number 2:"))

try:                                 
    result=x/y                       
except TypeError as e:                #here we have called only one type of error. so, 50/0 zero division error is not recognised by it
    print("Inside type error")        #it only recognises string/string error
except ZeroDivisionError as e:
    print("Inside zero division error")  
            
    
print("Result =",result)