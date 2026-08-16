def calculate_bmi(weight, height):
    return weight/height**2
result = calculate_bmi(70, 1.75)
print(f"Total of BMI = {result: .2f} Kg/m!")

import random

def get_secret_number():
    return random.randint(1, 200)

def get_guess():
    return int(input("Guess number: "))

def check_guess(guess, secret):
    if guess > secret:
        print("Too high! Try again.")
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Correct!")
        return True
    return False

def play_game():
    secret = get_secret_number()
    attempts = 0
    print("Guess a number between 1 and 200")
    
    while True:
        guess = get_guess()
        attempts += 1
        if check_guess(guess, secret):
            print(f"You got it in {attempts} attempts!")
            break

play_game()