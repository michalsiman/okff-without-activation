#/usr/bin/env python
# -*- coding: utf-8 -*-

# tento script vezme soubor *.csv ktery najde ve slozce, pak si vezme soubor okff.gpx ktery najde ve slozce
# a vytvori soubor okff-noactivation.gpx ktery ulozi a v kterem budou pouze a jen okff ze souboru .csv doplnene o presnou polohu
# cele to slouzi k tomu, aby se dala do LOCUSU pridat dalsi vrstva s OKFF ktere jeste nikdo neaktivoval

# skript je funkcni v Linuxu Mint a Python3
# pomoci "pip install" je treba naistalovat wget, zipfile

# pro spravny beh pod windows10 je treba na radku 45 odstranit parametr "encoding" kompletne

# udelal Michal OK1SIM pro komunitu OKFF ... 73 & 44
# pouzivej dle libosti, upravuj, sir, proste je to tvoje ...

import wget
from zipfile import ZipFile
import os
import shutil
from urllib.request import urlopen

i = 0

print("Zacinam pracovat, hledam, prochazim, cekej prosim ...")

if(os.path.isfile('okff-without-activation.gpx')):
    os.remove('okff-without-activation.gpx')

if(os.path.isfile('okff.zip')):
    os.remove('okff-without-activation.gpx')

shutil.rmtree('/okff', ignore_errors=True)

url = 'http://okff.wz.cz/download/okff.zip'
wget.download(url, 'okff.zip')

ZipFile('okff.zip').extractall('okff')

os.remove('okff.zip')

with open("okff-without-activation.gpx","a") as file:
    file.write('<?xml version="1.0" encoding="windows-1250" standalone="no" ?>\n\n')
    file.write('<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" creator="GPS Data Team ( http://www.gps-data-team.com )">\n\n')

with open('./okff/okff.gpx', encoding = 'ISO-8859-1') as f: # ve windows je třeba odstranit parametr encoding kompletně
    exist_lines = list(f)
    for exist_line in exist_lines:
        with open('bez-aktivace.csv') as b:
            new_lines = list(b)
            for new_line in new_lines:
                if new_line.strip() in exist_line:
                    #print(exist_line)
                    i = i + 1
                    with open("okff-without-activation.gpx","a") as file:
                        file.write(exist_line)

with open("okff-without-activation.gpx","a") as file:
    file.write("</gpx>")

shutil.rmtree('/okff', ignore_errors=True)

print("\nCelkem nalezeno v okff.gpx ", i, " OKFF mist bez aktivace a z tech jsem vytvoril soubor okff-without-activation.gpx. Hotovo, koncim!")
