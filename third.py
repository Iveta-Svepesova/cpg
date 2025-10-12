import time
import math

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
    cislo = int(cislo)
    if cislo <= 1:
        return False
    i = 0
    #for delitel in range(2, round(cislo**0.5)):
    for delitel in range(2, cislo):
        time.sleep(0.001)
        if cislo % delitel == 0:
            print(f'Iterace {i}')
            return False
        i += 1
    print(f'Iterace: {i}')
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    # 999983
    print(je_prvocislo(cislo))
    # prvocisla = vrat_prvocisla(cislo)
    # print(prvocisla)