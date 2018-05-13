


def load_data (file_name):
    birthdays = dict()

    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            birthdays[line.split(' ')[0]] = (line.split(' ')[1]).strip('\n')
            line = open_file.readline()
    return birthdays





    your_name = input('Who\'s birthday you want to know? ')
    print(birthdays[your_name])
