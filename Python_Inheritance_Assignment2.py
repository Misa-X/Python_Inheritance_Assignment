#Moderately Challenging

class Person:
    def __init__(self, name = "Misa", address = "London"):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __repr__(self):
        return {"name" : self.name, "address": self.address}

person1 = Person()
person2 = Person("Jhonaty", "Paris")
person3 = Person("Auman", "Malanga")
print(person1.__repr__())
print(person2.__repr__())
print(person3.__repr__())

class Student(Person):
    def __init__(self, numCourses = 3, courses = ["Intro to progarmming", "Web applications", "Operating systems"], grades = ["94", "75", "89"]) :
        super().__init__(self, address = "London")
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def __repr__(self):
        return {"numCourses" : self.numCourses, "courses" : self.courses, "grades" : self.grades}

    def addCourseGrade(self):
        course_grade = (self.courses + str(self.grades))
        print(course_grade)



    def printGrades(self):
        print(self.grades)


    def getAverageGrade(self):
        get_average = sum(self.grades) / len(self.grades)
        return get_average



    def __str__(self):
        super().__init__(self, name = "Misa", address = "London")
        return{"name" : self.name, "address": self.address}


student1 = Student()
student2 = Student(2, ["ICT", "Program design methods"], [80, 78])
print(student1.__repr__())
print(student2.__repr__())
print(student1.getAverageGrade())



class Teacher(Person):
    def __int__(self, numCourses = 3, courses = ["Intro to progarmming", "Web applications", "Operating systems"]):
        self.numCourses = numCourses
        self.courses = courses

    def __repr__(self):
        return {"numCourses":3, "courses":["Intro to progarmming", "Web applications", "Operating systems"] }

    def addCourse(self):
        if course in self.courses:
            print("false")

    def removeCourse(self):
        self.courses.pop("ICT")
        if ICT not in self.courses:
            print("false")

teacher1 = Teacher()
print(teacher1.__repr__())
print(teacher1.addCourse())
print(teacher1.removeCourse())


