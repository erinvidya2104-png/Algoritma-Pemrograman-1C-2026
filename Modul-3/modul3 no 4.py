print("=== PROGRAM SELEKSI BEASISWA ===")

penerima_penuh = 0
penerima_sebagian = 0
tidak_lolos = 0
i = 1

while i <= 10 and penerima_penuh < 3:
    print()
    print("Data Mahasiswa ke-", i)
    nama = input("Nama (0 untuk selesai): ")
    
    if nama == "0":
        break
        
    ipk = float(input("IPK: "))
    
    if ipk < 3.00:
        print("Tidak memenuhi syarat (IPK < 3.00)")
        tidak_lolos = tidak_lolos + 1
    else:
        penghasilan = float(input("Penghasilan Orang Tua: Rp "))
        
        if penghasilan <= 3000000:
            print("Dapat Beasiswa Penuh")
            penerima_penuh = penerima_penuh + 1
        elif penghasilan <= 5000000:
            print("Dapat Beasiswa Sebagian")
            penerima_sebagian = penerima_sebagian + 1
        else:
            print("Tidak mendapat beasiswa")
            tidak_lolos = tidak_lolos + 1
            
    i = i + 1

print()
print("=== HASIL AKHIR ===")
print("Penerima Penuh   :", penerima_penuh)
print("Penerima Sebagian:", penerima_sebagian)
print("Tidak Lolos  :", tidak_lolos)
