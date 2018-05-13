import json


def load_data (file_name):
    birthdays = dict()

    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            birthdays[line.split(' ')[0]] = (line.split(' ')[1]).strip('\n')
            line = open_file.readline()
    return birthdays




with open('birthdays.json', 'w') as f:
    data_raw = load_data('bdhs.txt')
    data_raw['Stephen'] = '25.07'
    json.dump(data_raw,f)
