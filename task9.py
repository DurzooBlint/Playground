import random

print('Welcome in number guessing game. Type \'quit\' anytime to stop.\n')
guess =''

while guess != 'quit':
    number = random.randint(1,99)
    while guess != number and guess != 'quit':
        guess = int(input('Make your guess: '))
        if guess == number:
            print('That\'s it ! you won!\n')
            guess=input('Press any button to play again or type \'quit\' to stop. \n')
        elif guess > number:
            print('Too high!')
        elif guess < number:
            print('Too low!')



