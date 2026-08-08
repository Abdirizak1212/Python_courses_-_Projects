age = int(input(" enter your age"))
has_ID = input("Do You have an ID? (Yes/No): ").lower()

if age >= 18 and has_ID == "yes":
    print("Access granted")
elif age >= 18 and has_ID == "no":
    print("You need an ID")
else:
    print("Access denied")