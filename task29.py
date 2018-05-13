import random
from task29_hang import draw_hangman

words = list()
characters = set()
hangman_phase = 0



with open('sowpods.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        words.append(line)
        line = open_file.readline().strip('\n')

word = words[random.randrange(0, len(words))]
guess = [''] * (len(word))
print(word)

print('>>> Welcome to Hangman!\n')
print('=======================\n')

while guess != list(word):
    print(guess)
    found = False

    letter = input('Guess your letter: ').upper()
    characters.add(letter)
    i = -1
    for char in word:
        i += 1
        if char == letter:
            found = True
            guess[i] = letter
    if not found:
            hangman_phase += 1

            if hangman_phase == 6:
                print('\n===============')
                print('Wrong ! You are dead!')
                draw_hangman(hangman_phase)
                print('\n===============')
            else:
                print('\n===============')
                print('Wrong ! Watch out !')
                draw_hangman(hangman_phase)
                print('\n===============')

