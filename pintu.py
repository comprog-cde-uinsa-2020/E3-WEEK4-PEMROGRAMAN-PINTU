# memrogram pintu ruang tamu dirumah (di waktu tertentu sesuai keinginan pemilik rumah kapan mereka mengaktifkan programnya)
a=17
A=[]
while a<22:
    A.append(a)
    a=a+1
print("Pemrograman ini hanya berlaku pada pukul", A)

class pintu:
    def __init__(self, nama, ketuk, waktu):
        self.nama = nama
        self.ketuk = ketuk
        self.waktu = waktu

    def buka(self):
        if self.ketuk>=3:
            print(" pintu " + self.nama + " terbuka.")
        elif self.ketuk<=2:
            print(" mohon " + self.nama + " untuk mengetuk kembali")
        else :
              print(" pintu " + self.nama + " terbuka.")

    def tutup(self):
        if self.waktu >= 10:
            print("pintu " + self.nama + " tertutup.")
        else :
            print("pintu akan segera ditutup")
            print(".\n.\n.\n.\n.\n.\n.\n.")
            print("pintu " + self.nama + " tertutup.")
