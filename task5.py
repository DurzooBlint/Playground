import random
import time

a = []
b = []
c = []

start = time.time()
print('randomizing...\n')

for i in range(random.randint(9,99),random.randint(9,999)):
    a.append(random.randint(1,999))

for i in range(random.randint(9, 99), random.randint(9, 999)):
    b.append(random.randint(1, 999))

a.sort()
b.sort()
end = time.time()
print('...done in '+ str(end - start))

print(a)
print(b)


for item in a:
    if item in b:
        c.append(item)

print (c)

