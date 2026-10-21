

print("Merhaba Kozmos Restoranına Hoşgeldiniz!")

name = input("\nLütfen adınızı giriniz: ")
lastName = input("Lütfen soyadınızı giriniz: ")

print(f"\nHoşgeldiniz {name} {lastName}!")

print("\nLütfen menüden yemek seçiniz: ")


sum = 0

while True:

    print("\n1. Pizza 15tl")
    print("2. Hamburger 20tl")
    print("3. Salata 10tl")
    print("4. işlemi bitir")

    choice = input("\nSeçiminizi yapınız (1-4): ") 

    if choice == "1":
        print("\nPizza sepete eklendi.")
        sum = sum + 15
        

    elif choice == "2":
        print("\nHamburger sepete eklendi.")
        sum = sum + 20

    elif choice == "3":
        print("\nSalata sepete eklendi.")
        sum = sum + 10

    elif choice == "4":
        print("\nİşlemi bitiriyorsunuz.")
        break

print(f"\nToplam tutar: {sum}tl")