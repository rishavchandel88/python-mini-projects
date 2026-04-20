import atm

while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        atm.deposit()
    elif choice == "3":
        atm.withdraw()
    elif choice == "4":
        atm.show_statement()
    elif choice == "5":
        print("Thank you for using ATM ")
        break
    else:
        print(" Invalid choice, try again")