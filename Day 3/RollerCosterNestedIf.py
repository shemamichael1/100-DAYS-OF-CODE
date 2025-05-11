print("Enter Value")
Height=int(input("enter your Height"))
Bill=0
if Height>=100:
    print("You Can Ride")
    age=int(input("enter your age"))
    if age <12:
        Bill=5
        print("you will pay 5")
    elif age<=18:
        Bill=7
        print("yoy will pay 7")
    else:
        print("you will pay 12")
        Bill=12
        Want_Photo=input("Do you want photo taken type Y for Yes or N for No")
    if Want_Photo =="Y":
        Bill+=3
        print(f"Total bill will be{Bill}")
            
else:
    print("you need to be taller")
