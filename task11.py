
#checks if number is prime (it has no dividors but itself and 1)
def isPrime(num):
    dividers = []
    x = range(1, num, 1)

    for item in x:
        if num % item == 0:
            dividers.append(item)
    if dividers.__len__() == 1:
        return True
    else:
        return False


number = int(input("Please provide number: "))
if isPrime(number):
    print('It\'s a prime number')
else:
    print('It\'s not a prime number')
