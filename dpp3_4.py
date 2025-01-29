# Taking input from the user
num = int(input("Enter a number to reverse : "))

# Initializing the reversed number
reversed_num = 0

# Reversing the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Printing the reversed number
print("The reversed number is : ",reversed_num)


