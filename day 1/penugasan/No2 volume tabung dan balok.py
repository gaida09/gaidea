import math 
r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi: "))

volume = math.pi * (r**2) * t
print(f"Volume Tabung: {volume:.2f}")



print("---Program Hitung Volume Balok ---")

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

volume = panjang * lebar * tinggi

print(f"\nHasil Perhitungan:")
print(f"Volume Balok adalah: {volume}")