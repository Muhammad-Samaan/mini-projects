## Input needed 
# Rent amount
# Food 
# Chai 
# Petrol 
# Electricity
# people 

## output
#display the total rent and the amount each person has to pay

rent_amount = int(input("Enter the rent amount: "))
food_amount = int(input("Enter the food amount: "))
chai_amount = int(input("Enter the chai amount: "))
petrol_amount = int(input("Enter the petrol amount: "))
electricity_amount = int(input("Enter the electricity amount: "))
people = int(input("Enter the number of people: "))
#Total expenses formula 
total_expenses = rent_amount + food_amount + chai_amount + petrol_amount + electricity_amount
amount_per_person = total_expenses / people
#prininting the values 
print(f"Total expenses: {total_expenses}")
print(f"Amount each person has to pay: {amount_per_person}")
