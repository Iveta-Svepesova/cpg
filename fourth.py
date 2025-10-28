def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """

    typ = figurka["typ"]
    start = figurka["pozice"]
    cil = cilova_pozice
    obsazena_pole = obsazene_pozice

    x1, y1 = start
    x2, y2 = cil

    # 1️⃣ Ověření – cílové pole musí být na šachovnici
    if not (1 <= x2 <= 8 and 1 <= y2 <= 8):
        return False

    # 2️⃣ Cílové pole musí být volné
    if cil in obsazena_pole:
        return False

    dx = x2 - x1
    dy = y2 - y1

    # 3️⃣ Logika pro každou figuru
    if typ == "pěšec":
        # Pěšec se pohybuje nahoru (z menšího na větší y)
        if dx == 0 and dy == 1 and cil not in obsazena_pole:
            return True
        # Dvojkrok z výchozí pozice (y == 2)
        if dx == 0 and dy == 2 and y1 == 2 and (x1, 3) not in obsazena_pole and (x1, 4) not in obsazena_pole:
            return True
        return False

    elif typ == "jezdec":
        return (abs(dx), abs(dy)) in [(1, 2), (2, 1)]

    elif typ == "věž":
        if dx != 0 and dy != 0:
            return False
        # zkontroluj, že mezi startem a cílem nejsou jiné figury
        if dx == 0:
            step = 1 if dy > 0 else -1
            for y in range(y1 + step, y2, step):
                if (x1, y) in obsazena_pole:
                    return False
        else:
            step = 1 if dx > 0 else -1
            for x in range(x1 + step, x2, step):
                if (x, y1) in obsazena_pole:
                    return False
        return True

    elif typ == "střelec":
        if abs(dx) != abs(dy):
            return False
        x_step = 1 if dx > 0 else -1
        y_step = 1 if dy > 0 else -1
        for i in range(1, abs(dx)):
            if (x1 + i * x_step, y1 + i * y_step) in obsazena_pole:
                return False
        return True

    elif typ == "dáma":
        # Kombinuje pohyb věže a střelce
        if dx == 0 or dy == 0:
            # Dáma se chová jako věž
            return je_tah_mozny({"typ": "věž", "pozice": start}, cil, obsazena_pole)
        elif abs(dx) == abs(dy):
            # Dáma se chová jako střelec
            return je_tah_mozny({"typ": "střelec", "pozice": start}, cil, obsazena_pole)
        else:
            return False

    elif typ == "král":
        return abs(dx) <= 1 and abs(dy) <= 1

    else:
        return False