import random

choices = ['r', 'p', 's']
print(random.choice(choices))
user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')
ai_choice = random.choice(choices)
if user_choice in choices:
    print(f'Your choice is {user_choice}. AI choice is {ai_choice}.')
    #r›s - p›r - s›p
    if user_choice == ai_choice:
        print( 'Tie')
    elif user_choice == 'r' and ai_choice == 's' :
        print( 'You Won!')
    elif user_choice == 'p' and ai_choice == 'r':
        print( 'You Won!')
    elif user_choice == 's' and ai_choice == 'p':
        print( 'You Won!')
    else:
        print( 'You Lost!')
else:
    print( 'Invalid input')