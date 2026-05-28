# Data awal
nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

# 1. Tambahkan siswa baru
nilai_siswa["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90
}

# 2. Hitung nilai akhir
print("Nilai Akhir Siswa:")
for kode, data in nilai_siswa.items():
    tugas = data["tugas"]
    uts = data["uts"]
    uas = data["uas"]

    nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)
    print(f"Siswa: {data['nama']} | Nilai Akhir: {nilai_akhir:.2f}")

print("\n--- Siswa dengan Nilai UAS di atas 80 ---")

# 3. Tampilkan siswa dengan UAS > 80
print("\nSiswa dengan nilai UAS > 80:")
for kode, data in nilai_siswa.items():
    if data["uas"] > 80:
        print(f"- {data['nama']} (Nilai UAS: {data['uas']})")