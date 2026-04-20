import random

def stone_paper_scissors():
    choices = ["stone", "paper", "scissors"]
    
    user = input("Enter (stone/paper/scissors): ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print(" It's a Draw")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print(" You Win!")
    else:
        print(" You Lose!")

def dice_game():
    user = random.randint(1, 6)
    computer = random.randint(1, 6)

    print(" You rolled:", user)
    print(" Computer rolled:", computer)

    if user > computer:
        print(" You Win!")
    elif user < computer:
        print(" You Lose!")
    else:
        print(" It's a Draw")