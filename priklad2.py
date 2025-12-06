import sys

# napište funkci spocitej_statistiku(text), která přijme jeden parametr:
# text – řetězec obsahující více řádků textu
# Funkce vrátí tři hodnoty:
# počet řádků v textu
# počet slov v textu (slovo je sekvence znaků oddělená mezerami nebo koncem řádku)
# počet znaků v textu (včetně mezer a konců řádků)

def spocitej_statistiku(text):

    pocet_radku = 0
    pocet_slov = 0
    pocet_znaku = 0

    # Vaše řešení zde

    return pocet_radku, pocet_slov, pocet_znaku


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pouziti: python program.py vstupni_soubor")
        sys.exit(1)
    vstupni_soubor = sys.argv[1]

    try:
        with open(vstupni_soubor, "r", encoding="utf-8") as f:
            obsah = f.read()

        pocet_radku, pocet_slov, pocet_znaku = spocitej_statistiku(obsah)

        print(f"Pocet radku: {pocet_radku}")
        print(f"Pocet slov: {pocet_slov}")
        print(f"Pocet znaku: {pocet_znaku}")

    except FileNotFoundError:
        print("Vstupni soubor neexistuje")
    except Exception:
        print("Doslo k chybe pri praci se souborem")
