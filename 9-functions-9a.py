

def topla(a,b):
    sonuc = a + b
    print(sonuc)

topla(8,12)

def carp(a,b):
    sonuc =a * b
    print(sonuc)

carp(5,6)

def bol(a,b):
    sonuc = a / b
    print(sonuc)

bol(10,2)

def cikar(a,b):
    sonuc = a - b
    print(sonuc)

cikar(5,2)

def ekrana_yazdir():
    for i in range(1,6):
        print("Merhaba, Dünya!")

ekrana_yazdir()


def hesapla(a,b,islem):
    if islem =="+":
        sonuc = a + b
        print(sonuc)
    elif islem =="-":
        sonuc = a - b
        print(sonuc)
    elif islem =="*":
        sonuc = a * b
        print(sonuc)
    elif islem =="/":
        sonuc = a / b
        print(sonuc)


hesapla(8,4,"/")
hesapla(8,4,"*")
hesapla(8,4,"-")
hesapla(8,4,"+")

