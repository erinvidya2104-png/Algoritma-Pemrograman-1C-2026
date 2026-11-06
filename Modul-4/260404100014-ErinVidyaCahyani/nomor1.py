baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))


for i in range(1, baris + 1):
    for j in range(1, lampu + 1):
        
        if j % 3 == 0:
            status = "mengalami gangguan"
        else:
            status = "berfungsi normal"
            
        print(f"Baris {i}, Lampu ke-{j}: {status}")

print("\nPemeriksaan selesai. Silakan periksa sumber listrik utama taman!")
