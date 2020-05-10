annual_salary = float(input("Enter the annual salary: "))
portion_saved = float(input("Enter the portion saved, as a decimal: "))
monthly_salary = (annual_salary)/12
monthly_saved = portion_saved*monthly_salary

total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost

current_savings = 0.0
r = 0.04/12
i=0

while current_savings < portion_down_payment :
    current_savings += current_savings*r + monthly_saved
    i += 1
print("number of months = ", i)
print("Total saved money = ", current_savings)