#Rock beats scissors
#Scissors beats paper
#Paper beats rock

dict = ['scissors', 'rock', 'paper']

player1 = input('Player 1, please choose: scissors, rock or paper: ')
while player1 not in dict:
    player1 = input('Player 1, you can only choose scissors, rock or paper. Please bet again: ')


player2 = input('Player 2, please choose: scissors, rock or paper: ')
while player2 not in dict:
    player2 = input('Player 2, you can only choose scissors, rock or paper. Please bet again: ')

def winner(bet1, bet2):
    if bet1 == bet2:
        return('It\'s a tie')
    elif bet1 == 'scissors':
        if bet2 == 'paper':
            return('Scissors win')
        elif bet2 == 'rock':
            return('Rock wins')
    elif bet1 == 'rock':
        if bet2 == 'paper':
            return ('Paper wins')
        elif bet2 == 'scissors':
            return ('Rock wins')
    elif bet1 == 'paper':
        if bet2 == 'scissors':
            return ('Scissors win')
        elif bet2 == 'rock':
            return ('Paper wins')


print(winner(player1,player2))