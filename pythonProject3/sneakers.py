import pprint


def beolvas_fajl(fajlnev):
    with open(fajlnev, encoding="utf-8") as f:
        return f.readlines()


def feldolgoz_adatok(sorok):
    fejlec = sorok[0].strip().split(",")
    adatok = []

    for sor in sorok[1:]:
        ertekek = sor.strip().split(",")
        cipo = {fejlec[i]: ertekek[i] for i in range(len(fejlec))}

        if "full_price" in cipo:
            cipo["full_price"] = float(cipo["full_price"])
        if "current_price" in cipo:
            cipo["current_price"] = float(cipo["current_price"])

        adatok.append(cipo)

    return adatok


def kivalaszt_rendezes():
    lehetosegek = {
        "1": "title",
        "2": "color",
        "3": "full_price",
        "4": "current_price",
        "5": "publish_date"
    }

    print("Válassz, melyik szempont alapján rendezzem a cipőket?")
    for key, value in lehetosegek.items():
        print(f"{key} - {value}")

    valasztas = input("Add meg a lehetőség számát! ")

    return lehetosegek.get(valasztas, None)


def rendezes_lista(adatok, kulcs):
    if kulcs:
        return sorted(adatok, key=lambda x: x[kulcs])
    else:
        print("Érvénytelen választás!")
        return adatok


def main():
    fajlnev = "sneakers.csv"

    sorok = beolvas_fajl(fajlnev)
    adatok = feldolgoz_adatok(sorok)

    kulcs = kivalaszt_rendezes()
    rendezett_adatok = rendezes_lista(adatok, kulcs)

    pprint.pprint(rendezett_adatok)


main()
