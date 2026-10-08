password = input("Masukkan password 3 digit: ")

d1 = int(password[0])
d2 = int(password[1])
d3 = int(password[2])

pelacak_awal = d1 * d3

if d2 % 2 != 0:
    pelacak = pelacak_awal + 25
else:
    pelacak = pelacak_awal - 2

if pelacak % 3 == 0:
    nilai_akhir = pelacak / 2
else:
    nilai_akhir = pelacak * 2
nilai_akhir = int(nilai_akhir)

if nilai_akhir > 50:
    status = "kategori A"
elif nilai_akhir > 20:
    status = "kategori B"
else:
    status = "password ditolak"

if nilai_akhir % 2 == 0:
    siklus = "siklus genap"
else:
    siklus = "siklus ganjil"

print(d1, d2, d3, pelacak_awal, pelacak, nilai_akhir, status, siklus)
