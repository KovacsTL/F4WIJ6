from tkinter import *
from szoveg_titkosito_KTL import SzovegTitkositoKTL

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Szöveg Titkosító")
        self.master.geometry("500x350")
        self.master.resizable(False, False)

        self.szo_titkosito = SzovegTitkositoKTL()

        #Szöveg bemenet és kimenetek
        self.szoveg_bemenet = Entry(master, width=50)
        self.titkositott_kimenet = StringVar()
        self.visszafejtett_kimenet = StringVar()

        self.ui()

    def ui(self):
        Label(self.master, text="Titkosítandó szöveg:").pack(pady=5)
        self.szoveg_bemenet.pack()

        Label(self.master, text="Titkosított szöveg:").pack(pady=5)
        Entry(self.master, textvariable=self.titkositott_kimenet, width=50).pack()

        Label(self.master, text="Visszafejtett szöveg:").pack(pady=5)
        Entry(self.master, textvariable=self.visszafejtett_kimenet, width=50).pack()

        Button(self.master, text="Titkosítás", command=self.titkositas).pack(pady=10)
        Button(self.master, text="Visszafejtés", command=self.visszafejtes).pack(pady=5)
        Button(self.master, text="Kilépés", command=self.master.quit).pack(pady=50)

    def titkositas(self):
        #Szöveg titkosítása
        szoveg = self.szoveg_bemenet.get()
        titkositott = self.szo_titkosito.titkositas(szoveg)
        self.titkositott_kimenet.set(titkositott)

    def visszafejtes(self):
        #Titkosított szöveg visszafejtése
        titkositott = self.titkositott_kimenet.get()
        visszafejtett = self.szo_titkosito.visszafejtes(titkositott)
        self.visszafejtett_kimenet.set(visszafejtett)

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()