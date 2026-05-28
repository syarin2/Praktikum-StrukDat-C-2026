ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

coding_only = ukm_coding.difference(ukm_robotik)
print("Hanya mendaftar UKM Coding:", coding_only)

total_mahasiswa = ukm_coding.union(ukm_robotik)
print("Daftar seluruh mahasiswa unik:", total_mahasiswa)

is_andi_robotik = "Andi" in ukm_robotik
print("Apakah Andi anggota UKM Robotik?:", is_andi_robotik)

