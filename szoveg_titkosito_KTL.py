import random

class SzovegTitkositoKTL:
    def __init__(self):
        # Karakterek listája és kulcs generálása
        self.karakterek = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÚÜÖÓŰabcdefghijklmnopqrstuvwxyzáéúüöóű!%.?_-@*(){}'=/,;: "
        self.karakterek = list(self.karakterek)
        self.kulcs = self.karakterek.copy()
        random.shuffle(self.kulcs)

    def titkositas(self, szoveg):
        # Szöveg titkosítása
        titkositott = ""
        for betu in szoveg:
            if betu in self.karakterek:
                index = self.karakterek.index(betu)
                titkositott += self.kulcs[index]
            else:
                titkositott += betu
        return titkositott

    def visszafejtes(self, titkositott):
        # Titkosított szöveg visszafejtése
        visszafejtett = ""
        for betu in titkositott:
            if betu in self.kulcs:
                index = self.kulcs.index(betu)
                visszafejtett += self.karakterek[index]
            else:
                visszafejtett += betu
        return visszafejtett