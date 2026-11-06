def hitung(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hitung(n - 1) + hitung(n - 2)

hari = int(input("Masukkan hari ke-N: "))

if hari <= 0:
    print("Masukkan angka positif yang lebih besar dari 0!")
else:
    hasil = hitung(hari)
    print("Jumlah pelanggan pada hari ke-", hari, "adalah:", hasil)

