print("Welcome to the tip calculator!\n")
bill_amount= float(input("What was the total bill? $\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))
contribution = (((tip_percentage / 100) * bill_amount) + bill_amount) /no_of_people
print(f"Each person should pay: ${round(contribution, 2)}")