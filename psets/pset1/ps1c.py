initial_deposit = float(input("Enter the initial deposit:"))
down_payment = 800000*0.25
epsilon = 100
low = 0
high = 10000
guess = (low+high)/2.0
number_guess = 0
amount_saved = 0

if initial_deposit >= (down_payment-100):
    print("Best savings rate:0.0")
    print(f"Steps in bisection search:{number_guess}")

elif initial_deposit*((1+1/12)**36) < (down_payment-100):
    print("Best savings rate : None")
    print("Steps in bisection search:0")
    
else:
    while abs(amount_saved-down_payment) >= epsilon:
        number_guess += 1
        guess = (low+high)/2.0
        r = guess/10000
        amount_saved = initial_deposit*((1+r/12)**36)
        if (amount_saved) > down_payment:
            high = guess
        else:
            low = guess
    print(f"Best savings rate:{r}")
    print(f"Steps in bisection search:{number_guess}")


    





    
