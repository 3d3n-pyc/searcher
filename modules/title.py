import threading
import pystyle
import time

LocheMan = ['...', 'L...' ,'Lo...' ,'Loc...' ,'Loch...' ,'Loche...' ,'LocheM...' ,'LocheMa...',         \
            'LocheMan' ,'LocheMan...' ,'LocheMan' ,'LocheMan...' ,'LocheMan' ,'LocheMan...' ,'LocheMan' \
            ,'LocheMa' ,'LocheM' ,'Loche' ,'Loch' ,'Loc' ,'Lo' ,'L']

def locheman():
    global stop
    stop = False

    global isImported
    isImported = False
    while not stop:
        number = 0
        for title in LocheMan:
            if not stop:
                number += 1
                if title == 'LocheMan' or title == 'LocheMan...':
                    pystyle.System.Title(f'Searcher  -  By {title}')
                    time.sleep(0.5)
                else:
                    pystyle.System.Title(f'Searcher  -  By {title}')
                    time.sleep(0.1)
            else:
                pass

def start():
    title = threading.Thread(target=locheman)
    title.start()

def stop():
    stop = True
    pystyle.System.Title(f'Searcher  -  By LocheMan')
