# Taking input from the user
n = int(input("Enter a number to find the sum of the first n natural numbers: "))

# Initializing the counter and sum
i = 1
sum_n = 0

# Calculating the sum using a while loop
while i <= n:
    sum_n += i
    i += 1

print("The sum of the first" , n , "natural numbers is : ",sum_n)  #result

