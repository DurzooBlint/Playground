import random
import math

def binary_search(listp, number):
    result_len = len(listp)
    result = listp
    while result_len > 1:
        result = sublist(listp,number)
        result_len = len(result)
    if result[0] == number:
        return True
    else:
        return False


    return True

def sublist(list_s,number_s):
    print(list_s)
    if len(list_s) == 1:
        return list_s

    middle_p = math.floor(round(len(list_s) / 2))
    middle_value = list_s[middle_p]
    print('Middle of list: ' + str(middle_value))
    if number_s == middle_value:
        return [number_s]
    elif number_s > middle_value:
        return sublist(list_s[middle_p:], number_s)
    elif number_s < middle_value:
        return sublist(list_s[:middle_p], number_s)
    else:
        return []

random_list = []
random_list = random.sample(range(100),20)

input = int(input('Please provide number: '))

random_list.sort()

if(binary_search(random_list,input)):
    print('Number is part of list')
else:
    print('Number is missing')