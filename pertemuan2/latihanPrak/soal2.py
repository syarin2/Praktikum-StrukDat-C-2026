barang = ("B001", "Laptop Gaming", 15000000)

harga_barang = barang[2]
print("Harga barang:", harga_barang)

# 2. Mencoba mengubah harga (akan error)
# barang[2] = 14000000
# ERROR karena tuple bersifat IMMUTABLE (tidak bisa diubah setelah dibuat)
# Jadi elemen di dalam tuple tidak bisa diganti seperti list

try:
    barang[2] = 14000000
except TypeError as e:
    print(f"\n[ERROR] Tidak bisa mengubah isi tuple! Pesan error: {e}")

# 3. Unpacking tuple
kode, nama, harga = barang

print("\nHasil Unpacking:")
print("Kode:", kode)
print("Nama:", nama)
print("Harga:", harga)