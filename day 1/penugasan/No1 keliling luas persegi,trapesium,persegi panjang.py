# ========================
# FUNGSI PERSEGI
# ========================
def hitung_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    return keliling, luas


# ========================
# FUNGSI PERSEGI PANJANG
# ========================
def hitung_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return keliling, luas


# ========================
# FUNGSI TRAPESIUM
# ========================
def hitung_trapesium(a, b, c, d, tinggi):
    keliling = a + b + c + d
    luas = 0.5 * (a + b) * tinggi
    return keliling, luas


# ========================
# DATA ANGKA (SUDAH DITENTUKAN)
# ========================

# Persegi (sisi = 4)
k_persegi, l_persegi = hitung_persegi(4)

# Persegi Panjang (panjang = 8, lebar = 3)
k_pp, l_pp = hitung_persegi_panjang(8, 3)

# Trapesium (a=6, b=10, c=5, d=5, tinggi=4)
k_trap, l_trap = hitung_trapesium(6, 10, 5, 5, 4)


# ========================
# OUTPUT
# ========================

print("=== PERSEGI ===")
print("Keliling:", k_persegi)
print("Luas:", l_persegi)

print("\n=== PERSEGI PANJANG ===")
print("Keliling:", k_pp)
print("Luas:", l_pp)

print("\n=== TRAPESIUM ===")
print("Keliling:", k_trap)
print("Luas:", l_trap)