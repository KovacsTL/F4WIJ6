import random

#Karakterek listája és kulcs generálása
class SzovegTitkositoKTL:
    def __init__(self):
        self.karakterek = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÚÜÖÓŰabcdefghijklmnopqrstuvwxyzáéúüöóű!%.?_-@*(){}'=/,;: "
        self.karakterek = list(self.karakterek)
        self.kulcs = self.karakterek.copy()
        random.shuffle(self.kulcs)

    #Szöveg titkosítása
    def titkositas_KTL(self, szoveg):
        titkositott = ""
        for betu in szoveg:
            if betu in self.karakterek:
                index = self.karakterek.index(betu)
                titkositott += self.kulcs[index]
            else:
                titkositott += betu
        return titkositott

    #Titkosított szöveg visszafejtése
    def visszafejtes_KTL(self, titkositott):
        visszafejtett = ""
        for betu in titkositott:
            if betu in self.kulcs:
                index = self.kulcs.index(betu)
                visszafejtett += self.karakterek[index]
            else:
                visszafejtett += betu
        return visszafejtett

    #Kulcs mentése
    def kulcs_mentes_txt_KTL(self, file):
        with open(file, 'w') as file:
            file.write(' '.join(self.kulcs))

    #Kulcs betöltése
    def kulcs_betoltes_txt_KTL(self, file):
        with open(file, 'r') as file:
            self.kulcs = file.read().split()