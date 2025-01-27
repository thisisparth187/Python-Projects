import random as r

list_choices = ['rock', 'paper', 'scissor']

def start():
    u_ch = user_choice()
    b_ch = bot_choice()
    winner = win_check(u_ch,b_ch)
    if winner == 'Tie':
        print("It's a tie")
    else:
        print(f"The winner is {winner}")
def user_choice():
    user_ch = input('Enter your choice: ')
    return user_ch

def bot_choice():
    bot_ch = r.choice(list_choices)
    print(f"The bot chooses: {bot_ch}")
    return bot_ch

def win_check(b_ch, u_ch):
    if b_ch == u_ch:
        return 'Tie'
    elif (b_ch == 'rock' and u_ch == 'scissor') or (b_ch == 'paper' and u_ch == 'rock') or (b_ch == 'scissor' and u_ch == 'paper'):
        return  'Bot'
    else:
        return 'User'

start()