from tkinter import *
from szoveg_titkosito_KTL import SzovegTitkositoKTL

class GUI_KTL:
    def __init__(self, root):
        self.root = root
        self.root.title("Szöveg Titkosító")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.szo_titkosito = SzovegTitkositoKTL()

        #Szöveg bemenet és kimenetek
        self.szoveg_bemenet = Entry(root, width=50)
        self.titkositott_kimenet = StringVar()
        self.visszafejtett_kimenet = StringVar()

        self.ui_KTL()

    def ui_KTL(self):
        Label(self.root, text="Titkosítandó szöveg:").pack(pady=5)
        self.szoveg_bemenet.pack()

        Label(self.root, text="Titkosított szöveg:").pack(pady=5)
        Entry(self.root, textvariable=self.titkositott_kimenet, width=50).pack()

        Label(self.root, text="Visszafejtett szöveg:").pack(pady=5)
        Entry(self.root, textvariable=self.visszafejtett_kimenet, width=50).pack()

        Button(self.root, text="Titkosítás", command=self.titkositas_KTL).pack(pady=10)
        Button(self.root, text="Visszafejtés", command=self.visszafejtes_KTL).pack(pady=5)
        Button(self.root, text="Kulcs mentés", command=self.kulcs_mentes_KTL).pack(pady=5)
        Button(self.root, text="Kulcs betöltés", command=self.kulcs_betolt_KTL).pack(pady=5)
        Button(self.root, text="Kilépés", command=self.root.quit).pack(pady=50)

    def titkositas_KTL(self):
        szoveg = self.szoveg_bemenet.get()
        titkositott = self.szo_titkosito.titkositas_KTL(szoveg)
        self.titkositott_kimenet.set(titkositott)

    def visszafejtes_KTL(self):
        titkositott = self.titkositott_kimenet.get()
        visszafejtett = self.szo_titkosito.visszafejtes_KTL(titkositott)
        self.visszafejtett_kimenet.set(visszafejtett)

    def kulcs_mentes_KTL(self):
        file = "kulcs.txt"
        self.szo_titkosito.kulcs_mentes_txt_KTL(file)
        print(f"Kulcs mentve: {file}")

    def kulcs_betolt_KTL(self):
        file = "kulcs.txt"
        self.szo_titkosito.kulcs_betoltes_txt_KTL(file)
        print(f"Kulcs betöltve: {file}")

if __name__ == "__main__":
    root = Tk()
    app = GUI_KTL(root)
    root.mainloop()