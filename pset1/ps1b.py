annual_salary = float(input("Enter the annual salary: "))
portion_saved = float(input("Enter the portion saved, as a decimal: "))
monthly_salary = (annual_salary)/12.0
monthly_saved = portion_saved*monthly_salary

total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost

semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

current_savings = 0.0
r = 0.04/12
i=0

while current_savings < portion_down_payment :
    i += 1
    current_savings += current_savings*r + monthly_saved
    
    if i % 6 == 0 :
        monthly_salary = (monthly_salary)*(1+semi_annual_raise)
        monthly_saved = portion_saved*monthly_salary

print("number of months = ", i)
print("Total saved money = ", current_savings)