# This program calculates the amount of tip to be paid and what share does each diner pay

no_of_people = int(input("How many people will share the bill: "))

net_bill = float(input("How much does the food cost total: EUR"))

tip_percentage = int(input("How many percent (%) tip are you willing to give: "))

total_bill = ((tip_percentage/100)+1) * net_bill

per_person_bill = round(total_bill / no_of_people,3)

print ("****** Thank you for dining with us ******")

print (f"Your total bill is EUR {total_bill} and each person would pay EUR {per_person_bill}")
