
hn = []
pn = []
common = []

#loading files into lists

with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line != '':
        hn.append(int(line))
        line = open_file.readline()
print('hm loaded')

with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line != '':
        pn.append(int(line))
        line = open_file.readline()
print('pn loaded')

common = list(set(hn+pn))

print(sorted(common))
