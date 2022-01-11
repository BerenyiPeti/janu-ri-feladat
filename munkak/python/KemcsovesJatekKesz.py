import random

print("""
Üdvözöllek a kémcsöves játékban!
A szabályok:
Van négy oszlop, abból háromban véletlenszerűen vannak elhelyezve számok. 
A feladatod az, hogy úgy pakolgasd a számokat, hogy mindegyik oszlopban ugyan azok a számok szerepeljenek!
Egy számot csak egy ugyan olyan számra rakhatsz rá!
Sok sikert! :)

Ha ki szeretnél lépni a játékból, csak írj be egy "k" betűt (kilépés) a számok helyett.
""")

sor1 = [1, 2, 3]
sor2 = [1, 2, 3]
sor3 = [1, 2, 3]

random.shuffle(sor1)
random.shuffle(sor2)
random.shuffle(sor3)

sor1.append(" ")
sor2.append(" ")
sor3.append(" ")

def kiiras(sor):
    for sorkiiras in range(4):
        print("|" + str(sor[sorkiiras]) + "|", end=" ")
    print("")

def kiirasegesz():
    kiiras(sor1)
    kiiras(sor2)
    kiiras(sor3)
    print("")
    print(" 1   2   3   4")
    print("---------------")

def atalakit(oszlop,szam):
    oszlop.append(sor1[szam])
    oszlop.append(sor2[szam])
    oszlop.append(sor3[szam])

def atalakito():
    atalakit(oszlop1,0)
    atalakit(oszlop2,1)
    atalakit(oszlop3,2)
    atalakit(oszlop4,3)

def visszaalakito(sor,szam):
    sor.append(oszlop1[szam])
    sor.append(oszlop2[szam])
    sor.append(oszlop3[szam])
    sor.append(oszlop4[szam])

def visszaalakitoegesz():
    visszaalakito(sor1,0)
    visszaalakito(sor2,1)
    visszaalakito(sor3,2)

jatek = True

while jatek:
    lepes1 = 0
    lepes2 = 0
    oszlop1 = []
    oszlop2 = []
    oszlop3 = []
    oszlop4 = []
    tarolo = []
    tarolo2 = []
    taroltszam = 0
    taroltszam2 = " "
    honnan = 0
    hova = 0
    ervenyes = True
    jobekeres1 = False
    jobekeres2 = False
    kilepes = False

    print("")
    kiirasegesz()
    atalakito()

    while jobekeres1 == False:
        lepes1 = input("Melyik oszlopból szeretnél számot mozgatni? (1-4)")
        if lepes1.isdigit():
            lepes1 = int(lepes1)
            if 4>= lepes1 >= 1:
                jobekeres1 = True
            else:
                kiirasegesz()
                print("Kérlek 1-4 -ig adj meg számokat!")
        elif lepes1 == "k":
            kilepes = True
            jobekeres1 = True
            jatek = False
        else:
            kiirasegesz()
            print("Kérlek 1-4 -ig adj meg egész számokat!")

    while jobekeres2 == False and kilepes == False:
        lepes2 = input("Melyik oszlopba szeretnéd tenni? (1-4)")
        if lepes2.isdigit():
            lepes2 = int(lepes2)
            if 4 >= lepes2 >= 1:
                jobekeres2 = True
            else:
                kiirasegesz()
                print("Kérlek 1-4 -ig adj meg számokat!")
        elif lepes2 == "k":
            kilepes = True
            jobekeres2 = True
            jatek = False
        else:
            kiirasegesz()
            print("Kérlek 1-4 -ig adj meg egész számokat!")

    print("")

    if kilepes == False:
        if lepes1 == 1:
            tarolo = oszlop1
        elif lepes1 == 2:
            tarolo = oszlop2
        elif lepes1 == 3:
            tarolo = oszlop3
        elif lepes1 == 4:
            tarolo = oszlop4

        if lepes2 == 1:
            tarolo2 = oszlop1
        elif lepes2 == 2:
            tarolo2 = oszlop2
        elif lepes2 == 3:
            tarolo2 = oszlop3
        elif lepes2 == 4:
            tarolo2 = oszlop4

        if lepes1 == lepes2:
            print("Nem adhatod meg kétszer ugyan azt az oszlopot!")
            ervenyes = False

        if tarolo2[0] != " ":
            print("Az oszlop, ahova tenni szeretnéd a számot már tele van!")
            ervenyes = False

        if tarolo == [" ", " ", " "]:
            print("Nem választhatsz üres oszlopot elsőnek!")
            ervenyes = False

        if ervenyes:
            for index1 in range(3):
                if tarolo[index1] != " ":
                    honnan = index1
                    taroltszam = tarolo[index1]
                    ervenyes = True
                    break
                else:
                    ervenyes = False

        if ervenyes:
            for index2 in range(2,-1,-1):
                if tarolo2 == [" "," "," "]:
                    hova = index2
                    taroltszam2 = " "
                    ervenyes = True
                    break
                elif tarolo2[index2] == " ":
                    taroltszam2 = tarolo2[index2+1]
                    hova = index2
                    ervenyes = True
                    break
                else:
                    ervenyes = False

        if ervenyes:
            if taroltszam == taroltszam2 or taroltszam2 == " ":
                ervenyes = True
            else:
                print("Nem rakhatsz két különböző számot egymásra!")
                ervenyes = False

        if ervenyes:
            sor1 = []
            sor2 = []
            sor3 = []
            tarolo[honnan] = " "
            tarolo2[hova] = taroltszam

            if lepes1 == 1:
                oszlop1 = tarolo
            elif lepes1 == 2:
                oszlop2 = tarolo
            elif lepes1 == 3:
                oszlop3 = tarolo
            elif lepes1 == 4:
                oszlop4 = tarolo

            if lepes2 == 1:
                oszlop1 = tarolo2
            elif lepes2 == 2:
                oszlop2 = tarolo2
            elif lepes2 == 3:
                oszlop3 = tarolo2
            elif lepes2 == 4:
                oszlop4 = tarolo2

        visszaalakitoegesz()

        if oszlop1[0] == oszlop1[1] == oszlop1[2] and \
        oszlop2[0] == oszlop2[1] == oszlop2[2] and \
        oszlop3[0] == oszlop3[1] == oszlop3[2] and \
        oszlop4[0] == oszlop4[1] == oszlop4[2]:
            kiirasegesz()
            print("Gratulálok, nyertél!")
            jatek = False



