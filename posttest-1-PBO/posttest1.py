class Pelanggan:
    nama_usaha = "Sewa Sound"
    kota = "Samarinda"
    jumlah_pelanggan = 0

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.__alamat = ""
        Pelanggan.jumlah_pelanggan += 1

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No HP:", self.no_hp)
        print("Alamat:", self.__alamat)

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, alamat):
        if alamat == "":
            raise ValueError("Alamat tidak boleh kosong")
        self.__alamat = alamat

    @classmethod
    def buat_pelanggan(cls, nama, no_hp):
        return cls(nama, no_hp)

    @staticmethod
    def cek_no_hp(no_hp):
        return no_hp.isdigit()


class Peralatan:
    nama_usaha = "Sewa Sound"
    kota = "Samarinda"
    jumlah_peralatan = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.__stok = stok
        Peralatan.jumlah_peralatan += 1

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Harga:", self.harga)
        print("Stok:", self.__stok)

    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__stok = stok

    @classmethod
    def buat_peralatan(cls, nama, harga, stok):
        return cls(nama, harga, stok)

    @staticmethod
    def hitung_harga(harga, hari):
        return harga * hari


class Penyewaan:
    nama_usaha = "Sewa Sound"
    kota = "Samarinda"
    jumlah_penyewaan = 0

    def __init__(self, pelanggan, peralatan, hari):
        self.pelanggan = pelanggan
        self.peralatan = peralatan
        self.hari = hari
        self.__total = 0
        Penyewaan.jumlah_penyewaan += 1

    def hitung_total(self):
        self.__total = self.peralatan.harga * self.hari

    def tampilkan_data(self):
        print("Pelanggan:", self.pelanggan.nama)
        print("Peralatan:", self.peralatan.nama)
        print("Lama sewa:", self.hari, "hari")
        print("Total:", self.__total)

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        if total < 0:
            raise ValueError("Total tidak boleh negatif")
        self.__total = total

    @classmethod
    def buat_penyewaan(cls, pelanggan, peralatan, hari):
        return cls(pelanggan, peralatan, hari)

    @staticmethod
    def cek_hari(hari):
        return hari > 0


# --- DEMO PROGRAM ---
print("SISTEM PENYEWAAN SOUND SYSTEM")
print("KOTA SAMARINDA")
print()

pelanggan1 = Pelanggan("Andi", "081234567890")
pelanggan2 = Pelanggan("Siti", "082345678901")
pelanggan1.alamat = "Jl. Juanda"
pelanggan2.alamat = "Jl. Pramuka"

pelanggan1.tampilkan_data()
print()
pelanggan2.tampilkan_data()

print("Jumlah pelanggan:", Pelanggan.jumlah_pelanggan)
print("Nomor HP valid:", Pelanggan.cek_no_hp(pelanggan1.no_hp))

pelanggan3 = Pelanggan.buat_pelanggan("Budi", "083456789012")
print()
pelanggan3.tampilkan_data()

alat1 = Peralatan("Speaker", 500000, 5)
alat2 = Peralatan("Mixer", 300000, 3)
print()
alat1.tampilkan_data()
print()
alat2.tampilkan_data()

alat1.tambah_stok(2)
print("Stok speaker:", alat1.stok)
print("Harga 3 hari:", Peralatan.hitung_harga(500000, 3))

alat3 = Peralatan.buat_peralatan("Microphone", 150000, 4)
print()
alat3.tampilkan_data()

sewa1 = Penyewaan(pelanggan1, alat1, 3)
sewa2 = Penyewaan(pelanggan2, alat2, 2)
sewa1.hitung_total()
sewa2.hitung_total()
print()
sewa1.tampilkan_data()
print()
sewa2.tampilkan_data()

print("Jumlah penyewaan:", Penyewaan.jumlah_penyewaan)
print("Lama sewa valid:", Penyewaan.cek_hari(3))

sewa3 = Penyewaan.buat_penyewaan(pelanggan1, alat3, 2)
sewa3.hitung_total()
print()
sewa3.tampilkan_data()

alat1.stok = 7
print("Stok setelah diubah:", alat1.stok)
sewa1.total = 1000000
print("Total setelah diubah:", sewa1.total)
pelanggan1.alamat = "Jl. P. Antasari"
print("Alamat setelah diubah:", pelanggan1.alamat)

# Uji Validasi (Error Handling)
try:
    alat1.stok = -2
except ValueError as e:
    print(e)

try:
    pelanggan1.alamat = ""
except ValueError as e:
    print(e)

try:
    sewa1.total = -500000
except ValueError as e:
    print(e)