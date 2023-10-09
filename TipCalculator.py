#if the Bill was like 100 bucks, split between 5 people, with 10% tip for example
print("Tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split the bill?"))
#bill_with_tip = tip / 100 * bill + bill
# other solution would be bill * (1+tip/100)
#print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bil + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
