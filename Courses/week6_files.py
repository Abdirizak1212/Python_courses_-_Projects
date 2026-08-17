with open ("students.txt","w") as file:
    file.write("Nadaara\n")
    file.write("Ali \n")
    file.write("Faadumo\n")
print("file written. ")

with open("students.txt","r") as file:
    content = file.read()
    print(content)
    with open("New_students.txt","w") as file:
        file.write(" Abdirizak\n")
        file.write("Abdi\n")
        file.write("Omar\n")
with open("new_students.txt","a") as file:
    file.write("Geedi\n")
with open("new_students.txt","r") as file:
    content1 = file.read()
    print(content1)
with open("new_students.txt","r") as file:
    for line in file:
        print(f"student: {line.strip()}")


 



 