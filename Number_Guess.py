import random

computer_output = random.randint(1, 100)
attempt = 0

while True:

    try:
        player_output = int(input("Please Guess a Number Between 1 to 100: "))
        attempt += 1

    except ValueError:
        print("Please Enter a valid integer number.")
        continue


    if player_output > computer_output:
        print(f"{player_output} is too high, Guess Again.")


    elif player_output < computer_output:
        print(f"{player_output} is too low, Guess Again.")


    else:
        print(f"Your Guess is correct, You attempt {attempt} times.")
        break