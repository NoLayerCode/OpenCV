n = int(input())

# Initialize the first number of each row to be printed
num = 7

# Loop through each row
for i in range(n):
    # Initialize the first number of the current row
    curr_num = num
    
    # Loop through each column of the current row
    for j in range(i+1):
        # Print the current number and update it for the next column
        print(curr_num, end=" ")
        curr_num += 1
    
    # Update the first number of the next row
    num -= (i+1)*2
    
    # Move to the next row
    print()
