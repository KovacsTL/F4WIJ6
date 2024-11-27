Kovács Tamás Levente

Szöveg titkosító

Feladat leírása:
Egy egyszerű szöveg titkosító és visszafejtő alkalmazás, amely a felhasználó által megadott szöveget titkosítja egy véletlenszerű kulcs segítségével, 
majd a titkosított szöveget vissza tudja fejteni az eredeti szöveggé. 

SzovegTitkositoKTL
Ez az osztály felelős a titkosítási és visszafejtési folyamatok kezeléséért a grafikus felhasználói felületen keresztül. 

Modulok:
Tkinter: A grafikus felület megvalósításához használt modul.
random: A titkosító kulcs véletlenszerű generálásához használt modul.

Függvények:
uiKTL(): A felhasználói felület létrehozása, beleértve a bemeneti mezőt, a gombokat és a kimeneti mezőket.
titkositasKTL(): A megadott szöveg titkosítása a generált kulcs segítségével.
visszafejtesKTL(): A titkosított szöveg visszafejtése a kulcs és az eredeti karakterek listájának felhasználásával.