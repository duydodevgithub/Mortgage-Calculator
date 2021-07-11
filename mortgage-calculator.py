#mortgage calculator        

home_value = float(input("What is your home value?: "))
down_payment = float(input("What is your down payment?: "))
interest = float(input("What is your interest rate?: "))
duration = int(input("How long do you take the loan (in year)?: "))

loan_amount = (home_value) - (down_payment)
first_month_interest_paid = (loan_amount) * (interest) / 1200
monthly_principle = (loan_amount) / (12 * (duration))
total_interest = (first_month_interest_paid)

for i in range(1, int(duration) + 1):
    current_month_interest_paid = 0
    remaining = loan_amount - (current_month_interest_paid - monthly_principle * i)
    current_month_interest_paid = remaining * ((interest) / 1200)
    total_interest += current_month_interest_paid
    

print("Your monthly payment is: " + str(monthly_principle + (total_interest / ((duration) * 12))))