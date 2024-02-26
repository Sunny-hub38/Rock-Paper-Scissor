import random

def play():
    r = 'rock'
    s = 'scissors'
    p = 'paper'
    user = input(f"What\'s your choice? {r} for rock, {s} for scissors, {p} for paper")
    computer = random.choice(['r', 's', 'p'])

    if(user == computer):
        return 'It\'s a Tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return  'It\'s a loss'

    return 'It\'s a win'

def is_win(player, opponent):
    # return if player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):

        return True
