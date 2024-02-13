import math

# Jumlah awal (P)
P = 200_000_000  # 200 juta rupiah

# Jumlah akhir (A)
A = 400_000_000  # 400 juta rupiah

# Bunga per periode (r)
r = 0.1  # 10% per tahun

# Jumlah periode bunga dalam setahun (n)
n = 1  # bunga dihitung setahun sekali

# Menghitung waktu yang dibutuhkan (t)
t = (math.log(A/P)) / (n * math.log(1 + r/n))

# Menampilkan waktu yang dibutuhkan
print("Waktu yang dibutuhkan:", round(t, 2), "tahun")
