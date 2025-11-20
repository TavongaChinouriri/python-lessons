total = 0
# loop will run at least once
while True:
    # ask the user to enter a number
    num = int(input("Enter a number (or 0 to exit): "))

    # exit the loop if the user enters 0
    if num == 0:
        break
    total += num

# print the total
print("Total:", total)