girilen_sayi = int(input("Sayı"))


for i in range(2,girilen_sayi):
    if (girilen_sayi % i) ==0:
        print("sayı asal değildir")
        break



    else:
       print("sayı asaldır")
       break