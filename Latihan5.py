# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

print("------------------------------------------------------")
print("----------- Latihan 4 - Muhammad Raihan -----------")
print("------------------------------------------------------")

modal_kesuluruhan = 0
laba_keseluruhan = 0

while (True):
    print("-----------------------------------------")

    nama_barang = input("\nMasukan nama barang      : ")
    harga_barang = int(input("Masukan harga barang     : "))
    barang_terjual = int(input("Jumlah barang            : "))

    persen = 10
    hargapersen = int(harga_barang * persen / 100)
    harga_penjualan = int(harga_barang + hargapersen)
    modal = harga_barang * barang_terjual
    laba = barang_terjual * hargapersen
    harga_penjualan_keseluruhan = barang_terjual * harga_penjualan

    modal_kesuluruhan = modal_kesuluruhan + modal
    laba_keseluruhan = laba_keseluruhan + laba

    print("\n======================================")
    print("========== I N F O R M A S I =========")
    print("======================================")

    print("\nNama Barang                       :", nama_barang)
    print("Jumlah Barang yang Terjual        :", barang_terjual, "pcs")
    print("Modal                             : Rp.", harga_barang, "per Barang")
    print("Modal Harga Keseluruhan           : Rp.", modal)
    print("Harga Penjualan                   : Rp.",
          harga_penjualan, "per Barang")
    print("Harga Penjualan Keseluruhan       : Rp.", harga_penjualan_keseluruhan)
    print("Keuntungan atau Laba              : Rp.", laba)

    print("\n--------------------------------------")

    apakahLanjut = input("Apakah ingin membeli barang lain? Y or N : ")
    if (apakahLanjut != 'y'):
        break

print("\n\n=======================================")
print("======== S T R U K  B E L I =========")
print("=======================================")

print("\nModal Harga Keseluruhan           : Rp.",
      modal_kesuluruhan)
print("Keuntungan atau Laba              : Rp.",
      laba_keseluruhan)

print("\n=======================================")