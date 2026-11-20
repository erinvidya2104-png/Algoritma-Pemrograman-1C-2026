print("MENGELOLA NILAI MAHASISWA")

total_nilai_kelas = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

for i in range(1, 11):
    print()
    print("Mahasiswa ke-", i)
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    
    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a = jumlah_a + 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_b = jumlah_b + 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c = jumlah_c + 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d = jumlah_d + 1
    else:
        kategori = "E"
        jumlah_e = jumlah_e + 1
        
    print("Nilai Akhir:", nilai_akhir, "| Kategori:", kategori)
    
    total_nilai_kelas = total_nilai_kelas + nilai_akhir
    
    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama
        
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

rata_rata_kelas = total_nilai_kelas / 10

print("=== LAPORAN AKHIR ===")
print("Jumlah A:", jumlah_a)
print("Jumlah B:", jumlah_b)
print("Jumlah C:", jumlah_c)
print("Jumlah D:", jumlah_d)
print("Jumlah E:", jumlah_e)
print("Tertinggi:", nilai_tertinggi, "oleh", nama_tertinggi)
print("Terendah:", nilai_terendah, "oleh", nama_terendah)
print("Rata-rata Kelas:", rata_rata_kelas)