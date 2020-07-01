import pyqrcode
import os

path = 'D:/Serathon2.0/Tiket'

#if not os.path.exists(chap):
 #   os.mkdir(chap)
#else:
 #   print("folder already exist")

teks=input("Masukkan Teks : ")
code = pyqrcode.create(teks)
file=code.png(teks+'.png',scale=6)
code.show()

