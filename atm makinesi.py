print(""" *********************

1.Bakiye Sorgulama


2.Para Yatırma


3.Para Çekme


""")

bakiye = 1000


while True:
    işlem = input("İşlemi Seçiniz")

    if (işlem == "q"):
        print("Yine Bekleriz")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} Liradır ".format(bakiye))

    elif(işlem == "2"):

        miktar = int(input("Miktarı Giriniz"))

        bakiye += miktar

        print("Bakiyeniz :",bakiye)



    elif (işlem == "3"):
        miktar = int(input("Miktar Giriniz"))

        if(bakiye - miktar < 0):
            print("Yetersiz Bakiye")
            continue
            bakiye -= miktar





    else:
        print("Geçersiz İşlem")