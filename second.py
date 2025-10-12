def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    specialni = {11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct",
                 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"}

    cislo = int(cislo)
    
    if cislo in specialni:
        return specialni[cislo]
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo % 10 == 0 and cislo < 100:
        return desitky[cislo // 10]
    elif cislo < 100:
        return desitky[cislo // 10] + " " + jednotky[cislo % 10]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah"


