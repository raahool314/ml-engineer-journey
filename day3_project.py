"""
Claude:
Ask the user for their name, weight (kg), and height (cm). Calculate their BMI and print a result card:
==============================
         BMI RESULT
==============================
Name   : Rahul
Weight : 75 kg
Height : 175 cm
BMI    : 24.49
Status : Normal weight
==============================
BMI formula: weight / (height_in_metres ** 2)
Status rules:
BMI < 18.5          → Underweight
18.5 ≤ BMI < 25     → Normal weight
25 ≤ BMI < 30       → Overweight
BMI ≥ 30            → Obese

Round BMI to 2 decimal places using round(bmi, 2).
"""

name = input("Enter your name: ")
weight = input("Enter your weight in kg: ")
height = input("Enter your height in cm: ")

bmi = round(float(weight) / ((float(height)/100) ** 2),2)
status = None
if bmi<18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal weight"
elif 25<= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("=" * 32)
print("         BMI RESULT")
print("=" * 32)
print(f"Name   : {name}")
print(f"Weight : {weight} kg")
print(f"Height : {height} cm")
print(f"BMI    : {bmi}")
print(f"Status : {status}")
print("=" * 32)