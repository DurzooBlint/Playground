import random

print('Welcome in number guessing game. This time it\'s me who is going to guess your number.')
anykey = input('Let\'s begin. Think about number between 0-100. Press any key to start.')
number = random.randint(1, 100)

guess = input('Is ' + str(number) +
              ' your number?. Type: \n\'y\' if that\'s true\n\'l\' if it\'s too low\n\'h\' if i\'s too high.\n')

min_num = 0
max_num = 100
tries = 1

while guess != '':
    if guess == 'y':
        print('Woohoo, I am smart !\nIt took me ' + str(tries) + ' tries\nThank you for playing with me.')
        break
    elif guess == 'l':
        print('OOPS! let me try again...')
        min_num = number
        number = random.randrange(min_num, max_num)
    elif guess == 'h':
        print('OOPS! let me try again...')
        max_num = number
        number = random.randrange(min_num, max_num)
    else:
        print('That didn\'t work. Type: \n\'y\' if that\'s true\n\'l\' if it\'s too low\n\'h\' if i\'s too high.\n')
    guess = input('Is ' + str(number) +
                  ' your number?. Type: \n\'y\' if that\'s true\n\'l\' if it\'s too low\n\'h\' if i\'s too high.\n')
    tries +=1