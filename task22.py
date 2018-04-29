dictn = dict()

with open('nameslist.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line in dictn.keys():
            dictn[line] += 1
        else:
            dictn[line] = 1
        line = open_file.readline()

for name, val in dictn.items():
    print(name, val)