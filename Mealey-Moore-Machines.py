def araFonk(string, a):
    sayi = 0
    for i in string:
        if a == i:
            return sayi
        sayi = sayi + 1

def mooreMAKINESI():
    dkEleman = int(input("DURUM KUMESININ ELEMAN SAYISI:"))
    DK = list(range(dkEleman))
    print(DK)
    E = input("Σ (ALFABE):").strip().split(',')
    print(E)

    SK = input("SONUC KUMESI:").strip().split(",")
    print(SK)
    Liste = []
    a = ""
    for i in DK:
        a = ""
        for j in E:
            a += ","
            a += input("{DK} DURUMUNDA {X} GIRDISI ICIN YENI DURUM:".format(DK=i, X=j))
        CIKTI = input("CIKTISI:")
        Liste.append("{DURUM},{CIKTI}".format(DURUM=i, CIKTI=CIKTI) + a)
    print(Liste)

    string = input("ARANACAK KELIME:")
    GIRDI = []
    DURUM = []
    Cikti = []
    GIRDI.append(" ")
    DURUM.append((str(Liste[0].split(",")[0])))
    Cikti.append(str(Liste[0].split(",")[1]))
    state = 0;
    for i in string:
        row = Liste[state].split(",")
        state = int(row[2 + araFonk(E, i)])
        GIRDI.append(str(i))
        DURUM.append(str(state))
        out = Liste[state].split(",")
        Cikti.append(str(out[1]))

    print("GIRDILER:    ", end='')
    print(GIRDI)
    print("DURUMLAR:    ", end='')
    print(DURUM)
    print("CIKTILAR:    ", end='')
    print(Cikti)

def mealeyMAKINESI():
    dkEleman = int(input("DURUM KUMESININ ELEMAN SAYISI:"))
    DK = list(range(dkEleman))
    print(DK)
    E = input("Σ (ALFABE):").strip().split(',')
    print(E)

    SK = input("SONUC KUMESI:").strip().split(",")
    print(SK)
    Liste = []
    a = ""

    for i in DK:
        a = ""
        for j in E:
            a += ","
            a += input("{DK} durumundaki {X} icin yeni durum giriniz:".format(DK=i, X=j))
            a += ","
            a += input("CIKTISI:")

        Liste.append("{DURUM}".format(DURUM=i) + a)
    print(Liste)

    string = input("ARANACAK KELIME:")
    GIRDI = []
    DURUM = []
    Cikti = []

    state = 0;
    for i in string:
        row = Liste[state].split(",")
        state = int(row[((araFonk(E, i) + 1) * 2) - 1])
        GIRDI.append(str(i))
        DURUM.append(str(state))
        Cikti.append(str(row[(araFonk(E, i) + 1) * 2]))

    print("GIRDILER:    ", end='')
    print(GIRDI)
    print("DURUMLAR:    ", end='')
    print(DURUM)
    print("CIKTILAR:    ", end='')
    print(Cikti)
while True:
    print("DEVAM ETMEK ISTEDIGINIZ MAKINEYI SECINIZ:")
    print("1-> MOORE MAKINESI")
    print("2-> MEALEY MAKINESI")
    secim=int(input())

    if secim==1:
        mooreMAKINESI()
    elif secim==2:
        mealeyMAKINESI()
    input("MENUYE DONMEK ICIN 'E' YE BASINIZ...")