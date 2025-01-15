n = int(input("Entrez un nombre pair : "))

if n % 2 != 0:
    print("Le nombre doit être pair.")
else:
    c = 0
    while n % 2 == 0:
        n = n / 2
        c += 1
        
print(f"Le nombre est divisible {c} fois par 2.")
