Kovács Tamás Levente
Szöveg titkosító

Feladat leírása:
Egy egyszerű szöveg titkosító és visszafejtő alkalmazás, amely a felhasználó által megadott szöveget titkosítja egy véletlenszerű kulcs segítségével, majd a titkosított szöveget vissza tudja fejteni az eredeti szöveggé. A titkosításhoz véletlenszerűen generált kulcsot lehetőség van lementeni és később felhaszálni.

Modulok:
Tkinter: A grafikus felület megvalósításához használt modul.
random: A titkosító kulcs véletlenszerű generálásához használt modul.
szoveg_titkosito_KTL: Ez egy saját modul, amely felelős a szöveg titkosításáért, visszafejtéséért illetve a kulcs lementéséért és betöltéséért.

Osztályok:
SzovegTitkositoKTL: Ez az osztály kezeli a titkosítást és a visszafejtést, valamint Kulcsokat generál, fájlba ment, és betölt a későbbi használathoz.
GUI_KTL: Ez az osztály a grafikus felhasználói felületet kezeli. A Tkinter segítségével létrehozza az ablakot, kezel különböző gombokat és szövegmezőket, és összekapcsolja azokat a SzovegTitkositoKTL osztály metódusaival.

Függvények:
ui_KTL: A felhasználói felület létrehozása, beleértve a bemeneti mezőt, a gombokat és a kimeneti mezőket.
titkositas_KTL: A megadott szöveg titkosítása a generált kulcs segítségével.
visszafejtes_KTL: A titkosított szöveg visszafejtése a kulcs és az eredeti karakterek listájának felhasználásával.
kulcs_mentes_txt_KTL: Lementi a kulcsot egy TXT fájlba.
kulcs_betoltes_txt_KTL: Betölti a lementett kulcsot.
