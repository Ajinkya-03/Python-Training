# Taking input from the user
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Printing even numbers between start and end
print(f"Even numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num) 