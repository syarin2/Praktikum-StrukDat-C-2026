class JadwalKuliah:
    def __init__(self, namaSiswa, jenisPelajaran, tingkatKesulitan):
        self.namaSiswa = namaSiswa
        self.jenisPelajaran = jenisPelajaran
        self.tingkatKesulitan = tingkatKesulitan

    def memperkenalkan_diri(self):
        print(f"Halo nama saya {self.namaSiswa}, saya suka pelajaran {self.jenisPelajaran}")

    def change_jenisPelajaran(self, new_jenisPelajaran):
        self.jenisPelajaran = new_jenisPelajaran

#object
mp1 = JadwalKuliah("Syarin", "Kalkulus", "Sulit")
mp2 = JadwalKuliah("Fira", "Pemograman", "Mudah")
mp3 = JadwalKuliah("Celsi", "StrukturData", "Sulit")

print("--- Status Awal Mahasiswa ---")
mp1.memperkenalkan_diri()
mp2.memperkenalkan_diri()
mp3.memperkenalkan_diri()

print("\n--- Perubahan Atribut Objek ---")
#Mengubah salah satu atribut
print(f"Awalnya {mp1.namaSiswa} mengambil pelajaran: {mp1.jenisPelajaran}")

# Memanggil method untuk mengubah isi atribut
mp1.change_jenisPelajaran("Algoritma Pemrograman")

print(f"Sekarang {mp1.namaSiswa} mengganti pelajarannya menjadi: {mp1.jenisPelajaran}")

print("\n--- Status Akhir Setelah Perubahan ---")
mp1.memperkenalkan_diri()