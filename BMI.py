#Code that Interprets the BMI with weight and height
height = float(input())
weight = int(input())

# formular for BMI
BMI = weight / (height * height)

#nested if and elif statements
if BMI < 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif BMI < 25:
  print(f"Your BMI is {bmi}, you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight")
elif BMI < 35:
  print(f"Your BMI is {bmi}, you are clinically obese")