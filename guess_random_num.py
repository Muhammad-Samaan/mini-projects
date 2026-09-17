from random import randint

ran_num = randint(1, 100)
while True:
    guess_num = int(input("Guess the number between 1 and 100 : "))
    if (ran_num > guess_num):
        print("number is too low")
    elif (ran_num < guess_num):
        print("number is too high")
    else:
        print(f"Congratulations You guess the right number {ran_num}")
        break
