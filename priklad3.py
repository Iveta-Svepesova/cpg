from abc import ABC, abstractmethod


class Zamestnanec(ABC):
    def __init__(self, jmeno, zakladni_mzda):
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0

    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    @abstractmethod
    def vypocitej_mzdu(self):
        # Zakladni mzda + 1000 Kc za kazdy odpracovany rok
        bonus = 1000 * self.pocet_odpracovanych_let
        return self.zakladni_mzda + bonus

    def __str__(self):
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"


# Vytvorte tridu Programator, ktera dedi od Zamestnanec
# Programator dostava 10% navíc proti mzdě vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Programator(Zamestnanec):
    pass


# Vytvorte tridu Manazer, ktera dedi od Zamestnanec
# konstruktor tridy Manazer prijima navic parametr pocet_podrizenych
# Manazer dostava 1000 Kc navíc za každého podřízeného zaměstnance nad rámec mzdy
# vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Manazer(Zamestnanec):
    pass


if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 0, zakladni mzda 40000 Kc
    # Mzda: 44000 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 0, zakladni mzda 50000 Kc
    # Mzda: 55000 Kc
    
    # Pridame 2 roky praxe
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 2, zakladni mzda 40000 Kc
    # Mzda: 46200 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 2, zakladni mzda 50000 Kc
    # Mzda: 57000 Kc
