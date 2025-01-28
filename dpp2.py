# Taking input from the user
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

# Comparing the values
if a == b == c:
    print("Equal")
elif a >= b and a >= c:
    print("The biggest value is a") 
elif b >= a and b >= c:
    print("The biggest value is b")
else:
    print("The biggest value is c")