# Use a class and functions to allow a teacher to enter 4 marks, 
# get the total, the average and grade that average.
# Teacher should use input function to enter the marks, not hard coded ones

class Marks:

    def __init__(self, studentName, mark1, mark2, mark3, mark4):
        self.studentName = studentName
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        print("Marks collected")

    def totalMarks(self):
        total_marks = self.mark1 + self.mark2 + self.mark3 + self.mark4
        print(f"The total marks for {self.studentName}: {total_marks}")
        return total_marks

    def average(self):
        total = self.totalMarks()
        average_marks = total / 4
        print(f"Average marks: {average_marks}")
        return average_marks

    def grade(self):
        average = self.average()
        if (75< average < 100) or average == 100:
            print(f"Graded Mark: A")
        elif (65<average<74):
            print(f"Graded Mark: B")
        elif (50<average<64):
            print(f"Graded Mark: C")
        elif (30<average<49):
            print(f"Graded Mark: D")
        elif (average < 30):
            print(f"Graded Mark: E")


data = input("Enter student name and 4 marks separated by commas (e.g., Tavonga,73,63,89,53): ")
name, m1, m2, m3, m4 = data.split(",")
teacher = Marks(name, int(m1), int(m2), int(m3), int(m4))
teacher.totalMarks()
teacher.average()
teacher.grade()
