yearly_salary = int(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
cost_of_dream_home = int(input("Enter the cost of your dream home: "))
portion_down_payment = cost_of_dream_home * 0.25
amount_saved = 0

r = 0.05
monthly_contribution = (yearly_salary*portion_saved)/12
months = 0

while amount_saved < portion_down_payment :
    amount_saved += monthly_contribution + (amount_saved * (r/12))
    months += 1
    if amount_saved >= portion_down_payment:
        print(f"Number of months: {months}")
        break
    




