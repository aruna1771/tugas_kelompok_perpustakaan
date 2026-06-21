class Buku:
    def __init__(self, kodeBuku, judul, penulis, tahunTerbit, stok):
        self.kodeBuku = kodeBuku
        self.judul = judul
        self.penulis = penulis
        self.tahunTerbit = tahunTerbit
        self.stok = max(0, stok)

    def tampilInfo(self):
        print(
            f"{self.kodeBuku} | "
            f"{self.judul} | "
            f"{self.penulis} | "
            f"{self.tahunTerbit} | "
            f"Stok: {self.stok}"
        )


class BukuPelajaran(Buku):
    def __init__(self, kodeBuku, judul, penulis,
                 tahunTerbit, stok, mataPelajaran):
        super().__init__(
            kodeBuku,
            judul,
            penulis,
            tahunTerbit,
            stok
        )
        self.mataPelajaran = mataPelajaran

    def tampilInfo(self):
        print(
            f"[Buku Pelajaran] "
            f"{self.kodeBuku} | "
            f"{self.judul} | "
            f"{self.penulis} | "
            f"{self.tahunTerbit} | "
            f"Stok: {self.stok} | "
            f"Mata Pelajaran: {self.mataPelajaran}"
        )


class Novel(Buku):
    def __init__(self, kodeBuku, judul, penulis,
                 tahunTerbit, stok, genre):
        super().__init__(
            kodeBuku,
            judul,
            penulis,
            tahunTerbit,
            stok
        )
        self.genre = genre

    def tampilInfo(self):
        print(
            f"[Novel] "
            f"{self.kodeBuku} | "
            f"{self.judul} | "
            f"{self.penulis} | "
            f"{self.tahunTerbit} | "
            f"Stok: {self.stok} | "
            f"Genre: {self.genre}"
        )


class Majalah(Buku):
    def __init__(self, kodeBuku, judul, penulis,
                 tahunTerbit, stok, edisi):
        super().__init__(
            kodeBuku,
            judul,
            penulis,
            tahunTerbit,
            stok
        )
        self.edisi = edisi

    def tampilInfo(self):
        print(
            f"[Majalah] "
            f"{self.kodeBuku} | "
            f"{self.judul} | "
            f"{self.penulis} | "
            f"{self.tahunTerbit} | "
            f"Stok: {self.stok} | "
            f"Edisi: {self.edisi}"
        )


class Keanggotaan:
    def __init__(self):
        self.anggota = [
            {"id": "A001", "nama": "Andi", "tipe": "Pelajar", "max_hari": 7},
            {"id": "A002", "nama": "Budi", "tipe": "Umum", "max_hari": 14},
            {"id": "A003", "nama": "Citra", "tipe": "Dosen", "max_hari": 30}
        ]

    def tampilAnggota(self):
        print("\n===== DAFTAR ANGGOTA =====")
        for i, a in enumerate(self.anggota, 1):
            print(
                f"{i}. {a['id']} | "
                f"{a['nama']} | "
                f"{a['tipe']} | "
                f"Maks {a['max_hari']} hari"
            )

    def tambahAnggota(self):
        idA = input("ID Anggota : ")
        nama = input("Nama       : ")
        tipe = input("Tipe       : ")

        while True:
            try:
                maxHari = int(input("Max Hari Pinjam : "))
                break
            except:
                print("Input harus angka!")

        self.anggota.append({
            "id": idA,
            "nama": nama,
            "tipe": tipe,
            "max_hari": maxHari
        })

        print("Anggota berhasil ditambahkan.")

    def hapusAnggota(self):
        self.tampilAnggota()

        try:
            nomor = int(input("Nomor yang dihapus : "))
            self.anggota.pop(nomor - 1)
            print("Anggota berhasil dihapus.")
        except:
            print("Data tidak valid.")

    def cariAnggota(self, idAnggota):
        for a in self.anggota:
            if a["id"] == idAnggota:
                return a
        return None


class Peminjaman:
    def __init__(self, keanggotaan):
        self.keanggotaan = keanggotaan
        self.dataPinjam = []

    def pinjamBuku(self, daftarBuku):

        idAnggota = input("ID Anggota : ")

        anggota = self.keanggotaan.cariAnggota(idAnggota)

        if anggota is None:
            print("Anggota tidak ditemukan!")
            return

        tampilSemuaBuku(daftarBuku)

        try:
            nomor = int(input("Nomor Buku : "))
        except:
            print("Input salah!")
            return

        if nomor < 1 or nomor > len(daftarBuku):
            print("Nomor tidak valid!")
            return

        buku = daftarBuku[nomor - 1]

        if buku.stok <= 0:
            print("Stok habis!")
            return

        durasi = int(
            input(
                f"Durasi pinjam (maks {anggota['max_hari']} hari): "
            )
        )

        if durasi > anggota["max_hari"]:
            print("Melebihi batas peminjaman!")
            return

        buku.stok -= 1

        self.dataPinjam.append({
            "anggota": anggota["nama"],
            "judul": buku.judul,
            "durasi": durasi,
            "objek": buku
        })

        print("Peminjaman berhasil!")

    def tampilPinjaman(self):
        print("\n===== DATA PEMINJAMAN =====")

        if not self.dataPinjam:
            print("Belum ada peminjaman.")
            return

        for i, p in enumerate(self.dataPinjam, 1):
            print(
                f"{i}. "
                f"{p['anggota']} | "
                f"{p['judul']} | "
                f"{p['durasi']} hari"
            )

    def kembalikanBuku(self):

        self.tampilPinjaman()

        if not self.dataPinjam:
            return

        try:
            nomor = int(
                input("Nomor yang dikembalikan : ")
            )

            data = self.dataPinjam.pop(nomor - 1)

            data["objek"].stok += 1

            print("Buku berhasil dikembalikan.")

        except:
            print("Data tidak valid.")


