# okff-without-activation

Script vytvoří seznam lokalit pro radioamatérský program Flóry a Fauny, které ještě nebyli nikdy aktivované (v OK) - tento seznam v podobě .gpx souboru se dá naimportovat do mapové aplikace (LOCUS, MAPY.CZ ...) a tam s ním pracovat.

Tento jednoduchý script má dva vstupy, tím prvním je soubor okff.gpx (najdete vždy aktuální na stránkách okff.cz) a druhým vstupem je prostý seznam doposud neaktivovaných OKFF oblastí jako .csv soubor, prostě a jednoduše na každém řádku toho .csv souboru bude jeden název OKFF, takže např. OKFF-0001. Takové .csv si můžete udělat sami, když si na stránkách wwff.co uděláte statistiku doposud neaktivovaných OKFF oblastí, označíte ty oblasti, zkopírujete do schránky a vložíte je do nové souboru např. v ONLYOFFICE nebo LIBREOFFICE, odstraníte sloupce, které obsahují cokoliv jiného než název OKFF-XXXX a uložíte to jako .csv. Nu a pak už se spustí script a ten vygeneruje soubor okff-without-activation.gpx - prostě to z toho původního kompletního .gpx souboru vytáhne do nového .gpx souboru jen ty OKFF, které tam byli a zároveň jsou i seznamu dosud neaktivovaných OKFF. To je vše. GPX soubor se pak naimportuje do např. do LOCUSu jako nová vrstva - nezapomeňte si vypnout vrstvu stávající, aby tam nebyli dvakrát stejné OKFF.

Pokud se mě v budoucnosti povede napřímo komunikovat s db wwff, tak bych si ten seznam těch dosud neaktivovaných OKFF tahal automaticky tam odtud, případně bych si tahal online i nejnovější .gpx soubor z webu okff.cz. Ale to jsou jen sny zatím ...

www.okff.cz

www.wwff.co

Michal 

OK1SIM
