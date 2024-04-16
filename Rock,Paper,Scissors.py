import random
import time

print("--------___------------------Rock, Paper, Scissors Game in Python------------------___--------")
time.sleep(3)

# Game Loop
Done = False
while not Done:
    choice = input("\nEnter a choice:  ")
    computer_choice = random.choice(['Rock','Paper', 'Scissors'])

    # Main game logic
    if choice == computer_choice:
        print(f"Its a tie! Both Chose {choice}\n")
        Done = True

    elif choice == 'Rock':
        if computer_choice == 'Paper':
            print(f"Computer Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
        else:
            print(f"You Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
    elif choice == 'Paper':
        if computer_choice == 'Scissors':
            print(f"Computer Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
        else:
            print(f"You Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
    elif choice == 'Scissors':
        if computer_choice == 'Rock':
            print(f"Computer Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
        else:
            print(f"You Won! You chose {choice} and Computer chose {computer_choice}\n")
            Done = True
    else:
        print("Please enter a valid Choice\n")
        Done = True
