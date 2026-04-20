import game

while True:
    print("\n====== GAME MENU ======")
    print("1. Stone Paper Scissors")
    print("2. Dice Game")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        game.stone_paper_scissors()
    elif choice == "2":
        game.dice_game()
    elif choice == "3":
        print("Thanks for playing 🎮")
        break
    else:
        print("1 Invalid choice, try again")