Kovács Tamás Levente

Szöveg titkosító

Feladat leírása:
Egy egyszerű szöveg titkosító és visszafejtő alkalmazás, amely a felhasználó által megadott szöveget titkosítja egy véletlenszerű kulcs segítségével, 
majd a titkosított szöveget vissza tudja fejteni az eredeti szöveggé. 

Osztály:
SzovegTitkositoKTL: Ez az osztály felelős a titkosítási és visszafejtési folyamatok kezeléséért a grafikus felhasználói felületen keresztül. 

Modulok:
Tkinter: A grafikus felület megvalósításához használt modul.
random: A titkosító kulcs véletlenszerű generálásához használt modul.
szoveg_titkosito_KTL: Ez egy saját modul, amely felelős a szöveg titkosításáért és visszafejtéséért.

Osztály:
SzovegTitkositoKTL: Ez az osztály felelős a titkosítási és visszafejtési folyamatok kezeléséért a grafikus felhasználói felületen keresztül.

Függvények:
uiKTL(): A felhasználói felület létrehozása, beleértve a bemeneti mezőt, a gombokat és a kimeneti mezőket.
titkositasKTL(): A megadott szöveg titkosítása a generált kulcs segítségével.
visszafejtesKTL(): A titkosított szöveg visszafejtése a kulcs és az eredeti karakterek listájának felhasználásával.
