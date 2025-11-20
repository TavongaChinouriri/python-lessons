# defining list of strings
list1 = ["geeksforgeeks", "C++",
         "Java", "Python", "C", "MachineLearning"]

print("Printing list items using do while loop")
size = len(list1)
print(list1)
print (size)

i = 0

# Implement do while loop to print list items
while(True):
    print(list1[i] + " " + str(i))
    i = i+1
    if(i < size and len(list1[i]) < 10):
        continue
    else:
        break