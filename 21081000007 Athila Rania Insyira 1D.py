#program spuder untuk menentukan bilangan terbesar dari beberapa bilangan
#meminta user memasukkan angka

#1.masukkan variable
a = int (input("masukkan bilangan a = "))
b = int (input("masukkan bilangan b = "))
c = int (input("masukkan bilangan c = "))

#kondisi jika bilangan a yang di masukkan lebih besar dari b dan c
if a > b and a > c :
    print (a,"bilangan terbesar dari 3 bilangan yang di inputkan")
elif b > a and b > c :
    print (b,"bilangan terbesar dari 3 bilangan yang di inputkan")
elif c > a and c > b :
    print (c,"bilangan terbesar dari 3 bilangan yang di inputkan")