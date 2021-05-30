import os
import shutil
from extensions import paths

#get listing of files/directores outside the current directory (brains)
directory_list = os.listdir('../')

def get_extension(file: str) -> str:
    period_points = []
    i = 0
    for character in file:
        if character == '.':
            period_points.append(i)
        i += 1
    return file[period_points[-1]: len(file)]

# Moving file to a directory
for entry in directory_list:
    if '.' not in entry or entry == '.git':
        continue
    else:
        shutil.move('../' + entry, '../' + paths.get(get_extension(entry)), shutil.copy2)
