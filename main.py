import os
import argparse
import sys
import time


class color:
    white = '\033[38;2;255;255;255m'
    dark_gray = '\033[38;2;100;100;100m'
    gray = '\033[38;2;150;150;150m'
    red = '\033[38;2;255;0;0m'
    orange = '\033[38;2;255;150;0m'
    turquoise = '\033[38;2;0;150;255m'
    cyan = '\033[38;2;0;255;255m'

def listFiles(path:str) -> list:
    filePaths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filePaths.append(path + os.path.relpath(os.path.join(root, file), start=path))
    return filePaths

def search(value:str, path:str, lower:bool) -> str:
    output = ''
    value = value.lower() if lower else value
    
    for i, line in enumerate(open(path, 'r', encoding='latin-1').readlines()):
        if value in (line.lower() if lower else line):
            i += 1
            espaces = ' ' * (7 - len(str(i)))
            output += f'  {color.turquoise}{i}{espaces}{color.cyan}{line}'
    
    return output if output else None


parser = argparse.ArgumentParser(
    prog='searcher',
    description='Search in all files of directory',
    epilog="Script by '@3d3n.pyc'. (https://github.com/LocheMan)"
)

parser.add_argument('value',
                    help='value to search')

parser.add_argument('-l', '--lower', action='store_true',
                    help='lower value')

parser.add_argument('-t', '--time', action='store_true',
                    help='show time of search')

parser.add_argument('-p', '--path', type=str,
                    help='specify the path')

args:argparse.Namespace = parser.parse_args()

os.system('title Search in progress...')


value = args.value

lower = args.lower
timeArg = args.time
pathArg = args.path


if pathArg and not os.path.exists(pathArg):
    print(color.red + 'Path is invalid')
    print(color.white, end='')
    sys.exit()

if pathArg in ['', None]:
    pathArg = '.\\'
    
if pathArg:
    pathArg = pathArg.replace('/', '\\')

if not pathArg.endswith('\\'):
    pathArg += '\\'


if value == "":
    print(color.red + 'Value is empty.\n')
    print(color.white, end='')
    sys.exit()

found = False

if timeArg:
    start = time.time()


files = listFiles(pathArg)

for file in files:
    result = search(value, file, lower)
    
    if result != None:
        found = True
        print('\033[38;2;40;70;200m' + file)
        print(result)

if timeArg:
    end = time.time()
    timeTaken = round(end-start, 3)

if not found:
    print(color.orange + 'Value not found.\n')


if timeArg:
    print(f'{color.dark_gray}Time taken by search : {color.gray}{timeTaken}{color.dark_gray}s')

print(color.white, end='')
