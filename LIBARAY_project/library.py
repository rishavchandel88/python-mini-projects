books = {
    "python": {"available": True},
    "java": {"available": True},
    "c++": {"available": True}
}

issued_books = {}

def show_books():
    print("\n Available Books:")
    for book, info in books.items():
        status = "Available" if info["available"] else "Not Available"
        print(f"- {book} ({status})")

def issue_book():
    book = input("Enter book name: ").lower()
    
    if book in books:
        if books[book]["available"]:
            name = input("Enter student name: ")
            days = int(input("For how many days: "))
            
            books[book]["available"] = False
            issued_books[book] = {
                "student": name,
                "days": days
            }
            print(" Book Issued Successfully")
        else:
            print(" Book not available")
    else:
        print(" Book not found")

def calculate_fine(extra_days):
    fine = 0
    rate = 10
    week = 1

    while extra_days > 0:
        days = min(7, extra_days)
        fine += days * rate
        rate *= (week + 1)
        week += 1
        extra_days -= days

    return fine

def return_book():
    book = input("Enter book name to return: ").lower()

    if book in issued_books:
        used_days = int(input("Enter number of days used: "))
        allowed_days = issued_books[book]["days"]

        if used_days > allowed_days:
            extra = used_days - allowed_days
            fine = calculate_fine(extra)
            print(f" Late return! Fine = ₹{fine}")
        else:
            print(" Returned on time")

        books[book]["available"] = True
        del issued_books[book]
        print(" Book Returned Successfully")
    else:
        print(" This book was not issued")