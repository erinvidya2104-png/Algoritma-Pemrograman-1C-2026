print(" Sistem Penjadwalan Shift Asisten Laboratorium ")


asisten_list = []
print("Masukkan nama-nama asisten awal (ketik 'cukup' untuk selesai):")
while True:
    nama = input("Nama asisten: ")
    if nama.lower() == "cukup":
        break
    asisten_list.append(nama)
asisten_awal = tuple(asisten_list)


tambahan = input("Masukkan 1 nama asisten tambahan yang mendadak bergabung: ")
asisten_akhir = asisten_awal + (tambahan,)


hari_list = []
print("\nMasukkan nama-nama hari tugas (ketik 'cukup' untuk selesai):")
while True:
    hari = input("Hari tugas: ")
    if hari.lower() == "cukup":
        break
    hari_list.append(hari)
hari_tugas = tuple(hari_list)


print("\n--- Konfigurasi Pengecualian Shift ---")
kecuali_asisten = input("Masukkan nama asisten pengecualian: ")
kecuali_hari = input("Masukkan hari pengecualian: ")


print("\n--- Jadwal Shift Asisten Laboratorium ---")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == kecuali_asisten and hari == kecuali_hari:
            continue
        print(f"Shift -> Asisten: {asisten} | Hari: {hari}")
        