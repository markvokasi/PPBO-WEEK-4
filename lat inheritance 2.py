class Orang:
    def __init__(self, namadpn, namablk, nomorID):
        self.namadpn = namadpn
        self.namablk = namablk
        self.nomorID = nomorID
    
    def tampilkan_info(self):
        print(f"Nama: {self.namadpn} {self.namablk}, ID: {self.nomorID}")

class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = range(3)
    Gelar_Jenjang = {SARJANA: "SARJANA", MASTER: "MASTER", DOKTOR: "DOKTOR"}
    
    def __init__(self, namadpn, namablk, nomorID, jenjang):
        super().__init__(namadpn, namablk, nomorID)
        self.jenjang = jenjang
        self.matkul = []
    
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenjang: {self.Gelar_Jenjang[self.jenjang]}")
        print(f"Mata Kuliah yang diambil: {', '.join(self.matkul)}")

class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)
    
    def __init__(self, namadpn, namablk, nomorID, status_karyawan):
        super().__init__(namadpn, namablk, nomorID)
        self.status_karyawan = status_karyawan
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Karyawan: {'Tetap' if self.status_karyawan == self.TETAP else 'Tidak Tetap'}")

class Dosen(Karyawan):
    def __init__(self, namadpn, namablk, nomorID, status_karyawan):
        super().__init__(namadpn, namablk, nomorID, status_karyawan)
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah yang diajar: {', '.join(self.matkul_diajar)}")

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")

riski = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
riski.mengajar("Statistik")

class Pelajar:
    def __init__(self):
        self.matkul = []
    
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)      

    def tampilkan_info(self):
        print(f"Mata Kuliah yang diambil: {', '.join(self.matkul)}")

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
    
    def tampilkan_info(self):
        print(f"Mata Kuliah yang diajar: {', '.join(self.matkul_diajar)}")

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, namadpn, namablk, nomorID):
        Orang.__init__(self, namadpn, namablk, nomorID)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah yang diambil: {', '.join(self.matkul)}")
        print(f"Mata Kuliah yang diajar: {', '.join(self.matkul_diajar)}")

uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

print("Mahasiswa")
bowo.tampilkan_info()

print("Dosen")
riski.tampilkan_info()

print("Asisten Dosen")
uswatun.tampilkan_info()
