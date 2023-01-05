"""
Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b 
are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and 
your program must tell whether the number is greater than the actual number or less than the actual number. Log the 
number of trials it took your friend to arrive at the number. You play the same game, and then the person with the 
minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
"""

import random
player1 = input("Enter Player 1 Name :")
player2 = input("Enter Player 2 Name :")
gamePlayer = [player1, player2]
scoreLog = []

for player in gamePlayer:
    random_a = random.randint(1, 50)
    random_b = random.randint(80, 100)
    random_num = random.randint(random_a, random_b)
    print(random_num)
    attempt = 1  # If you guess the number in 1st attempt it'll count it.
    print(f"{player}, Try to guess the number between {random_a} and {random_b}.\n")

    while True:
        guess_a = int(input(f"Guess The number : "))
        if guess_a == random_num:
            print(f">>> Congrats !! You made it at {attempt} attempts.\n")
            # Because counting starts from 1 so in this loop we'll not going to add +1
            scoreLog.append(attempt)
            break
        elif guess_a > random_b or guess_a < random_a:
            print("You're going Out of range. Open your Eyes and read the range.\n")

        elif guess_a > random_num:
            print(">>> Go down bro !! It's high\n")
            attempt += 1

        elif guess_a < random_num:
            print(">>> GO up bro !! It's low\n")
            attempt += 1

# Who wins the game --
if scoreLog[0] < scoreLog[1]:
    print("\t\t\tCongratulations !!")
    print(f"\t\t\t{player1} took {scoreLog[0]} attempts")
    print(f"\t\t** {player1} Won !! **")
elif scoreLog[0] > scoreLog[1]:
    print("\t\t\tCongratulations !!")
    print(f"\t\t\t{player2} took {scoreLog[1]} attempts")
    print(f"\t\t** {player2} Won !! **")
else:
    print("\t\t\tIt's a Draw")
    print(f"\t\t\t{player1} took {scoreLog[0]} attempts")
    print(f"\t\t\t{player2} took {scoreLog[1]} attempts")

