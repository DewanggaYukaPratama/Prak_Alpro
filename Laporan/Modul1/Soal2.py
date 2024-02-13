# Harga emas awal pergram
harga_awal = 650000

#Harga emas sekarang pergram
harga_skr = 685000

# Berat emas awal dibeli
berat_awal = 25

# Hitung keuntungan dalam rupiah
rupiah = (harga_skr - harga_awal) * berat_awal

# Hitung keuntungan dalam persen
persen = (rupiah / (harga_awal * berat_awal)) * 100

print("Keuntungan yang didapat Gerard Sebesar:")
print("Keuntungan yang didapat Gerrard :", rupiah)
print("Keuntungan yang didapat Gerrard :", persen)

# Harga baru/kemudian 
harga_baru = 715000

#Berat baru/kemudian
berat_baru = 15

# Total berat emas setelah pembelian baru
total_emas = berat_awal + berat_baru

# Hitung keuntungan setelah pembelian baru dalam rupiah
rupiah_baru = (harga_baru - harga_skr) * berat_baru

# Hitung keuntungan setelah pembelian baru dalam persen
persen_baru = (rupiah_baru / (harga_skr * total_emas)) * 100

print("\nKeuntungan setelah pembelian baru sebesar :")
print("Keuntungan dalam Rupiah:", rupiah_baru)
print("Keuntungan dalam Persen:", persen_baru)
