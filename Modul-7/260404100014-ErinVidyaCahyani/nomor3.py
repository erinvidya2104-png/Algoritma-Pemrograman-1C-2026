daftar_undangan = set()
peserta_webinar_a = set()
peserta_webinar_b = set()

print("--- INPUT DATA UNDANGAN ---")
print("Masukkan nama undangan (ketik 'selesai' jika sudah):")
while True:
    nama = input("Nama undangan: ").strip()
    if nama.lower() == 'selesai':
        break
    if nama:
        daftar_undangan.add(nama)

print("\n--- INPUT PESERTA WEBINAR A ---")
print("Masukkan nama peserta Webinar A (ketik 'selesai' jika sudah):")
while True:
    nama = input("Peserta Webinar A: ").strip()
    if nama.lower() == 'selesai':
        break
    if nama:
        peserta_webinar_a.add(nama)

print("\n--- INPUT PESERTA WEBINAR B ---")
print("Masukkan nama peserta Webinar B (ketik 'selesai' jika sudah):")
while True:
    nama = input("Peserta Webinar B: ").strip()
    if nama.lower() == 'selesai':
        break
    if nama:
        peserta_webinar_b.add(nama)

semua_peserta = peserta_webinar_a.union(peserta_webinar_b)

hadir_keduanya = peserta_webinar_a.intersection(peserta_webinar_b)

hanya_satu_webinar = peserta_webinar_a.symmetric_difference(peserta_webinar_b)

tidak_hadir = daftar_undangan.difference(semua_peserta)

print("\n================ HASIL ANALISIS HIMPUNAN ================")
print(f"1. Semua peserta dari kedua webinar : {semua_peserta}")
print(f"2. Peserta yang hadir di keduanya   : {hadir_keduanya}")
print(f"3. Peserta yang hanya di salah satu : {hanya_satu_webinar}")
print(f"4. Undangan yang tidak hadir        : {tidak_hadir}")