import random

number = []
guess = []
while (len(number) <4):
    number.append(str(random.randint(0,9)))

while (guess != number):
    guess = list(input('Please guess 4 digits: '))
    guess = guess[0:4]

    print('Number: ' + "".join(str(x) for x in number))
    print('Guess: ' + "".join(str(x) for x in guess))
    cows = []
    bulls = []
    for x in number:
        bulls.append([x for y in guess if x==y])
        cows.append([x for y in guess if (x==y and number.index(x) == guess.index(y))])


    bulls = list(filter(None, bulls))
    cows = list(filter(None, cows))

    print('Cows final: ' + "".join(str(x) for x in cows))
    print('Bulls final: ' + "".join(str(x) for x in bulls))
    print('Cows : ' + str(len(cows)))
    print('Bulls : ' + str(len(bulls)))


print('Number final: ' + "".join(str(x) for x in number))
print('Guess final: ' + "".join(str(x) for x in guess))