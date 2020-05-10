annual_salary = float(input("Enter the annual salary: "))
months = 36
monthly_salary = (annual_salary)/12.0

total_cost = 1000000
current_savings = 0.25*total_cost
current_savings_guessed = 0.0

semi_annual_raise = 0.07

r = 0.04/12
found = False
low = 0
high = 10000
epsilon = 1
guess = (low + high)/2.0
steps = 0
max1 = 0
monthly_saved1 = monthly_salary

for i in range (6,months + 1,6) :
    max1 += max1*r + 6 * monthly_saved1
    monthly_saved1 += monthly_saved1 * semi_annual_raise

if (max1 < current_savings) :
    found = False
else :
    found = True
    current_savings_guessed = 0.0
    monthly_saved = (guess/10000) * monthly_salary
    for i in range (6,months + 1,6) :
        current_savings_guessed += current_savings_guessed*r + 6 * monthly_saved
        monthly_saved += monthly_saved * semi_annual_raise
    
    while abs(current_savings_guessed - current_savings) >= 100 :
        steps += 1
        if current_savings_guessed < current_savings :
            low = guess
        else :
            high = guess
        guess = (low + high)/2
        monthly_saved = (guess/10000) * monthly_salary
        current_savings_guessed = 0.0
        for i in range (6,months + 1,6) :
            current_savings_guessed += current_savings_guessed*r + 6 * monthly_saved
            monthly_saved += monthly_saved * semi_annual_raise
    
if found :
    portion_saved = guess
    print("portion saved = ", (portion_saved)/10000)
    print("bisection steps = ", steps)
else :
    print("Is is not possible to pay the down payment in three years")