import sys

try:
    x=int(input("x: "))
    y=int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)

    
try:
    result=x/y
except ZeroDivisionError:
    print("Error:Cannot divide by 0.")
    sys.exit(1)        #exit the program with a status code of one, where a statuse code of one generally means something gone wrong in this program.(for this you need to import the module sys)

print(f"{x} / {y} = {result}")
