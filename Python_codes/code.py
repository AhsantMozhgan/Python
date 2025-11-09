import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r' : 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}
print(random.choice(choices))
user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')
ai_choice = random.choice(choices)
if user_choice in choices:
    # print(f'Your choice is {user_choice}. AI choice is {ai_choice}.')
    print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
    #r›s - p›r - s›p
    if user_choice == ai_choice:
        print( 'Tie')
    # elif user_choice == 'r' and ai_choice == 's' :
    #     print( 'You Won!')
    # elif user_choice == 'p' and ai_choice == 'r':
    #     print( 'You Won!')
    # elif user_choice == 's' and ai_choice == 'p':
    #     print( 'You Won!')
    elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
        print( 'You Won!')
    else:
        print( 'You Lost!')
else:
    
    
# p
# Select from Rock, Paper, Scissors: (r, p, s) r
# Your choice is Rock. AI choice is Scissors.
# You Won!