class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet


#example
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

r1 = Rectangle(5, 3)
print(r1.area())

class AkunBank:
    total_nasabah = 0  # Class Property

    def __init__(self, nama_pemilik):
        self.nama_pemilik = nama_pemilik  # Instance Property
        # Setiap ada objek baru dibuat, total nasabah bertambah
        AkunBank.total_nasabah += 1 

    # 1. Instance Method (Butuh data spesifik objek)
    def sapa_nasabah(self):
        print(f"Halo Selamat Datang, Kak {self.nama_pemilik}!")

    # 2. Class Method (Mengolah data level Class global)
    @classmethod
    def tampilkan_total_nasabah(cls):
        print(f"Total nasabah aktif saat ini: {cls.total_nasabah}")


# --- Cara Penggunaan ---
nasabah1 = AkunBank("Rian")
nasabah2 = AkunBank("Dewi")

# Memanggil Instance Method
nasabah1.sapa_nasabah()  # Output: Halo Selamat Datang, Kak Rian!

# Memanggil Class Method (bisa langsung lewat Class-nya tanpa bikin objek baru)
AkunBank.tampilkan_total_nasabah()  # Output: Total nasabah aktif saat ini: 2