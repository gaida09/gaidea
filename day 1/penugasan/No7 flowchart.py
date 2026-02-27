# Program Menghitung Gaji Bersih

# Input
nama = "Juju"
gaji_pokok = 5000000

# Proses
tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print("Nama           :", nama)
print("Gaji Pokok     :", gaji_pokok)
print("Gaji Bersih    :", gaji_bersih) 