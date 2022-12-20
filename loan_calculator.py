import math
from math import ceil

principal_loan = float(input("Enter the loan principal:\n>"))
print("What do you want to calculate?")
print(' - type "m" for number of monthly payments,')
print(' - type "p" for the monthly payment:')
calculated_parameter = input('>')
if calculated_parameter == 'm':
    monthly_payment = float(input("Enter the monthly payment:\n>"))
    payments_number = math.ceil(principal_loan / monthly_payment)

    if payments_number == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {payments_number} months to repay the loan\n")
        calcule_test = monthly_payment * payments_number
        if principal_loan != calcule_test:
            payments_number = payments_number - 1
            rest_loan = float(principal_loan - (monthly_payment * payments_number))
            print(f"the month number {payments_number + 1} will be {rest_loan} \nyou can pay it separately")
            print("or you can choose a month to add it to ")
            client_decision = input('what do you want \n - type "s" for separately \n - type "a" to add to a month \n>')
            if client_decision == 's':
                print("here's your monthly payment list :")
                for month in range(payments_number):
                    print(f"month number {month + 1} : {monthly_payment}")
                print(f"month number {payments_number + 1} : {rest_loan}")
            elif client_decision == 'a':
                which_month = int(input(f"which month you want to add it to\nchoose a number between 1 nad {payments_number}\n>"))
                print("here's your monthly payment list :")
                for month in range(payments_number):
                    if which_month != (month + 1):
                        print(f"month number {month + 1} : {monthly_payment}")
                    else:
                        adding_month = month + 1
                        print(f"month number {adding_month} : {monthly_payment + rest_loan}")
elif calculated_parameter == 'p':
    payments_number = int(input("Enter the number of months:\n>"))
    monthly_payment = float(math.ceil(principal_loan / payments_number))
    last_payment = float(principal_loan - ((payments_number - 1)*monthly_payment))
    print(f"your monthly payment will be : {monthly_payment} during {payments_number} month/s")
    rest_loan = monthly_payment - last_payment
    print(f"and the rest payment will be : {rest_loan} \nyou can pay it separately")
    print("or you can choose a month to add it to ")
    client_decision = input('what do you want \n - type "s" for separately \n - type "a" to add to a month \n>')
    if client_decision == 's':
        print("here's your monthly payment list :")
        for month in range(payments_number):
            print(f"Month number {month + 1} : {monthly_payment}")
        print(f"month number {payments_number + 1} : {rest_loan}")
    elif client_decision == 'a':
        which_month = int(input(f"which month you want to add it to\nchoose a number between 1 nad {payments_number}\n>"))
        print("here's your monthly payment list :")
        for month in range(payments_number):
            if which_month != (month + 1):
                print(f"Month number {month + 1} : {monthly_payment}")
            else:
                adding_month = month + 1
                print(f"month number {adding_month} : {monthly_payment + rest_loan}")
else:
    print('only "m" or "p" are allowed!')
