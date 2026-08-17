class student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def great(self):
        print(f"Hello, I am {self.name} Studying{self.course}. I am {self.age} years old")
    def is_adult(self):
        if self.age>=18:
            return True
           
        else:
            return False
            
student1 = student("Nadaara", 25,"AI Engineering")
student2 = student("Ali",16,"Computer science")

student1.great()
print(student1.is_adult())
student2.great()

print(student2.is_adult())