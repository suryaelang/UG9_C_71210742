#Memasukkan kalimat yang akan dijadikan materi untuk mencari kata yang akan ditentukan
kalimat = str(input("Masukkan kalimat : "))
kata = str(input("Masukkan kata untuk dihitung : "))

#Proses untuk mencari jumlah kata yang telah ditentukan dalam sebuah kalimat
jumlah = kalimat.count(kata)


#Hasil dari proses
print("ada", jumlah, "buah kata", kata)