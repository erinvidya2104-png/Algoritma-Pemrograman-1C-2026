todo_list = {}

while True:
    print("\n--- MENU TO-DO LIST ---")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Tampilkan Jumlah Tugas Selesai & Belum")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ").strip()
    
    if pilihan == "1":
        tugas = input("Masukkan nama tugas baru: ").strip().lower()
        if not tugas:
            print("Nama tugas tidak boleh kosong!")
        elif tugas in todo_list:
            print("Tugas tersebut sudah ada di dalam daftar!")
        else:
            todo_list[tugas] = "Belum Selesai"
            print(f"Tugas '{tugas}' berhasil ditambahkan.")
            
    elif pilihan == "2":
        if len(todo_list) == 0:
            print("Belum ada tugas dalam daftar.")
        else:
            print("\n--- DAFTAR TUGAS ---")
            for tugas, status in todo_list.items():
                print(f"- {tugas} : [{status}]")
                
    elif pilihan == "3":
        tugas = input("Masukkan nama tugas yang ingin ditandai selesai: ").strip().lower()
        if tugas in todo_list:
            todo_list[tugas] = "Selesai"
            print(f"Tugas '{tugas}' telah ditandai Selesai.")
        else:
            print("Error: Tugas tidak ditemukan!")
            
    elif pilihan == "4":
        tugas = input("Masukkan nama tugas yang ingin dihapus: ").strip().lower()
        if tugas in todo_list:
            del todo_list[tugas]
            print(f"Tugas '{tugas}' berhasil dihapus.")
        else:
            print("Error: Tugas tidak ditemukan!")
            
    elif pilihan == "5":
        selesai = 0
        belum = 0
        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1
        print(f"\nJumlah Tugas Selesai      : {selesai}")
        print(f"Jumlah Tugas Belum Selesai : {belum}")
        
    elif pilihan == "6":
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan masukkan angka 1-6.")