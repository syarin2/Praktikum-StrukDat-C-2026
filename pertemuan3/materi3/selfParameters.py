class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()


#example
class Car:
  def __init__(self, brand):
    self.brand = brand

  def show(self):
    print(self.brand)

c1 = Car("Ford")
c1.show()

class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    # Menggunakan 'self' di dalam method untuk mengambil data objek tersebut
    def cetak_info(self):
        print(f"Mobil ini adalah {self.merek} berwarna {self.warna}")

# Eksperimen dengan dua objek berbeda
mobil_a = Mobil("Toyota", "Hitam")
mobil_b = Mobil("Honda", "Putih")

mobil_a.cetak_info()  # Output: Mobil ini adalah Toyota berwarna Hitam
mobil_b.cetak_info()  # Output: Mobil ini adalah Honda berwarna Putih