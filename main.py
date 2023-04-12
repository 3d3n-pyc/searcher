import pystyle
import time
import os

import modules.title as title
import modules.watermark

title.start()

def search(name):
    files = os.listdir("data")

    total_lines = 0
    lines = 0
    message = ''
    output = ''

    for i in range(len(files)):
        with open(f'data/{files[i]}', encoding='latin-1') as f:
            file = open(f'data/{files[i]}')
            for line in f:
                if name in line:
                    total_lines += 1
                    lines += 1
                    
                    espaces = ' ' * (6 - len(str(lines)))
                    output += f'    {pystyle.Colors.turquoise}{lines}{espaces}{pystyle.Colors.cyan}{line}'
            if output != '':
                print(f'    {pystyle.Colors.light_blue}{str(files[i])} ({lines})\n{str(output)}')
        lines = 0
        output = ''

    return message

while True:
    print(search(input(f'  {pystyle.Colors.dark_green}Recherche : {pystyle.Colors.light_green}')))