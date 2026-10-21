
print("Kozmos Restoranına hoş geldiniz!")

name = input("\nLütfen adınızı giriniz: ")
lastName = input("Lütfen soyadınızı giriniz: ")

print(f"\nHoş geldiniz {name} {lastName}!")

sum = 0

while True :

    print("\n1. pizza 15tl")
    print("2. hamburger 10tl")
    print("3. makarna 12tl")
    print("4. işlem bitir")

    choice = input("\nLütfen siparişinizi seçiniz (1-4): ")

    if choice == "1":
        print("sepete pizza eklendi.")
        sum = sum + 15

    elif choice == "2":
        print("sepete hamburger eklendi.")
        sum = sum + 10

    elif choice == "3":
        print("sepete makarna eklendi.")
        sum = sum + 12

    elif choice == "4":
        print("işlem bitirildi.")
        break

print(f"\nToplam tutar: {sum}tl")
