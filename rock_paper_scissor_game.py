from random import choice
# why we use tuple instead of list. A:Becz lists are mutable so if we change the value accidently so there will be problem
ROCK = "r"
PAPER = "p"
SCISSOR = "s"

emojis = {ROCK: "🪨", PAPER: "📃", SCISSOR: "✂️"}
choices = tuple(emojis.keys())


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
    elif ((user_choice == ROCK and computer_choice == SCISSOR) or
          (user_choice == SCISSOR and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
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
