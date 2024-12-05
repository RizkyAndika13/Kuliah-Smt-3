
print ("Nama : Rizky Andika")
print ("Nim : 23090230006")
print ("Kelas : Sains Data")

a = 3
b = 4
c = 5
print (f"hasil dari {a} + {b} + {c} =", a+b+c)
print (f"hasil dari {a} * {b} =", a*b)
print (f"hasil dari {c} + {a} =", c+a)
print (f"hasil dari {c} - {b} =", c-b)

alas = int(input("masukan alas segitiga : "))
tinggi = int(input("masukan tinggi segitiga : "))
luas = 1/2 * alas * tinggi

print (f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas} ")

nilai = int (input("masukan nilai :"))

if nilai >= 90:
    print ("selmat nilai anda A")
elif nilai >=80:
    print("selamat nilai anda B")
elif nilai >=70:
    print("selamat nilai anda C")
elif nilai >= 60:
    print("selamat nilai anda D")
else :
    print("selamat nilai anda E")

