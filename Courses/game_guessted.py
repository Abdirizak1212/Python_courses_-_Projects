import random
secret = random.randint(1,200)
attempts = 0
print("Guess random numbers between 1 to 200")
while True:
    guess = int(input("Guess number:"))
    attempts+=1
    if guess>secret:
        print("Too high: try agian! ")
    elif guess<secret:
        print("Too low: try again!")
    else:
        print(f"Correct!\n {attempts} Attempts")
        break