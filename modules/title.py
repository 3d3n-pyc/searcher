import threading
import pystyle
import time

LocheMan = ['...', '3...' ,'3D...' ,'3D3...',         \
            '3D3N' ,'3D3N...' ,'3D3N' ,'3D3N...' ,'3D3N' ,'3D3N...' ,'3D3N' \
            ,'3D3' ,'3D' ,'3']

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
                if title == '3D3N' or title == '3D3N...':
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
    pystyle.System.Title(f'Searcher  -  By 3D3N')
