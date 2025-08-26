#functions example based on while_atm.py
balance = 500


def main():
    repeat = "yes"
    while repeat == "yes":
        action = input("Would you like to deposit or withdraw:").lower()

        while (action != "deposit" and action != "withdraw"):
            action = input("Please enter 'deposit' or 'withdraw': ").lower()

        currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()

        while (currency != "USD" and currency != "EUR" and currency != "CAD"):
            currency = input("The currency is not valid. Please enter USD, EUR, or CAD: ").upper()

        amount = int(input("Please enter an amount:"))
        while (amount <=0):
            amount = int(input("The amount you entered is not valid. Please re-enter the amount: "))

        if action == "withdraw":
           # call the witdraw function
           if withdraw(currency, amount) == False:
               print("Insufficient funds!")
        elif action.lower() == "deposit":
           # call the deposit function
           deposit(currency,amount)
        else:
            print("Please enter 'deposit' or 'withdraw'")
            
        print("Your balance is: ", balance)
        repeat = input("Would you like to continue? yes or no: ")

    print("Goodbye!")

def withdraw(c, a):
    global balance
    amount_in_usd = convert(c,a)
    if amount_in_usd > balance:
        return False
    else:
        balance = balance - amount_in_usd
        return True
    

def deposit(c, a):
    global balance
    amount_in_usd = convert(c, a)
    balance = balance + amount_in_usd

def convert(c, a):
    if (c == "USD"):
        return a
    elif (c == "EUR"):
        a = a/0.86
        return int(a)
    elif (c == "CAD"):
        a = a/1.3
        return int(a)

main()
        

