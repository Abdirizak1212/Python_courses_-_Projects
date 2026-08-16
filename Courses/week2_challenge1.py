def calculate_bmi(weight, height):
    return weight/height**2
result = calculate_bmi(70, 1.75)
print(f"Total of BMI = {result: .2f} Kg/m!")