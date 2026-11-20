pendaftaran = []

print("=== Pendaftaran Klub Robotika ===")
while True:
  nama = input(
      "Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): "
  )
  if nama.lower() == "selesai":
    break
  pendaftaran.append(nama)  

print("\n--- Evaluasi Daftar Calon Anggota ---")
for nama in pendaftaran:
  
  if nama.lower() == "admin" or len(nama) < 4:
    print(
        f"Nama '{nama}' -> Tidak Valid (Menggunakan nama 'admin' atau panjang"
        " kurang dari 4 karakter)"
    )
  else:
    print(f"Nama '{nama}' -> Valid")


penyusup = input(
    "\nMasukkan nama spesifik yang dicurigai sebagai penyusup untuk dihapus: "
)

if penyusup in pendaftaran:
  pendaftaran.remove(penyusup)  
  print(f"Nama '{penyusup}' berhasil dihapus dari sistem.")
else:
  print(
      f"Nama '{penyusup}' tidak ditemukan di dalam pendaftaran, program aman"
      " dari error."
  )

print("\nDaftar Akhir Pendaftaran:", pendaftaran)