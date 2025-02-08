from random import randint

random_number = randint(1, 100)
tahmin = int(input("Tuttuğum sayıyı tahmin et "))
while tahmin != 0:
    if tahmin == random_number:
        print("Tahmin doğru")
        break
    else:
        if tahmin > random_number:
            print("Tahmin ettiğin sayı büyük")
        else:
            print("Tahmin ettiğin sayı küçük")
        tahmin = int(input("Tuttuğum sayıyı tahmin et"))