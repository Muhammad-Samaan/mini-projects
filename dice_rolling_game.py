from random import randint
while True:
    choice = input("Roll the dice (y/n)").lower()
    if choice == "y":
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        print(f"({dice1},{dice2})")
        # break
    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")
        # break
