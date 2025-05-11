print("Welcome to Pizza Deliverable")

size = input("Choose Size S (Small), M (Medium), L (Large): ")
add_pepperoni = input("Add pepperoni? Y for Yes or N for No: ")
extra_cheese = input("Add extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")


      
