#Masukkan alas atap
alasAtap = int(input("Masukkan alas atap : "))

#Masukkan tinggi atap 
tinggiAtap = int(input("Masukkan tinggi atap : "))

#Masukkan tinggi tembok 
tinggiTembok = int(input("Masukkan tinggi tembok : "))

#Proses penghitungan semen yang dibutuhkan 
#Luas atap
luasAtap = 0.5 * alasAtap * tinggiAtap
#Luas Tembok
luasTembok = tinggiTembok ** 2
#Luas Keseluruhan
luas = luasAtap + luasTembok
#Semen yang dibutuhkan
semen = luas / 5 

#Hasil
print("Rumah teresebut membutuhkan", semen, "sak semen")
