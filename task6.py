word = input('please provide a word: ')

wordc = word[::-1]

print(word)
print(wordc)

if word==wordc:
    print('your word is palimdrome')