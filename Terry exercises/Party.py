# Esercizio molto semplice, per rilassarmi. Un cane ha diversi amici con un grado di amicizia
# espresso con un numero che può essere minore o maggiore di 0; sta organizzando una festa e deve valutare
# chi invitare, per cui deve calcolare il massimo divertimento della festa sommando i gradi di amicizia di chi
# vuole invitare, in base a se renderebbero la festa migliore o peggiore.

import sys

def main():
    data_mom = map(int, sys.stdin.read().split())
    n_casi = next(data_mom)
    data = list(data_mom)
    fun = []
    i = 0
    while i < len(data):
        massimo = 0
        caso = data[i]
        amici = data[i + 1: i + caso + 1]
        for amico in amici:
            if amico > 0:
                massimo += amico
        fun.append(massimo)
        i += caso + 1

    return fun


if __name__ == '__main__':
    valori_divertimento = main()
    for ind, divertimento in enumerate(valori_divertimento):
        print(f"Case #{ind + 1}: {divertimento}")