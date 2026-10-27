
fruit1 = "armut"
fruit2 = "elma"
fruit3 = "çilek"
fruit4 = "muz"

fruits = ["armut","elma","çilek","muz","kivi"]

numbers = [11.1 , 12.9 , 50.5, 20.5]

numbers2 = [11 , 12 , 50, 20]

mix = ["Ali", 25, True, 3.14]

print(fruits[0])

fruits.append("kiraz")

print(fruits[5])

fruits.remove("kiraz")

sum = len(fruits)

print(sum)

fruits[0] = "mandalina"

print(fruits[0])

print("Listenin elemanları")
for i in range(0,len(fruits)):
    print(fruits[i])
