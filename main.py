import random

angka_min = 1
angka_max = 10
angka_rahasia = random.randint(angka_min, angka_max)


tebakan = int(input("tebak angka dari 1 - 10: "))

while tebakan != angka_rahasia:
    if tebakan < angka_rahasia:
        print("Tebakanmu terlalu rendah.")
    else:
        print("Tebakanmu terlalu tinggi.")
    tebakan = int(input("Coba lagi: "))

print("Selamat! Tebakanmu benar.")