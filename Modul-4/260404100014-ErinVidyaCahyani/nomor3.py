n = int(input("Masukkan Bilangan Bulat Positif (n): "))


for i in range(1, n + 1):
    
    
    for a in range(1, i + 1):
        print(f"{a:2}", end=" ")
        
    
    for b in range(2 * (n - i) * 3):
        print(" ", end="")
        
    
    for a in range(i, 0, -1):
        print(f"{a:2}", end=" ")
        
    
    print()

    