import math

class BangunRuang:
    def __init__(self):
        pass

    def luas(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi ** 2

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__()
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari ** 2

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi
    
class Kerucut(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        sisi_samping = math.sqrt(self.jari_jari ** 2 + self.tinggi ** 2)
        return math.pi * self.jari_jari * (self.jari_jari + sisi_samping)

    def volume(self):
        return (1/3) * math.pi * self.jari_jari ** 2 * self.tinggi

# Informasi Nama dan NIM
nama = "Zahwa Nur Azkia Putri"
nim = "064002300038"
print("Nama:", nama)
print("NIM:", nim)
print("============")

# Membuat objek Kubus
kubus1 = Kubus(5)
print("Luas kubus:", kubus1.luas())
print("Volume kubus:", kubus1.volume())

# Membuat objek Balok
balok1 = Balok(3, 4, 5)
print("Luas balok:", balok1.luas())
print("Volume balok:", balok1.volume())

# Membuat objek Bola
bola1 = Bola(5)
print("Luas bola:", bola1.luas())
print("Volume bola:", bola1.volume())

# Membuat objek Tabung
tabung1 = Tabung(3, 5)
print("Luas tabung:", tabung1.luas())
print("Volume tabung:", tabung1.volume())

# Membuat objek Kerucut
kerucut1 = Kerucut(4, 6)
print("Luas kerucut:", kerucut1.luas())
print("Volume kerucut:", kerucut1.volume())
