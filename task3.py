a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


for item in a:
    b.append((item-5))

print(b)

num = int(input('provide number: '))

for item in a:
    if item > num:
        print(item)