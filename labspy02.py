# Input 3 Buah Bilangan Menggunakan Statement If
print("Menuntukan Bilangan Terbesar")

print("Masukkan Bilangan ke 1 : ")
bilangan1=int(input())
print("Masukkan Bilangan ke 2  : ")
bilangan2=int(input())
print("Masukkan Bilangan ke 3 : ")
bilangan3=int(input())

print("\n")

if ( bilangan1 > bilangan2 ) and ( bilangan1 > bilangan3) :
    print ("Bilangan 1 lebih besar  dari bilangan 2 dan 3")
elif ( bilangan2 > bilangan1 ) and ( bilangan2 > bilangan3 ) :
    print ("Bilangan 2 lebih besar dari bilangan 1 dan 3")
elif ( bilangan3 > bilangan1 ) and ( bilangan3 > bilangan2 ) :
    print ("Bilangan 3 lebih besar dari Bilngan 1 dan 2")
else :
    print ("Semua Bilangan sama besarnya")