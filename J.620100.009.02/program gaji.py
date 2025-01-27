from datetime import datetime

class Pegawai:
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, jabatan):
        # Inisialisasi atribut dasar pegawai
        self.nip = nip
        self.nama = nama
        self.tahun_masuk = tahun_masuk
        self.gaji_pokok = gaji_pokok
        self.jabatan = jabatan

    def hitung_gaji(self):
        # Metode untuk menghitung gaji pokok
        return self.gaji_pokok

class Satpam(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, jam_lembur):
        # Menggunakan konstruktor kelas induk
        super().__init__(nip, nama, tahun_masuk, gaji_pokok, "Satpam")
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        # Gaji Satpam dengan tambahan honor lembur
        honor_lembur = self.jam_lembur * 20000
        return self.gaji_pokok + honor_lembur

class Sales(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, jumlah_pelanggan):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok, "Sales")
        self.jumlah_pelanggan = jumlah_pelanggan

    def hitung_gaji(self):
        # Gaji Sales dengan tambahan komisi dari jumlah pelanggan
        komisi = self.jumlah_pelanggan * 50000
        return self.gaji_pokok + komisi

class Administrasi(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, tahun_sekarang):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok, "Administrasi")
        self.lama_kerja = tahun_sekarang - tahun_masuk  # Menghitung lama kerja

    def hitung_gaji(self):
        # Tunjangan berdasarkan lama kerja
        if self.lama_kerja >= 5:
            tunjangan = self.gaji_pokok * 0.03
        elif self.lama_kerja >= 3:
            tunjangan = self.gaji_pokok * 0.01
        else:
            tunjangan = 0
        return self.gaji_pokok + tunjangan

class Manajer(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, peningkatan):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok, "Manajer")
        self.peningkatan = peningkatan

    def hitung_gaji(self):
        # Bonus berdasarkan peningkatan kinerja
        if self.peningkatan > 10:
            bonus = self.gaji_pokok * 0.1
        elif self.peningkatan >= 6:
            bonus = self.gaji_pokok * 0.05
        elif self.peningkatan >= 1:
            bonus = self.gaji_pokok * 0.02
        else:
            bonus = 0
        return self.gaji_pokok + bonus

def format_rupiah(angka):
    # Format angka ke dalam format Rupiah
    return f"Rp {angka:,.0f}".replace(",", ".")

def input_karyawan(jabatan):
    # Validasi jabatan
    if jabatan not in ["Administrasi", "Satpam", "Sales", "Manajer"]:
        print("Jabatan Tidak Valid")
        print("Jabatan Tersedia: Satpam, Sales, Administrasi, Manajer")
        return

    # Tentukan input tambahan berdasarkan jabatan
    arg_tambahan = "Masukkan Jam Lembur: "
    if jabatan == "Sales":
        arg_tambahan = "Masukkan Jumlah Pelanggan: "
    elif jabatan == "Manajer":
        arg_tambahan = "Masukkan Peningkatan Karyawan: "

    # Input data karyawan
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama Karyawan: ")
    tahun_masuk = int(input("Masukkan tahun masuk: "))
    gaji_pokok = int(input("Masukkan gaji pokok: "))

    if jabatan == "Administrasi":
        arg_tambahan_value = datetime.now().year
    else:
        arg_tambahan_value = int(input(arg_tambahan))

    # Inisialisasi objek pegawai berdasarkan jabatan
    if jabatan == "Administrasi":
        pegawai = Administrasi(nip, nama, tahun_masuk, gaji_pokok, arg_tambahan_value)
    elif jabatan == "Satpam":
        pegawai = Satpam(nip, nama, tahun_masuk, gaji_pokok, arg_tambahan_value)
    elif jabatan == "Sales":
        pegawai = Sales(nip, nama, tahun_masuk, gaji_pokok, arg_tambahan_value)
    elif jabatan == "Manajer":
        pegawai = Manajer(nip, nama, tahun_masuk, gaji_pokok, arg_tambahan_value)

    # Hitung dan tampilkan gaji
    gaji_pegawai = format_rupiah(pegawai.hitung_gaji())
    print("=====================")
    print(f"Gaji Akhir {pegawai.nama} adalah {gaji_pegawai}")

def menu():
    while True:
        # Tampilkan menu utama
        print("\nMENU PILIHAN")
        print("1. Cek Gaji Karyawan")
        print("2. Selesai")
        pilihan = input("Masukkan pilihan [1/2]: ")

        if pilihan == "1":
            print("Jabatan Tersedia: Satpam, Sales, Administrasi, Manajer")
            jabatan = input("Masukkan Jabatan karyawan: ")
            input_karyawan(jabatan)
        elif pilihan == "2":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
