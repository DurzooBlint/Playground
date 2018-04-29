import datetime

date = datetime.datetime.now()

name = input('Give me your name: ')
age = int(input('and your age: '))
rand = int(input('provide random number: '))
print(rand*(name + ' you will hit 100 yo in ' + str((date.year + 100-age)) +'\n'))