total_gaji = 0
total_hari_shift = 0
gaji_pokok = 100000
tambahan_shift = 50000

print("Program Gaji Karyawan (7 Hari)")

for hari in range(1, 8):
    print("\n--- Hari ke-", hari, " ---")
    shift = input("Apakah bekerja shift malam? (ya/tidak): ")
    
    lembur = int(input("Masukkan jam lembur (0-8 jam): "))
    while lembur > 8 or lembur < 0:
        print("Lembur melebihi batas atau tidak valid! Silakan masukkan ulang.")
        lembur = int(input("Masukkan jam lembur (0-8 jam): "))

    upah_lembur = 0
    if lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000

    
    if shift == 'ya':
        tambahan_harian = tambahan_shift
    else:
        tambahan_harian = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan_harian

    total_gaji = total_gaji + gaji_harian
    
    if shift == 'ya':
        total_hari_shift = total_hari_shift + 1

print("Total Gaji Mingguan Selama 7 Hari: Rp", total_gaji)
print("Total Hari Kerja Shift Malam:", total_hari_shift, "hari")