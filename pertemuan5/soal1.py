stok_barang = [15, 40, 30, 10, 25]

indeks_10 = stok_barang.index(10)
stok_barang[indeks_10] = 50

stok_barang.append(5)
stok_barang.sort(reverse=True)

total_stok = sum(stok_barang)
print("List setelah diubah & diurutkan:", stok_barang)
print("Total seluruh nilai dalam list:", total_stok)

rata_rata = sum(stok_barang) / len(stok_barang)
status = "Stok Aman" if rata_rata > 20 else "Waspada"
print(f"Rata-rata: {rata_rata} -> Status: {status}")