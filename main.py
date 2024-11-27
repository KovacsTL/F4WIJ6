from tkinter import *
from szoveg_titkosito_KTL import SzovegTitkositoKTL

class GUI_KTL:
    def __init__(self, master_KTL):
        self.master_KTL = master_KTL
        self.master_KTL.title("Szöveg Titkosító")
        self.master_KTL.geometry("500x350")
        self.master_KTL.resizable(False, False)

        self.szo_titkosito_KTL = SzovegTitkositoKTL()

        #Szöveg bemenet és kimenetek
        self.szoveg_bemenet_KTL = Entry(master_KTL, width=50)
        self.titkositott_kimenet_KTL = StringVar()
        self.visszafejtett_kimenet_KTL = StringVar()

        self.ui_KTL()

    def ui_KTL(self):
        Label(self.master_KTL, text="Titkosítandó szöveg:").pack(pady=5)
        self.szoveg_bemenet_KTL.pack()

        Label(self.master_KTL, text="Titkosított szöveg:").pack(pady=5)
        Entry(self.master_KTL, textvariable=self.titkositott_kimenet_KTL, width=50).pack()

        Label(self.master_KTL, text="Visszafejtett szöveg:").pack(pady=5)
        Entry(self.master_KTL, textvariable=self.visszafejtett_kimenet_KTL, width=50).pack()

        Button(self.master_KTL, text="Titkosítás", command=self.titkositas_KTL).pack(pady=10)
        Button(self.master_KTL, text="Visszafejtés", command=self.visszafejtes_KTL).pack(pady=5)
        Button(self.master_KTL, text="Kulcs mentés", command=self.kulcs_mentes_KTL).pack(pady=5)
        Button(self.master_KTL, text="Kulcs betöltés", command=self.kulcs_betolt_KTL).pack(pady=5)
        Button(self.master_KTL, text="Kilépés", command=self.master_KTL.quit).pack(pady=50)

    def titkositas_KTL(self):
        szoveg_KTL = self.szoveg_bemenet_KTL.get()
        titkositott_KTL = self.szo_titkosito_KTL.titkositas_KTL(szoveg_KTL)
        self.titkositott_kimenet_KTL.set(titkositott_KTL)

    def visszafejtes_KTL(self):
        titkositott_KTL = self.titkositott_kimenet_KTL.get()
        visszafejtett_KTL = self.szo_titkosito_KTL.visszafejtes_KTL(titkositott_KTL)
        self.visszafejtett_kimenet_KTL.set(visszafejtett_KTL)

    def kulcs_mentes_KTL(self):
        fajlnev_KTL = "kulcs_KTL.txt"
        self.szo_titkosito_KTL.kulcs_mentes_txt_KTL(fajlnev_KTL)
        print(f"Kulcs mentve: {fajlnev_KTL}")

    def kulcs_betolt_KTL(self):
        fajlnev_KTL = "kulcs_KTL.txt"
        self.szo_titkosito_KTL.kulcs_betoltes_txt_KTL(fajlnev_KTL)
        print(f"Kulcs betöltve: {fajlnev_KTL}")

if __name__ == "__main__":
    root_KTL = Tk()
    app_KTL = GUI_KTL(root_KTL)
    root_KTL.mainloop()