def tampilSemuaBuku(daftarBuku):
    print("\n===== DAFTAR BUKU =====")

    for i, buku in enumerate(daftarBuku, 1):
        print(f"{i}. ", end="")
        buku.tampilInfo()


def cariBuku(daftarBuku):
    keyword = input("Masukkan judul : ").lower()

    ditemukan = False

    for buku in daftarBuku:
        if keyword in buku.judul.lower():
            buku.tampilInfo()
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan.")


def sortingBuku(daftarBuku):
    daftarBuku.sort(key=lambda x: x.judul.lower())
    print("Data berhasil diurutkan berdasarkan judul.")


def tambahBuku(daftarBuku):

    print("\n1. Buku Pelajaran")
    print("2. Novel")
    print("3. Majalah")

    jenis = input("Pilih jenis : ")

    kode = input("Kode Buku : ")
    judul = input("Judul : ")
    penulis = input("Penulis : ")

    tahun = int(input("Tahun Terbit : "))

    while True:
        stok = int(input("Stok : "))

        if stok < 0:
            print("Stok tidak boleh negatif!")
        else:
            break

    if jenis == "1":

        mapel = input("Mata Pelajaran : ")

        daftarBuku.append(
            BukuPelajaran(
                kode,
                judul,
                penulis,
                tahun,
                stok,
                mapel
            )
        )

    elif jenis == "2":

        genre = input("Genre : ")

        daftarBuku.append(
            Novel(
                kode,
                judul,
                penulis,
                tahun,
                stok,
                genre
            )
        )

    elif jenis == "3":

        edisi = input("Edisi : ")

        daftarBuku.append(
            Majalah(
                kode,
                judul,
                penulis,
                tahun,
                stok,
                edisi
            )
        )

    else:
        print("Pilihan tidak valid!")
        return

    print("Buku berhasil ditambahkan.")

daftarBuku = [

    BukuPelajaran(
        "BP001",
        "Matematika Dasar",
        "Budi",
        2020,
        10,
        "Matematika"
    ),

    BukuPelajaran(
        "BP002",
        "Fisika Dasar",
        "Andi",
        2021,
        8,
        "Fisika"
    ),

    BukuPelajaran(
        "BP003",
        "Algoritma Pemrograman",
        "Rina",
        2022,
        5,
        "Informatika"
    ),

    Novel(
        "NV001",
        "Laskar Pelangi",
        "Andrea Hirata",
        2005,
        7,
        "Drama"
    ),

    Novel(
        "NV002",
        "Bumi",
        "Tere Liye",
        2014,
        6,
        "Fantasi"
    ),

    Novel(
        "NV003",
        "Dilan 1990",
        "Pidi Baiq",
        2014,
        4,
        "Romantis"
    ),

    Majalah(
        "MJ001",
        "National Geographic",
        "NG Team",
        2024,
        3,
        "Januari"
    ),

    Majalah(
        "MJ002",
        "Tempo",
        "Tempo Media",
        2024,
        5,
        "Februari"
    )
]

keanggotaan = Keanggotaan()
peminjaman = Peminjaman(keanggotaan)


while True:

    print("\n==============================")
    print(" SISTEM PERPUSTAKAAN")
    print("==============================")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Tampilkan Semua Buku")
    print("4. Urutkan Buku")
    print("5. Keanggotaan")
    print("6. Peminjaman")
    print("7. Pengembalian")
    print("8. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        tambahBuku(daftarBuku)

    elif pilihan == "2":
        cariBuku(daftarBuku)

    elif pilihan == "3":
        tampilSemuaBuku(daftarBuku)

    elif pilihan == "4":
        sortingBuku(daftarBuku)

    elif pilihan == "5":

        while True:

            print("\n=== KEANGGOTAAN ===")
            print("1. Tampilkan Anggota")
            print("2. Tambah Anggota")
            print("3. Hapus Anggota")
            print("4. Kembali")

            pilih = input("Pilih : ")

            if pilih == "1":
                keanggotaan.tampilAnggota()

            elif pilih == "2":
                keanggotaan.tambahAnggota()

            elif pilih == "3":
                keanggotaan.hapusAnggota()

            elif pilih == "4":
                break

    elif pilihan == "6":
        peminjaman.pinjamBuku(daftarBuku)

    elif pilihan == "7":
        peminjaman.kembalikanBuku()

    elif pilihan == "8":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")