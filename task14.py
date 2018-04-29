
#Function takes list, converts it to set in order to remove duplicates and then return the result as list
def removeDupliacates (listInput):
    tempSet = set(listInput)
    tempList = list(tempSet)
    return tempList



namesRaw = input("Provide names: ")
names = namesRaw.split()

print('Your string with names after split:')

for name in names:
    print(name)

print('\n')

namesUnique = removeDupliacates(names)
print('List without duplicates: ')

print(namesUnique)


