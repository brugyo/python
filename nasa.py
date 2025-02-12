def honap_beolvaso(eleres):
    with open(eleres, 'r', encoding='utf-8') as file:
        next(file)
        honapok = []
        for sor in file:
            reszek = sor.strip().split(',')
            if len(reszek) >= 5:
                if reszek[4]:
                    honap = int(reszek[4].split('/')[0])
                    honapok.append(honap)
    return honapok


def top_honap_szamolo(honapok):
    szamolt_honapok = {}
    total = len(honapok)

    for honap in honapok:
        szamolt_honapok[honap] = szamolt_honapok.get(honap, 0) + 1

    top_harom = []
    for _ in range(3):
        max_honap = max(szamolt_honapok, key=szamolt_honapok.get)
        top_harom.append((max_honap, szamolt_honapok.pop(max_honap)))

    return [(honap, round(szam / total * 100, 1)) for honap, szam in top_harom]


def main():
    eleres = "astronauts.csv"
    honapok = honap_beolvaso(eleres)
    top_honapok = top_honap_szamolo(honapok)
    for honap, szazalek in top_honapok:
        print(f"{honap}. hónap: {szazalek}%")


main()
