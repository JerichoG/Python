import os

chap='D:/contoh'

if not os.path.exists(chap):
    os.mkdir(chap)
else:
    print("folder already exist")