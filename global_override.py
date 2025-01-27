x = "easy"

def newfunc():
    global x
    x = "difficult"
    print("Python is : ",x)

newfunc()
print("Python is : ",x)

#since the value of x is beign override by the global value of x therefore the output will be "difficult"

#output :
# Python is :  difficult
#Python is :  difficult-