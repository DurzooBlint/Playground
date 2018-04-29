def fibo(number):
    list = [1]
    i=0
    while i < number:
        i+=1
        list.append(list(len(list)) + list(len(list)-1))
    return list

print(fibo(5))


