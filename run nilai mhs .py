import json

nama_file = "nilai mhs .json"

#Membaca data dari file nilai mhs .json
with open(nama_file, "r", encoding="utf-8") as f:
    data = json.load(f)


while True:
    print("=====Sistem Pencatatan Nilai Mahasiswa=====")
    print("1. Lihat Histori Nilai")
    print("2. Tambah Nilai Mahasiswa")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    #Percabangan untuk mengeksekusi pilihan pengguna
    if pilihan == "1":

        #Membaca data dari file nilai mhs .json
        try:
            file = open(nama_file, "r") #Membuka file untuk dibaca
            data = json.load(file) #Memuat data dari file JSON
            file.close() #Menutup file setelah selesai membaca

            print("\n=== HISTORI NILAI MAHASISWA ===")

            #Mengecek apakah data nilai kosong
            if len(data) == 0:
                print("Belum ada data nilai.")

            #Menampilkan data nilai
            else:
                for nilai in data:
                    print("Nama        :", nilai["nama"])
                    print("Mata Kuliah :", nilai["mata_kuliah"])
                    print("Nilai       :", nilai["nilai"])
                    print("-----------------------------")

        #Mengatasi kasus kalau file tidak ditemukan
        except FileNotFoundError:
            print("File nilai belum tersedia.")

    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa: ")
        mata_kuliah = input("Masukkan mata kuliah: ")
        nilai = input("Masukkan nilai: ")

        #Menambahkan data nilai mahasiswa ke dalam list
        data.append({
            "nama": nama,
            "mata_kuliah": mata_kuliah,
            "nilai": nilai
        })

        #Menyimpan data nilai mahasiswa ke dalam file nilai mhs .json
        with open(nama_file, "w") as file: # Membuka file untuk ditulis
            json.dump(data, file, indent=4) # Menulis data ke file JSON dengan format yang rapi

        print("Data nilai mahasiswa berhasil ditambahkan.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem ini.")
        break

    else:
        print("Pilihan hanya 1/2/3, silakan coba lagi boskuh.")