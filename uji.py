def coba_lagi():
    cl = input('Mau coba lagi [Y/N]? ')
    if cl == "Y" or "y" :
        main_menu()
    if cl == "N" or "n":
        exit()
    else :
        coba_lagi()

def persegipanjang():
   p = int(input('Masukkan Panjang : '))
   l = int(input('Masukkan Lebar : '))
   Luas = p * l
   print('Luas Persegi Panjang adalah %d\n'% Luas)
   coba_lagi()
def lingkaran():
    phi = 3.14
    r = int(input('Masukkan jari-jari : '))
    Luas = phi * (r**2)
    print('Luas Lingkaran adalah %f\n'% Luas)
    coba_lagi()
def segitiga():
    a = int(input('Masukkan Alas : '))
    t = int(input('Masukkan Tinggi : '))
    Luas = (a*t)/2
    print('Luas Segitiga adalah %f\n'% Luas)
    coba_lagi()

def main_menu():
    print("Selamat Datang di Program Untuk Menghitung Luas")
    print("==============================================\n")
    print("Menu Pilihan\n")
    print("1. Persegi Panjang\n"
          "2. Lingkaran\n"
          "3. Segitiga\n"
          "4. Keluar")
    pil = int(input('Masukkan Pilihan : '))
    if pil == 1:
        persegipanjang()
    elif pil == 2:
        lingkaran()
    elif pil == 3 :
        segitiga()
    elif pil == 4:
        exit()
    else :
        print("angka yang anda pilih salah")
        input("Press Enter to Continue....")
        main_menu()
main_menu()