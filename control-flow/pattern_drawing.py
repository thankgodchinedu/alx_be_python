#prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Loop to print each row of the pattern
while row < size:
    # Use a for loop to print asterisks in each row
    for i in range(size):
        print("*", end="")
    
    # Move to the next line after each row
    print()
    
    # Increase the row counter
    row += 1