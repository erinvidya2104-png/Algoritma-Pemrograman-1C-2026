print("PROGRAM KASIR BUS SIDOARJO")

total_pendapatan = 0
jumlah_penumpang = 0
jarak_terjauh = 0
total_jarak = 0

jarak = int(input("Masukkan jarak tempuh (0 untuk berhenti): "))

while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid!")
    else:
        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
        else:
            tarif = 13000 + (jarak - 15) * 500
        
        jumlah_penumpang = jumlah_penumpang + 1 
       
        if jumlah_penumpang % 5 == 0:
            tarif = tarif * 0.5
            print("Anda mendapat diskon 50%!")
            
        print("Tarif yang harus dibayar: Rp", tarif)
        
        total_pendapatan = total_pendapatan + tarif
        total_jarak = total_jarak + jarak
        
        if jarak > jarak_terjauh:
            jarak_terjauh = jarak
            
    jarak = float(input("Masukkan jarak tempuh berikutnya (0 untuk berhenti): "))

print("--- LAPORAN AKHIR ---")
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Rata-rata jarak:", rata_rata, "km")
else:
    print("Rata-rata jarak: 0 km")