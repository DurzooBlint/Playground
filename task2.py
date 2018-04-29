import datetime

date = datetime.datetime.now()

rand = int(input('provide random number: '))

if rand%4 ==0:
    print('it\'s multiple of 4')
else:
    if rand%2 == 0:
        print('it\'s even!')
    else:
        print('it\'s odd!')

num = int(input('provide number: '))
div = int(input('provide divider: '))
if num % div == 0:
    print('num is multiple of div')
else:
    print('learn math boy')
