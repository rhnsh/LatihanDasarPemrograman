#input nama barang
#input harga baranngbaran#deskriptif
#membuat variabel nama barang
#membuat variabel harga barang
#membuat variabel persen harga
#menghitung harga barang
#harga barang * persen /100
#print harga barang beserta nama barang

while("True"):
    nama_barang = input('masukan nama barang   :')
    harga_barang = input('masukan harga barang :')
    persen = input('masukan persen barang :')
    harga_keuntungan = int(harga_barang) * int (persen) / 100
    harga_jual = int(harga_barang) + harga_keuntungan
    print(nama_barang, 'dijual dengan harga :', harga_jual)

    apakahLanjut = input('apakah ingin input barang lain? Y lanjut, N tidak :')
    if(apakahLanjut != 'Y'):
        break