# Create a program that add allows teacher to enter student name and 4 marks only(out of 100). 
# The program must grade each mark, calculate the total of these marks and then the average.
# Store the name and marks in a list, use the if statement, the while or do while loop
number_of_marks = 0
student_name = str(input("Enter student name")) 
total = 0
list=[student_name]
while(True) :
    mark = int(input("Enter mark "))
    list.append(mark)
    total += mark 
    number_of_marks = number_of_marks + 1
    if(number_of_marks < 4 and mark < 101):
        continue
    else:
        break
average = total/400
print("Total is " + str(total) + "\nAverage is " + str(average))
print(list)
      