# Menggunakan referensi dari contoh 1.3 menggunakan rumus langsung compound interest

import math 

'''
memerlukan bantuan modul math supaya mampu menghitung/mencari t 
yang jika didalam rumus aslinya menggunakan rumus logaritma natural 
'''
# Uang Awal Erika (P)
P = 200000000

# Uang yang diinginkan Erika setelah dideposito (A)
A = 400000000

# Bunga pertahun/periode (r)
r = 0.1 #10% pertahun biasanya 

# Jumlah periode bunga (n)
n = 1  

# Jumlah waktu/tahun yang dibutuhkan (t)
t = (math.log(A/P)) / (n * math.log(1 + r/n))

# Menampilkan waktu yang dibutuhkan
print("Waktu yang dibutuhkan Erika untuk mencapai 400 Juta adalah selama sekitar :", round(t) , "tahun")
