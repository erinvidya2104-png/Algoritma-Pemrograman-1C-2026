playlists = {}

while True:
    print("\n--- PENGELOLA PLAYLIST MUSIK ---")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist & Lagu")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")
    
    pilihan = input("Pilih menu (1-7): ").strip()
    
    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist baru: ").strip().lower()
        if nama_playlist in playlists:
            print("Playlist tersebut sudah ada!")
        else:
            playlists[nama_playlist] = {}
            print(f"Playlist '{nama_playlist}' berhasil dibuat.")
            
    elif pilihan == "2":
        if not playlists:
            print("Belum ada playlist yang tersedia. Buat playlist terlebih dahulu.")
            continue
            
        nama_playlist = input("Masukkan nama playlist yang dituju: ").strip().lower()
        if nama_playlist not in playlists:
            print(f"Error: Playlist '{nama_playlist}' tidak ditemukan!")
        else:
            judul = input("Masukkan judul lagu: ").strip().lower()
            penyanyi = input("Masukkan nama penyanyi: ").strip()
            
            playlists[nama_playlist][judul] = penyanyi
            print(f"Lagu '{judul}' oleh {penyanyi} berhasil ditambahkan ke playlist '{nama_playlist}'.")
            
    elif pilihan == "3":
        if not playlists:
            print("Belum ada playlist sama sekali.")
        else:
            print("\n--- DAFTAR PLAYLIST MUSIK ---")
            for pl, lagu in playlists.items():
                print(f"\nPlaylist: {pl.title()}")
                if not lagu:
                    print("  (Playlist ini masih kosong)")
                else:
                    for judul, penyanyi in lagu.items():
                        print(f"  - Judul: {judul.title()} | Penyanyi: {penyanyi}")
                        
    elif pilihan == "4":
        if not playlists:
            print("Belum ada playlist untuk dicari.")
            continue
            
        cari_lagu = input("Masukkan judul lagu yang ingin dicari: ").strip().lower()
        ditemukan = False
        
        for pl, lagu in playlists.items():
            if cari_lagu in lagu:
                print(f"Ditemukan! Lagu '{cari_lagu.title()}' (Penyanyi: {lagu[cari_lagu]}) ada di playlist '{pl.title()}'.")
                ditemukan = True
                
        if not ditemukan:
            print(f"Lagu dengan judul '{cari_lagu}' tidak ditemukan di playlist manapun.")
            
    elif pilihan == "5":
        if not playlists:
            print("Belum ada playlist.")
            continue
            
        nama_playlist = input("Masukkan nama playlist asal lagu: ").strip().lower()
        if nama_playlist not in playlists:
            print(f"Error: Playlist '{nama_playlist}' tidak ditemukan!")
        else:
            if not playlists[nama_playlist]:
                print(f"Playlist '{nama_playlist}' kosong, tidak ada lagu untuk dihapus.")
            else:
                judul = input("Masukkan judul lagu yang ingin dihapus: ").strip().lower()
                if judul in playlists[nama_playlist]:
                    del playlists[nama_playlist][judul]
                    print(f"Lagu '{judul}' berhasil dihapus dari playlist '{nama_playlist}'.")
                else:
                    print(f"Error: Lagu '{judul}' tidak ditemukan di playlist tersebut!")
                    
    elif pilihan == "6":
        if not playlists:
            print("Belum ada playlist untuk dihapus.")
            continue
            
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ").strip().lower()
        if nama_playlist in playlists:
            del playlists[nama_playlist]
            print(f"Playlist '{nama_playlist}' berhasil dihapus.")
        else:
            print(f"Error: Playlist '{nama_playlist}' tidak ditemukan!")
            
    elif pilihan == "7":
        print("Keluar dari program Pengelola Playlist. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan masukkan angka 1-7.")