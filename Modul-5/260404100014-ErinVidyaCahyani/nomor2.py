def palindrom(teks):
    balik = teks[::-1]
    
    if teks == balik:
        return True
    else:
        return False

kata = input("Masukkan kata(huruf kecil semua): ")
cek = palindrom(kata)


if cek == True:
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")