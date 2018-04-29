dictn = dict()

with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    temps = (line.split('/'))[2]
    while line:
        if temps in dictn.keys():
            dictn[temps] += 1
        else:
            dictn[temps] = 1
        line = open_file.readline()
        if line != '':
            temps = (line.split('/'))[2]
for name, val in dictn.items():
    print(name, val)