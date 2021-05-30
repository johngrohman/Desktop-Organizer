import os
import shutil

#get listing of files/directores outside of brains folder
directory_list = os.listdir('../')

def get_extension(file: str) -> str:
    period_points = []
    i = 0
    for character in file:
        if character == '.':
            period_points.append(i)
        i += 1
    return file[period_points[-1]: len(file)]

print(directory_list)