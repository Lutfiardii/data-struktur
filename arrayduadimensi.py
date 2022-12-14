a=10
b=30
perkalian=a*b
print(perkalian)

#dictionary
nama_mhs = {
    "nama" : "lutfi",
    "alamat" : "batang",
    "noHP" : 9880,
}
print("---------------------------")
print("nama | mahasiswa | alamat |")
print("---------------------------")
print(nama_mhs["nama"],nama_mhs["alamat"],nama_mhs["noHP"])
print("---------------------------")



#array
from array import *
array1 = array ('i',[10,20,30,40,50])
perkalian = array1[3] * array1[4]
print("------------------------------------------------")
print("hasil perkalian antara ",array1[3],"dan ",array1[4],"adalah",perkalian)
print("------------------------------------------------")
# print(array1[0])
# print(array1[2])
array1.insert(1,60)
for x in array1:
    # print(x)
    result = x**2
    # print(result)
    print("bil awal",x,"hasil pangkatnya adalah",result)
print()

#loopingmatriks
a = array("i",[10,12,13])
b = array("i",[2,4,6])

for x in a:
    for y in b:
        penjumlahan = x+y
        perkalian = x*y

    print(x,"+",y,"=",penjumlahan,x,"x",y,"=",perkalian)
