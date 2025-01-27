# Fungsi untuk menyimpan hasil pengurutan ke file txt
def simpan_ke_file(data):
    with open("hasil_pengurutan.txt", "w") as file:
        file.write(", ".join(map(str, data)))

# Fungsi untuk membaca hasil pengurutan dari file txt
def baca_dari_file():
    try:
        with open("hasil_pengurutan.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File hasil_pengurutan.txt tidak ditemukan!"

# Fungsi utama untuk menampilkan menu dan menangani pilihan pengguna
def menu():
    data = []
    while True:
        print("\nMENU PILIHAN")
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")
        pilihan = input("Masukkan pilihan [1/2/3]: ")

        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah angka yang akan diinput: "))
                data = []

                for i in range(jumlah):
                    angka = int(input(f"Angka {i+1}: "))
                    data.append(angka)

                data.sort()
                simpan_ke_file(data)

                print("\nData berhasil diurutkan dan disimpan ke file.")
            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilihan == "2":
            print("\nTAMPIL HASIL PENGURUTAN")
            print("Nilai tugas:", baca_dari_file())

        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Coba lagi!")

if __name__ == "__main__":
    menu()
