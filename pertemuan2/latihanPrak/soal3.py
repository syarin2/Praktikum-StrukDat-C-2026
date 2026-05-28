tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# 1. Irisan (skill yang dimiliki kedua tim)
irisan = tim_frontend.intersection(tim_backend)
print("Keahlian yang dimiliki kedua tim (Irisan):", irisan)

# 2. Skill yang hanya dimiliki tim_backend
backend_only = tim_backend.difference(tim_frontend)
print("Keahlian yang hanya dimiliki tim_backend:", backend_only)

# 3. Gabungan semua skill unik
gabungan = tim_frontend.union(tim_backend)
print("Total keahlian unik di perusahaan (Gabungan):", gabungan)

