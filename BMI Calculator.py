print("this program is to calculate the BMI of an individal\n:")
name=input("enter your name:")
weight=float(input("enter your weight: "))
height=float(input("enter your height in meters:"))
bmi=weight / (height ** 2)
if(bmi<25):
    print(f"{name} is underweight by calculated {bmi} BMI")
else:
    print(f"{name} is overweight by calculated {bmi} BMI")