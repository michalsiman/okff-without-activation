# tento script vezme soubor *.csv ktery najde ve slozce, pak si vezme soubor okff.gpx ktery najde ve slozce
# a vytvori soubor okff-noactivation.gpx ktery ulozi a v kterem budou pouze a jen okff ze souboru .csv doplnene o presnou polohu
# cele to slouzi k tomu, aby se dala do LOCUSU pridat dalsi vrstva s OKFF ktere jeste nikdo neaktivoval

# udelal OK1SIM pro komunitu OKFF
# pouzivej dle libosti, upravuj, sir, proste je to tvoje ...

i = 0

print("Zacinam pracovat, hledam, prochazim, cekej prosim ...")

# nejdriv procistime soubor okff-without-.....
file_to_delete = open("okff-without-activation.gpx",'w')
file_to_delete.close()

with open("okff-without-activation.gpx","a") as file:
    file.write('<?xml version="1.0" encoding="windows-1250" standalone="no" ?>\n\n')
    file.write('<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" creator="GPS Data Team ( http://www.gps-data-team.com )">\n\n')

with open('okff.gpx') as f:
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

print("\nCelkem nalezeno v okff.gpx ", i, " OKFF mist bez aktivace a z tech jsem vytvoril soubor okff-without-activation.gpx. Hotovo, koncim!")
