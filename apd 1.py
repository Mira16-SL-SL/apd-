x= int(input("Masukkan jumlah kue keju yang akan dibeli  : "))
keju = 6000
if int(4 <= x <= 15):
    print("Anda mendapatkan diskon 10%")
    harga_asli = x * keju
    print("harga asli : ", harga_asli)
    total = x *keju * (10/100)
    diskon = harga_asli - total
    print("Harga spesial : ",diskon)
    
elif int(16 <= x <= 25):
    print("Anda mendapatkan diskon 15%")
    harga_asli = x * keju
    print("harga asli : ", harga_asli)
    total = x *keju * (15/100)
    diskon = harga_asli - total
    print("Harga spesial : ",diskon)
    
elif (x > 25):
    print("Maaf, stok hanya 25")

else :
    print("Maaf anda tidak mendapatkan diskon")
    jumlah = x *keju
    print("Jumlah rasa keju : ",jumlah)


y = int(input("Masukkan jumlah kue rasa coklat yang akan dibeli : "))
coklat = 3500
if int(5 <= y <= 20):
    print("Anda mendapatkan diskon 7%")
    harga_asli =y * coklat
    print("harga asli : ", harga_asli)
    total = y *coklat * (7/100)
    diskon = harga_asli - total
    print("Harga spesial :",diskon)
    
elif int(21 <= y <= 35):
    print("Anda mendapatkan diskon 12%")
    harga_asli = y * coklat
    print("harga asli : ", harga_asli)
    total4 = y *coklat * (12/100)
    diskon2 = harga_asli - total
    print("Harga spesial : ",diskon)
    
elif (y > 35):
    print("Maaf stok hanya 35")

else :
    print("Maaf anda tidak mendapatkan diskon")
    jumlah = y *coklat
    print("Jumlah kue rasa  coklat : ",jumlah)