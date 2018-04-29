import random

def genPass (lenght, complexity):
    pool = []
    if (lenght < 8):
        lenght = 8

    if complexity == 1:
        pool = wordList + numbers
    elif complexity == 2:
        pool = wordList + numbers + alphabetLower
    elif complexity == 3:
        pool = wordList + numbers + alphabetLower + charList
    elif complexity == 4:
        pool = wordList + numbers + alphabetLower + alphabetUpper + charList
    else:
        pool = wordList + numbers + alphabetLower + alphabetUpper + charList
    return fitLen(lenght,pool)


def fitLen (lenght, poolArg):
    password = []
    while (len(''.join(map(str,password))) < lenght):
        gen = random.randint(0,(len(poolArg) -1))
        if (len(''.join(map(str,poolArg[gen]))) + len(''.join(map(str,password))) <=lenght ):
            password.append(poolArg[gen])
    return  ''.join(map(str,password))

wordList = ['spring','winter', 'summer', 'autumn', 'january', 'february', 'earth', 'sun', 'car' , 'mouse', 'dog', 'house']
charList = ['!','@','#','$','%','^','&','*']
alphabetLower = list(map(chr, range(97, 123)))
alphabetUpper = list(map(chr, range(65, 91)))
numbers = range(0,10)
numbers = list(map(str, numbers))

print(wordList)
print(charList)
print(alphabetLower)
print(alphabetUpper)
print(numbers)

lenght = int(input('Please provide lenght of your password (can\'t be less than 8): '))
complexity = int(input('Please provide desired complexity of password from 1 to 4, where 4 is the strongest password: '))

print(genPass(lenght,complexity))




