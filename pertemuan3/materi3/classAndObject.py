class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

del p1

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Person:
  pass

#example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("John", 36)
p1.greet()

class Mahasiswa:
    # Constructor untuk inisialisasi properti/atribut
    def __init__(self, nama, nim):
        self.nama = nama  # Properti Nama
        self.nim = nim    # Properti NIM

# Membuat Object (Realisasi dari Class)
mhs1 = Mahasiswa("Ahmad", "2307112001")
mhs2 = Mahasiswa("Siti", "2307112002")

# Mengakses properti object
print(mhs1.nama)  # Output: Ahmad
print(mhs2.nim)   # Output: 2307112002