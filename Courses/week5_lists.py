fruits=["apple","banana","mango","orange"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
fruits.append("grape")
print(fruits[4])
fruits.remove("banana")
fruits[0] ="waterlemon"
print(fruits[0])


print(fruits)
print(len(fruits))
for fruits in fruits:
    print(f"Fruit: {fruits}")

student = {
    "name": "nadaara",
    "age": "26",
    "city":"Mogadisho",
    "course": "AI engineeering"
}
print(student["name"])
print(student["age"])
student["Email"] = "nadaara@gmail.com"
print(student["Email"])
student["age"]=20
print(student["age"])
for key, value in student.items():
    print(f"{key}: {value}")
print(student)

def displsy_student(students):
    for key, value in students.items():
            print(f"{key }:  {value}")
         
students={
    "name": "Abdirizak",
    "age": "26",
    "course": "AI"
}
displsy_student(students)