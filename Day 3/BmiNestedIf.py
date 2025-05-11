print("BMI")
Weight=float(input("enter your weight"))
Height=float(input("Enter your height"))
Bmi=Weight/Height**2

print(Bmi)

if Bmi<18.5:
    print("They are under weight")
elif Bmi<25:
    print("Normal weight")
elif Bmi<30:
    print("Slight weigt")
elif Bmi<35:
    print("Obese")
else:
    print("inlinical")