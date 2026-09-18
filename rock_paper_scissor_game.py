from random import choice
# why we use tuple instead of list. A:Becz lists are mutable so if we change the value accidently so there will be problem

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ["r", "p", "s"]
while True:
    user_choice = input(
        "Enter your choice Rock , Paper or Scissor (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = choice(choices)
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer choose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Match Tie")
    elif ((user_choice == "r" and computer_choice == "s") or
          (user_choice == "s" and computer_choice == "p") or
            (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else:
        print("You lose")

    player_continue = input("Do you want continue playing (y/n): ").lower()
    if player_continue == "n":
        print("Thanks for playing.")
        break
