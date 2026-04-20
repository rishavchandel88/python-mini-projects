balance = 1000
transactions = []

def check_balance():
    print(f"\n Current Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print(" Amount Deposited Successfully")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print(" Please collect your cash")
    else:
        print(" Insufficient Balance")

def show_statement():
    print("\n Transaction History:")
    if not transactions:
        print("No transactions yet")
    else:
        for t in transactions:
            print("-", t)