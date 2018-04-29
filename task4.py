
num = int(input('Please provide number: '))

dividers = []
x = range(1,num,1)

for item in x:
    if num%item == 0:
        dividers.append(item)

dividers.append(num)
print(dividers)

