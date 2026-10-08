total_awal = int(input("Masukkan total belanja awal: "))

if total_awal % 100000 == 0:
    diskon = 1.0  
else:
    if total_awal % 50000 == 0:
        diskon = 0.50 
    else:
        if total_awal % 10000 == 0:
            diskon = 0.20
        else:
            if total_awal >= 200000:
                diskon = 0.10
            else:
                diskon = 0.0 


total_akhir = int(total_awal * (1 - diskon))


poin = "Poin Bertambah" if total_akhir > 0 else "Tidak Ada Poin"


print("Total Belanja Awal : Rp", total_awal)
print("Total Harga Akhir  : Rp", total_akhir)
print("Status Poin        :", poin)