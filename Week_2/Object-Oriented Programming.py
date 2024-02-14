# The blueprint for creating students
class Student:
    def __init__(self, name, gender, student_ID, subject):
        self.name = name
        self.gender = gender
        self.student_ID = student_ID
        self.subject = subject

    def submission(self, score):
        self.grade = score
        print(f"Grade Book has been updated - current Grade: {self.grade}")

    def attendance(self, attendance):
        self.register = attendance
        print(f"Attendance Percentage: {self.register}%")


    # This method should be indented to be inside the class
    def introduce(self):
        print(f"Hi, my name is {self.name} and I study {self.subject}.")

# Creating an object of the Student class
Aaron = Student('Aaron', 'Male', '123456', 'Software Engineering')



# Final Step
Aaron.introduce()
Aaron.submission(97)
Aaron.attendance(50)