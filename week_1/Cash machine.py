# Initial pin number and balance
pin_number = int(1234)
balance = float(100)

def check_pin(input_pin: int):
    global pin_number
    if(pin_number != input_pin):
        print("Incorrect Pin")
        return False
    else:
        print("Correct Pin")
        return True

def withdraw_cash(amount: float):
    global balance
    if(amount > balance):
        print("Insufficient Funds")
    else:
        balance -= amount
        print(f"{amount} withdrawn")
        print(f"Your new balance {balance}")

# Simulating interaction with the cash machine
print("********************************")
print("***   Welcome to the cash machine   ***")
print("********************************")
if(check_pin(int(input("Enter Pin Number : ")))):
    print("Welcome to your account")
    print(f"Current balance: £{balance}")
    withdraw_cash(float(input("Enter Amount To Withdraw : £")))
