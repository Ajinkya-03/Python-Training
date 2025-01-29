# Taking input from the user
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

current = start
# Printing even numbers between start and end

while current <= end:
    if current % 2 == 0:
        print(current) 
    current += 1

    