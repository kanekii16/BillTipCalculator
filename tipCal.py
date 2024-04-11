print("Welcome To Tip Calculator ")

tot_bill = float(input("What was Total Bill ? $"))

per_tip = int(input("How much tip would you like to give ? 10 /12 / 15 ? "))

people = int(input("How many people to split the  Bill ? "))


per_tip = round((per_tip / 100) + 1 , 2)

bill = (tot_bill * per_tip) / people

bill = "{:.2f}".format(bill)

print(f"Each Person Should pay : ${bill}")


