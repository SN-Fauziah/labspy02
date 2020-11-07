# labspy02
Repository ini dibuat untuk memenuhi tugas pertemuan 7 Modul praktikum 2 <br>

Nama    : Siti Nur Fauziah<br>
NIM     : 312010032<br>
Kelas   : TI.20.B1<br>


## Menentukan Bilangan Tersebar  dari Nilai yang diinputkan
<br>
Pada pertemuan ke 7 saya mendapatkan tugas dari Dosen Bahasa Pemrograman untuk membuat aplikasi yang menentukan bilagan terbesar dari 3 nilai yang user inputkan menggunakan Bahasa Pemrograman<br>
![Tugas Labspy](Foto.PNG) <br>

> Pada repository kali ini saya akan menjelaskan alur dalam *Flowchart* yang telah saya buat. File *flowchar* bisa dilihat pada link berikut ini :<br>
[Tugas Labspy](link)<br>

Berikut source code yang saya tulis untuk menjadikan tersebut Link Labspy ([Labspy02](link.py)) : <br>

```python
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
```
Dari source code tersebut akan menghasilkan output :<br>
