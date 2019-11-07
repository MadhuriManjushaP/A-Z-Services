height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
bmi=round(weight / (height * height), 2)
print(bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>18.5 and bmi<24.9:
    print("normal weight")
elif bmi>=25 and bmi<29.9:
    print("over weight")
elif bmi>=30 and bmi<40:
    print("obesity")
elif bmi>=40:
    print("Extreme obesity")