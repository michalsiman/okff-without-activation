import requests
import re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

link = "https://wwff.co/directory/statistics/"
f = requests.get(link)
b = f.text
i = 0
vypis = 0
okff_jmeno = ''
okff_aktivaci = ''

for line in b.split('\n'):
    i += 1
    line = line.strip('\r')
    if 'OKFF-' in line or vypis > 0:
        if vypis == 0:
            okff_jmeno = cleanhtml(line)
        if vypis == 3:
            okff_aktivaci = cleanhtml(line)
        if vypis == 0 or vypis >0:
            vypis += 1
        if vypis > 5:
            if int(okff_aktivaci.replace(',', '')) == 0:
                print (okff_jmeno)
            vypis = 0
        
    
    
