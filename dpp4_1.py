# Taking input from the user
n = int(input("Enter the number of elements you want to add to the list : "))

# Initializing the list
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("")
print("The numbers in list are : ",numbers)

# Finding the maximum and minimum numbers in the list
max_num = max(numbers)
min_num = min(numbers)
print("")
print("The maximum number in the list is : ", max_num)
print("The minimum number in the list is : ", min_num)