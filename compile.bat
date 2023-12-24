echo off

echo Building...
pyinstaller main.py --onefile --icon=logo.png

echo Clean directory...
rmdir /Q /S build
del main.spec /Q

echo Move file...
move .\dist\main.exe .\searcher.exe
rmdir /Q /S dist

