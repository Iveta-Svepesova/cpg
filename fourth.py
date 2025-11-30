def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    start = figurka["pozice"]
    cil = cilova_pozice
    obsazena_pole = obsazene_pozice

    x1, y1 = start
    x2, y2 = cil

    # 1️⃣ Ověření – cílové pole musí být na šachovnici
    if not (1 <= x2 <= 8 and 1 <= y2 <= 8):
        return False

    dx = x2 - x1
    dy = y2 - y1

    if typ == "pěšec":
        # pohyb vpřed
        if dx == 0:
            # jedno pole vpřed
            if dy == 1 and cil not in obsazena_pole:
                return True
            # dva pole vpřed z výchozí pozice
            if dy == 2 and y1 == 2 and (x1, 3) not in obsazena_pole and (x1, 4) not in obsazena_pole:
                return True
        # bicí tah diagonálně
        if abs(dx) == 1 and dy == 1 and cil in obsazena_pole:
            return True
        return False

    elif typ == "jezdec":
        return (abs(dx), abs(dy)) in [(1, 2), (2, 1)]

    elif typ == "věž":
        if dx != 0 and dy != 0:
            return False
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
        if dx == 0 or dy == 0:
            return je_tah_mozny({"typ": "věž", "pozice": start}, cil, obsazena_pole)
        elif abs(dx) == abs(dy):
            return je_tah_mozny({"typ": "střelec", "pozice": start}, cil, obsazena_pole)
        else:
            return False

    elif typ == "král":
        return abs(dx) <= 1 and abs(dy) <= 1

    else:
        return False
