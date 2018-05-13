def draw_hangman(phase):
    if phase == 1:
        print('       _______')
        print('     |/')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('    _|___')

    elif phase == 2:
        print('       _______')
        print('     |/      |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('    _|___')



    elif phase == 3:
        print('       _______')
        print('     |/      |')
        print('     |      (_)')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('    _|___')

    elif phase == 4:
        print('       _______')
        print('     |/      |')
        print('     |      (_)')
        print('     |      \|/')
        print('     |')
        print('     |')
        print('     |')
        print('    _|___')

    elif phase == 5:
        print('       _______')
        print('     |/      |')
        print('     |      (_)')
        print('     |      \|/')
        print('     |       |')
        print('     |')
        print('     |')
        print('    _|___')

    elif phase == 6:
        print('       _______')
        print('     |/      |')
        print('     |      (_)')
        print('     |      \|/')
        print('     |       |')
        print('     |      / \\')
        print('     |')
        print('    _|___')
    else:
        print('')