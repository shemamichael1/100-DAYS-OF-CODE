print("Leap Year")

Year=int(input("enter year"))

if Year%4==0:
   if Year%100==0:
    if Year%400==0:
        print("Leap year")
    else:
         print("Not leap year")

   else:
          print("leap Year")
else:
    print("not leap year")