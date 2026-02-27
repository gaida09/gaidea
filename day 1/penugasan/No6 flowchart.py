# Program Kelulusan Siswa (tanpa input manual)

while True:
    nilai_siswa = 60   # nilai pertama

    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        mengulang = "Ya"   # keputusan mengulang

        if mengulang.lower() == "ya":
            nilai_siswa = 80   # nilai setelah mengulang
            
            if nilai_siswa >= 75:
                print("Tuntas")
            else:
                print("Tidak Tuntas")
            break
        else:
            print("Tidak Tuntas")
            break
        