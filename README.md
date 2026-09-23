# Laporan Praktikum PBO - Posttest 1
**Nama:** Kirana Cinta Mentari  
**NIM:** 2509106106  
**Kelas:** Informatika C1'25 

---

## 1. Penjelasan Program
Program ini merupakan **Sistem Penyewaan Sound System** di Kota Samarinda berbasis *Object-Oriented Programming* (OOP) dalam bahasa Python. Program ini mengelola data pelanggan, inventaris peralatan sound system, serta transaksi penyewaan yang menghubungkan pelanggan dan peralatan.

---

## 2. Struktur Class & Konsep OOP

Program ini terdiri dari **3 Class Utama** sesuai dengan modul 1–3:

### A. Class `Pelanggan`
- **Atribut Kelas:** `nama_usaha`, `kota`, `jumlah_pelanggan`
- **Atribut Instance:**
  - Public: `nama`, `no_hp`
  - Private: `__alamat`
- **Method:**
  - *Instance Method:* `tampilkan_data()`
  - *Class Method:* `buat_pelanggan(cls, nama, no_hp)` (Factory Method)
  - *Static Method:* `cek_no_hp(no_hp)` (Utility pengecekan angka)
- **Getter & Setter (`@property`):**
  - Getter: `alamat`
  - Setter: `alamat` (dengan validasi: *alamat tidak boleh kosong*)

### B. Class `Peralatan`
- **Atribut Kelas:** `nama_usaha`, `kota`, `jumlah_peralatan`
- **Atribut Instance:**
  - Public: `nama`, `harga`
  - Private: `__stok`
- **Method:**
  - *Instance Method:* `tampilkan_data()`, `tambah_stok(jumlah)`
  - *Class Method:* `buat_peralatan(cls, nama, harga, stok)`
  - *Static Method:* `hitung_harga(harga, hari)`
- **Getter & Setter (`@property`):**
  - Getter: `stok`
  - Setter: `stok` (dengan validasi: *stok tidak boleh negatif*)

### C. Class `Penyewaan`
- **Atribut Kelas:** `nama_usaha`, `kota`, `jumlah_penyewaan`
- **Atribut Instance:**
  - Public: `pelanggan`, `peralatan`, `hari`
  - Private: `__total`
- **Method:**
  - *Instance Method:* `hitung_total()`, `tampilkan_data()`
  - *Class Method:* `buat_penyewaan(cls, pelanggan, peralatan, hari)`
  - *Static Method:* `cek_hari(hari)`
- **Getter & Setter (`@property`):**
  - Getter: `total`
  - Setter: `total` (dengan validasi: *total tidak boleh negatif*)

---

## 3. Panduan Pengujian & Jalankan Program

### Cara Menjalankan Program
1. Pastikan Python 3.x telah terinstal di komputer/laptop.
2. Buka Terminal / Command Prompt pada folder proyek.
3. Jalankan perintah berikut:
   ```bash
   python posttest1.py
