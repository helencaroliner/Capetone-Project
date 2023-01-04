import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calcute the amount you'll have to pay on a home loan")

finance_type = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
# A variable finance type was created to give the correct output for user.

#A cascaded if statement evaluates a series of conditions until one of them tests True. 
# When Python comes across a True condition, it executes its accompanying code. Then the cascaded if statement ends.
if finance_type == 'investment':
    amount = int(input("Please, enter the deposit amount: "))
    rate = int(input("Enter the actual interest rate: "))
# Defined that value of rate is the user input by divided by 100.
    rate_input = float(rate / 100)
    time = int(input("For how many years you plan to invest? "))

    interest = input("Would you like simple or compound interest? ")
    if interest == 'simple':
        total_simple = math.ceil(amount * (1 + (rate_input * time))) #math.ceil function rounds up the decimal float result, making readability easier for user.
        print (f"After {time} years investing, you will get back the total of £{total_simple} at a rate of {rate}%. ")
#The math.pow() method returns the value of x raised to power y.
    else:
        interest == 'compound'
        total_compound = math.ceil(amount * math.pow ((1 + rate_input), time))
        print (f"After {time} years investing, you will get back the total of £{total_compound} at a rate of {rate}%. ")

elif finance_type == 'bond':
    house_value = float(input("Please, enter the value of the house. e.g.: 100000: "))
    interest_rate = float(input("Enter the current interest rate: "))
# Defined that value of rate is the user input divided by 100 before diving by 12 (12 represents the annual interest rate).
    int_rate_input = float((interest_rate / 100) /12)
    time_to_pay = float(input("In how many months do you plan to repay the bond? "))
# Used math.ceil to round up result for variable 'repayment', making easier for user to read.
    repayment = math.ceil(float(int_rate_input * house_value) / (1 - (1 + int_rate_input) ** (-time_to_pay)))
    print(f"You will have to repay each month the total amount of £{repayment}.")

else:
    print (" You have entenred an invalid option. Please enter either 'investment' or 'bond' from the menu above to proceed: ")

