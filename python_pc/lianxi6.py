class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    
class Student(Person):
    def __init__(self,school,name,age):
        self.school=school
        super().__init__(name,age)
    def grade(self,n):
        print("{0}'s grade is {1}".format(self.name,str(n)))


stu1=Student('sccdhow',"Galileo",27)
stu1.grade(99)
print(stu1.get_name())
print(stu1.get_age())