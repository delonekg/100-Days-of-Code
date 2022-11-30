print("Welcome to the tip calculator!")

bill = float(input("What is the total bill?: $"))
tip_percent = float(input("What percentage would you like to tip? 12%, 15%, 25%: "))/100
people_to_split = int(input("How many people are splitting the bill?: "))
tip_amount = bill * tip_percent
individual_amount = round((bill + tip_amount) / people_to_split, 2)

print(f"Each person has to pay: ${individual_amount}.")
