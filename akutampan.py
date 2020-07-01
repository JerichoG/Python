nilai = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
temp = [] #Tempat simpan nilai tengah kanan kiri sementara
array_kanan = [] #Tempat simpan array bagian kanan
array_kanan1 = [];array_kanan2 = []
array_kiri = [] #Tempat simpan array bagian kiri
array_kiri1 = [];array_kiri2 = []
tampung_array= [] #Tempat simpan array tengah kanan kiri final

def cari_tengah(a,b):   #Mencari Nilai tengah untuk tiap bagian
    if len(a) == 0:
        return 0
    tengah = len(a)//2
    b.append(a[tengah])
    kiri = a[:tengah]
    kanan = a[tengah+1:]
    cari_tengah(kanan,b) #Mencari nilai tengah untuk bagian kanan
    cari_tengah(kiri,b) #Mencari nilai tengah untuk bagian kiri

def pisah_kanan(a,b): #Untuk memisahkan hasil nilai tengah bagian kanan
    tengah = len(a)//2
    if b == 0:
        global array_kanan
        array_kanan = a[1:tengah+1]
        pisah_kiri(temp,0)
    elif b == 1:
        global array_kanan1
        array_kanan1 = a[1:tengah+1]
        pisah_kiri(array_kiri,1)
    elif b == 2:
        global array_kiri2
        array_kiri2  = a[1:tengah+1]
        pisah_kiri(array_kanan,2)

def pisah_kiri(a,b): #Untuk memisahkan hasil nilai tengah bagian kiri
    tengah = len(a)//2
    if b == 0:
        global array_kiri
        array_kiri = a[tengah+1:]    
        pisah_kanan(array_kanan,1)
    elif b == 1:
        global array_kiri1
        array_kiri1 = a[tengah+1:]
        pisah_kanan(array_kiri,2)
    elif b == 2:
        global array_kanan2
        array_kanan2 = a[tengah+1:]
        gabung_awal()

def gabung_awal():  #Memasukkan nilai awal untuk tiap array yang akan dimasukkan kedalam tampung_array
    global tampung_array,temp,array_kanan,array_kiri,array_kanan1,array_kanan2,array_kiri1,array_kiri2
    tampung_array.append(temp[0])
    tampung_array.append(array_kanan[0]);tampung_array.append(array_kiri[0])
    tampung_array.append(array_kanan1[0]);tampung_array.append(array_kanan2[0])
    tampung_array.append(array_kiri2[0]);tampung_array.append(array_kiri1[0])

def gabung_kanan_kiri(a,b): #Menggabungkan sub array_kanan dan sub array_kiri ke dalam tampung_array
    global tampung_array,temp,array_kanan,array_kiri,array_kanan1,array_kanan2,array_kiri1,array_kiri2
    for i in range(1,5):
        if i%2 == a:
            tampung_array.append(array_kanan1[i]);tampung_array.append(array_kiri2[i])
            if i == b:
                for j in range(1,5):
                    if j%2 == a:
                        tampung_array.append(array_kanan2[j]);tampung_array.append(array_kiri1[j])

cari_tengah(nilai,temp)
pisah_kanan(temp,0)
print("array_sementara ",temp,"banyaknya data",len(temp))
print("array_kanan", array_kanan);print("array_kiri",array_kiri)
print("array_kanan1",array_kanan1)
print("array_kanan2",array_kanan2)
print("array_kiri1",array_kiri1);print("array_kiri2",array_kiri2)
gabung_kanan_kiri(1,3)
gabung_kanan_kiri(0,4)
print("array_tampung_kanan_kiri ",tampung_array,"banyaknya data",len(tampung_array))