from random import choice
# why we use tuple instead of list. A:Becz lists are mutable so if we change the value accidently so there will be problem
choices = ["r", "p", "s"]
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}


def get_user_choice():
    while True:
        user_choice = input(
            "Enter your choice Rock , Paper or Scissor (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer choose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Match Tie")
    elif ((user_choice == "r" and computer_choice == "s") or
          (user_choice == "s" and computer_choice == "p") or
            (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else:
        print("You lose")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        player_continue = input("Do you want continue playing (y/n): ").lower()
        if player_continue == "n":
            print("Thanks for playing.")
            break


play_game()
