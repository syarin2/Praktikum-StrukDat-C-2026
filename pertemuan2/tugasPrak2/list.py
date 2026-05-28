# list
data = ["Anggur", "Apel", "Pir"]
print("List:", data)

thislist = ["apple", "banana", "cherry"]
print(thislist)

data.append("Go")
print("Setelah tambah:", data)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

# 4. Mengubah Data
colors = ["red", "green", "blue"]
colors[1] = "yellow"
colors.append("purple")

print("Setelah diubah:", colors)
print("Jumlah isi:", len(colors))

colors.remove("red")
print("Setelah hapus:", colors)

print("Isi List:")
for item in colors:
    print(item)
