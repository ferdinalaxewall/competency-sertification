# Program Penghitungan Gaji Karyawan

## Deskripsi
Program ini digunakan untuk menghitung gaji akhir karyawan berdasarkan jabatan mereka, dengan mempertimbangkan faktor-faktor seperti jam lembur, jumlah pelanggan, peningkatan kinerja, atau lama kerja.

## Jabatan yang Didukung
- **Satpam**: Mendapat tambahan honor dari jam lembur.
- **Sales**: Mendapat komisi berdasarkan jumlah pelanggan.
- **Administrasi**: Mendapat tunjangan berdasarkan lama kerja.
- **Manajer**: Mendapat bonus berdasarkan peningkatan kinerja.

## Cara Menggunakan Program
1. Jalankan program.
2. Pilih menu:
   - Pilih **1** untuk menghitung gaji karyawan.
   - Pilih **2** untuk keluar dari program.
3. Jika memilih opsi 1, masukkan jabatan karyawan (Satpam, Sales, Administrasi, Manajer).
4. Masukkan data karyawan:
   - **NIP**: Nomor Induk Pegawai.
   - **Nama**: Nama karyawan.
   - **Tahun Masuk**: Tahun mulai bekerja.
   - **Gaji Pokok**: Gaji dasar karyawan.
   - Data tambahan (berdasarkan jabatan):
     - Satpam: Jam lembur.
     - Sales: Jumlah pelanggan.
     - Administrasi: Tidak perlu data tambahan.
     - Manajer: Peningkatan kinerja.
5. Program akan menampilkan gaji akhir karyawan dalam format Rupiah.

## Contoh Output
```
MENU PILIHAN
1. Cek Gaji Karyawan
2. Selesai

Masukkan pilihan [1/2]: 1
Jabatan Tersedia: Satpam, Sales, Administrasi, Manajer
Masukkan Jabatan karyawan: Sales
Masukkan NIP: 12345
Masukkan Nama Karyawan: John Doe
Masukkan tahun masuk: 2015
Masukkan gaji pokok: 5000000
Masukkan Jumlah Pelanggan: 20
=====================
Gaji Akhir John Doe adalah Rp 6.000.000
```
