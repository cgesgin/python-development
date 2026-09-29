print("=== TAŞ KAĞIT MAKAS OYUNU ===")

oyuncu = input("Taş, kağıt veya makas seç: ")
bilgisayar = "taş"

if oyuncu == bilgisayar:
    print("Berabere!")
elif oyuncu == "kağıt":
    print("Kazandın!")
elif oyuncu == "makas":
    print("Kaybettin!")
else:
    print("Geçersiz seçim!")
