import random

#Karakterek listája és kulcs generálása
class SzovegTitkositoKTL:
    def __init__(self):
        self.karakterek_KTL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÚÜÖÓŰabcdefghijklmnopqrstuvwxyzáéúüöóű!%.?_-@*(){}'=/,;: "
        self.karakterek_KTL = list(self.karakterek_KTL)
        self.kulcs_KTL = self.karakterek_KTL.copy()
        random.shuffle(self.kulcs_KTL)

    #Szöveg titkosítása
    def titkositas_KTL(self, szoveg_KTL):
        titkositott_KTL = ""
        for betu_KTL in szoveg_KTL:
            if betu_KTL in self.karakterek_KTL:
                index_KTL = self.karakterek_KTL.index(betu_KTL)
                titkositott_KTL += self.kulcs_KTL[index_KTL]
            else:
                titkositott_KTL += betu_KTL
        return titkositott_KTL

    #Titkosított szöveg visszafejtése
    def visszafejtes_KTL(self, titkositott_KTL):
        visszafejtett_KTL = ""
        for betu_KTL in titkositott_KTL:
            if betu_KTL in self.kulcs_KTL:
                index_KTL = self.kulcs_KTL.index(betu_KTL)
                visszafejtett_KTL += self.karakterek_KTL[index_KTL]
            else:
                visszafejtett_KTL += betu_KTL
        return visszafejtett_KTL

    # Kulcs mentése
    def kulcs_mentes_txt_KTL(self, fajlnev_KTL):
        with open(fajlnev_KTL, 'w') as file_KTL:
            file_KTL.write(' '.join(self.kulcs_KTL))

    #Kulcs betöltése
    def kulcs_betoltes_txt_KTL(self, fajlnev_KTL):
        with open(fajlnev_KTL, 'r') as file_KTL:
            self.kulcs_KTL = file_KTL.read().split()