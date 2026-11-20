print("=== SISTEM KEAMANAN GARASI MARKAS CIA ===")


pin = int(input("Masukkan PIN 3 digit pin kamu: "))
jam = int(input("Masukkan jam berapa kamu datang (0-23): "))


digit1 = (pin // 100)
digit2 = ((pin // 10) % 10)   
digit3 = (pin % 10)

print("\nHasil pecahan digit PIN:")
print("Digit 1:", digit1)
print("Digit 2:", digit2)
print("Digit 3:", digit3)


if pin % 5 == 0:
    if jam < 12:
        pesan_akses = "Garasi Pagi Terbuka"
    else:
        pesan_akses = "Garasi Malam Terbuka"
elif pin % 2 == 0:
    if (digit1 + digit3) == digit2:
        pesan_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan_akses = "Akses Diitolak Sepenuhnya"


status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Merekam"

print("\nStatus Pintu :", pesan_akses)
print("Status CCTV :", status_cctv)