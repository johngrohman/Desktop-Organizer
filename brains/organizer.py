import os
import shutil
from extensions import paths

this = True

def get_extension(file: str) -> str:
    '''
    Function that returns the extension of an inputed file
    '''
    period_points = []
    i = 0
    for character in file:
        if character == '.':
            period_points.append(i)
        i += 1
    return file[period_points[-1]: len(file)]

while this == True:
    #get listing of files/directores outside the current directory (brains)
    directory_list = os.listdir('../')
    print('\033[H\033[J')
    print('Running...')

    # Moving file to their respective directory
    for entry in directory_list:
        # print(entry)
        if ('.' not in entry) or (entry[0] == '.'):
            continue
        elif str(paths.get(get_extension(entry))) == 'None':
            shutil.move('../' + str(entry),  '../unorganized/', shutil.copy2)
        else:
            shutil.move('../' + str(entry),  '../' + str(paths.get(get_extension(entry))), shutil.copy2)
