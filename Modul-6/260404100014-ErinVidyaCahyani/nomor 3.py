print("=== Sistem Pendataan Inventaris PC ===")
jumlah_input = int(input("Masukkan jumlah PC yang ingin didata: "))

inventaris_pc = []

for i in range(jumlah_input):
  nomor = i + 1
  print("\nPendataan PC ke-" + str(nomor) + ":")
  
  nama_pc = input("Masukkan Nama PC: ")
  status_pc = input("Masukkan Status (Normal/Rusak): ")
  ram_pc = input("Masukkan Kapasitas RAM (GB): ")
  
  inventaris_pc.append([nama_pc, status_pc, ram_pc])

print("\n=== Hasil Evaluasi Kelayakan PC ===")

def evaluasi_pc(status, ram):
  if ram.lower() == "delapan":
    return "Format RAM Kacau"
  else:
    ram_angka = int(ram)
    if status.lower() == "normal" and ram_angka >= 8:
      return "Layak"
    else:
      return "Tidak Layak"

for pc in inventaris_pc:
  nama = pc[0]
  status = pc[1]
  ram = pc[2]
  
  kelayakan = evaluasi_pc(status, ram)
  
  hasil_string = '{ "PC": "' + str(nama) + '", "Status": "' + str(kelayakan) + '" }'
  print(hasil_string)