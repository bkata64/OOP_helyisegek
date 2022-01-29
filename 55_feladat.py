class Helyiseg:
    def __init__(self, szelesseg, hosszusag, magassag):
        self.szelesseg = szelesseg
        self.magassag = magassag
        self.hosszusag = hosszusag

    def alapterulet(self):
        return self.szelesseg * self.hosszusag

    def falterulet(self):
        return (self.hosszusag * self.magassag + self.szelesseg) * 2

    def festett_felulet(self):
        return self.falterulet() + self.alapterulet()


def beker():
    helyisegek_szama = int(
        input("Hány helyiségben szeretne kövezni/festeni? "))
    hely = []
    for i in range(helyisegek_szama):
        print(f"{i + 1}. helyiség adatai:")
        sz = float(input("\tHelyiség szélesség: "))
        h = float(input("\tHelyiség hosszúság: "))
        m = float(input("\tHelyiség magasság: "))
        helyiseg = Helyiseg(sz, h, m)
        hely.append(helyiseg)
    return hely

def beolvas():
    lista = []
    with open("hely.txt", "r") as file:
        for sor in file:
            adatok = sor.strip().split()
            sz = float(adatok[0])
            h = float(adatok[1])
            m = float(adatok[2])
            helyiseg = Helyiseg(sz, h, m)
            lista.append(helyiseg)
    return lista

def kiertekel(helyisegek):
    print("\nA szükséges alapanyagok mennyisége:")
    mennyiseg_m2 = 0.13
    ossz_at = 0
    ossz_ff = 0
    for i, hely_ in enumerate(helyisegek):
        print(f"A(z) {i + 1}. helyiséghez szükséges:")
        at = hely_.alapterulet()
        ossz_at += at
        print(f"\tPadlóburkoló: {at} m2")
        ff = hely_.festett_felulet()
        ossz_ff += ff
        print(f"\tFesték: {round(ff * mennyiseg_m2)} l")

    print(f"\nÖsszes szükséges padlóburkoló: {ossz_at} m2")
    print(f"Összes szükséges festékmennyiség: {round(ossz_ff * mennyiseg_m2)} l")

def main():
    print("Helyiségek festése, kövezése")
    valasz = input("Az adatokat állományból olvassuk be? (i / n): ")
    helyisegek = []
    if valasz == "i":
        helyisegek = beolvas()
    elif valasz == "n":
        helyisegek = beker()
    kiertekel(helyisegek)

main()


