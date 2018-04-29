'''
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
'''



def draw(size):
    line = ' ---'
    wall = '|   '

    for i in range(size):
        print(line*size)
        print(wall*size + '|')
    print(line*size)

size = input('What size of board would you like me to draw? ')
draw(int(size))