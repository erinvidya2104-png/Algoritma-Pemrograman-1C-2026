print("=== SISTEM MONITORING  REAKTOR CHERYNOBYL ===")

suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("\nSuhu Diinput :", suhu)
print("Tekanan Diinput:", tekanan)


if suhu > 1000:
    if tekanan > 50:
        pesan_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan_bahaya = "Bahaya suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan_bahaya = "Tekanan Tidak Stabil"
    else:
        pesan_bahaya = "Operasi Reaktor Normal"
else:
    pesan_bahaya = "Reaktor Belum Cukup Panas"


status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"


print("Pesan Status Bahaya :", pesan_bahaya)
print("Status Pompa Air :", status_pompa)
