def nilai_mhs(nama, tugas, uts, uas):
    
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    
   
    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
   
    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"
        
   
    print("\nNama:", nama)
    print("Nilai Akhir:", akhir)
    print("Grade:", grade)
    print("Status:", status)


nm = input("Masukkan nama: ")
tgs = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai_mhs(nm, tgs, uts, uas)