from abc import ABC, abstractmethod


class Peralatan(ABC):
    def __init__(self, nama, harga_sewa):
        self.nama = nama
        self._harga_sewa = harga_sewa

    @abstractmethod
    def informasi(self):
        pass

    @abstractmethod
    def hitung_biaya(self, durasi):
        pass

    def tampilkan(self):
        print(f"Peralatan: {self.nama}")
        print(f"Harga sewa per hari: Rp{self._harga_sewa}")


class Speaker(Peralatan):
    def __init__(self, nama, harga_sewa, daya):
        super().__init__(nama, harga_sewa)
        self.daya = daya

    def informasi(self):
        return f"{self.nama}, daya {self.daya} watt"

    def hitung_biaya(self, durasi):
        return self._harga_sewa * durasi


class Mikrofon(Peralatan):
    def __init__(self, nama, harga_sewa, jenis):
        super().__init__(nama, harga_sewa)
        self.jenis = jenis

    def informasi(self):
        return f"{self.nama}, jenis {self.jenis}"

    def hitung_biaya(self, durasi):
        return self._harga_sewa * durasi


class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

    def informasi(self):
        return f"Pelanggan: {self.nama}"


class Pembayaran:
    def __init__(self, total):
        self.__total = total

    def __str__(self):
        return f"Total pembayaran: Rp{self.__total}"


class Penyewaan:
    def __init__(self, pelanggan, peralatan, durasi):
        # Asosiasi: pelanggan dibuat terpisah dan diberikan ke Penyewaan.
        self.pelanggan = pelanggan

        # Agregasi: daftar peralatan berasal dari luar Penyewaan.
        self.peralatan = list(peralatan)
        self.durasi = durasi

        total = sum(alat.hitung_biaya(durasi) for alat in self.peralatan)

        # Komposisi: objek Pembayaran dibuat dan dimiliki oleh Penyewaan.
        self.__pembayaran = Pembayaran(total)

    def tampilkan(self):
        print(self.pelanggan.informasi())
        print(f"Durasi sewa: {self.durasi} hari")
        print("Daftar peralatan:")
        for alat in self.peralatan:
            print("-", alat.informasi())
        print(self.__pembayaran)


class Keranjang:
    def __init__(self):
        self.daftar = []

    def tambah(self, peralatan):
        self.daftar.append(peralatan)

    def __add__(self, peralatan):
        self.tambah(peralatan)
        return self

    def __len__(self):
        return len(self.daftar)


def tampilkan_informasi(objek):
    # Duck typing: cukup memiliki method informasi().
    print(objek.informasi())


if __name__ == "__main__":
    print("=== BUKTI ABSTRAKSI ===")
    try:
        Peralatan("Peralatan", 100000)
    except TypeError as error:
        print("Peralatan tidak dapat dibuat menjadi objek.")
        print("Pesan:", error)

    print("\n=== POLIMORFISME PEWARISAN ===")
    daftar_peralatan = [
        Speaker("Speaker JBL", 150000, 500),
        Mikrofon("Mikrofon Shure", 50000, "Wireless")
    ]

    for alat in daftar_peralatan:
        alat.tampilkan()
        print(alat.informasi())
        print(f"Biaya 2 hari: Rp{alat.hitung_biaya(2)}")
        print()

    print("=== DUCK TYPING ===")
    pelanggan = Pelanggan("Kirana")
    speaker = daftar_peralatan[0]
    tampilkan_informasi(pelanggan)
    tampilkan_informasi(speaker)

    print("\n=== OPERATOR OVERLOADING ===")
    keranjang = Keranjang()
    keranjang + daftar_peralatan[0]
    keranjang + daftar_peralatan[1]
    print("Jumlah peralatan:", len(keranjang))

    print("\n=== RELASI KELAS ===")
    penyewaan = Penyewaan(pelanggan, daftar_peralatan, 2)
    penyewaan.tampilkan()
