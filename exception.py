x = input("Enter first number : ")
y = input("Enter second number : ")
try:                                    #exception handling
    z = int(x)/int(y)
except Exception as e:                  
    print("Exception occured: ",e)
    z = None
# except ZeroDivisionError as e:                  
#     print("Zero Devision Exception occured")
#     z = None
print("Division is: ",z)