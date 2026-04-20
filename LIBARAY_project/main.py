import library

while True:
    print("\n====== LIBRARY MENU ======")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.show_books()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        print("Thank you ")
        break
    else:
        print(" Invalid choice")