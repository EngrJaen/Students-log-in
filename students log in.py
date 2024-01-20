
class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section 

    def introduce(self):
        print ("    Name     : " + self.name)
        print ("    Course   : " + self.course)
        print ("    Year     : " + self.year)
        print ("    Section  : " + self.section)

listofStudent = []

while True:
    print()
    name = input("Name    : ")
    course = input("Course    : ")
    year = input("Year    : ")
    section = input("Section    : ")
    s = Student(name,course,year,section)
    listofStudent.append(s)
    print()
    choice =input("Create Another Student? [Y/Any Char] :")
    if choice == 'Y' or choice == 'y': pass
    else: break

i = 1
for student in listofStudent:
    print()
    print("Student #" + str(i))
    student.introduce()
    i = 1 + 1

        