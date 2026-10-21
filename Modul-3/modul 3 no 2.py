
print("PROGRAM MENARA LAMPU HIAS")
print()

n = int(input("Masukkan tinggi n (2 sampai 15): "))
while n < 2 or n > 15:
    print("Nilai harus antara 2 sampai 15! Coba lagi.")
    n = int(input("Masukkan tinggi n (2 sampai 15): "))

i = 1
while i <= n:

    spasi = n - i
    s = 1
    while s <= spasi:
        print(" ", end="")
        s = s + 1

    j = 1
    while j <= i:
        print(j % 10, end="")
        j = j + 1
    
    k = i - 1
    while k >= 1:
        print(k % 10, end="")
        k = k - 1

    print()
    i = i + 1

i = n - 1
while i >= 1:
  
    s = 1
    while s <= (n - i):
        print(" ", end="")
        s = s + 1

    j = 1
    while j <= i:
        print(j % 10, end="")
        j = j + 1

    k = i - 1
    while k >= 1:
        print(k % 10, end="")
        k = k - 1

    print()
    i = i - 1
