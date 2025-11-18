sum = 0 
n=4
for i in range(0, n):
    mark = int(input('Enter mark: '))
    sum = sum + mark
average = sum/(n)
print("The average of marks entered is: " + str(average))

