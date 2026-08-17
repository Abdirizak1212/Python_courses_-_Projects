# Without error handling — crashes if user types text
# num = int(input("Enter a number: "))  # try typing "hello" — it crashes

# WITH error handling
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 divided by {num} = {result}")

except ValueError:
    print("Error: Please enter a valid number, not text.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Program finished.")