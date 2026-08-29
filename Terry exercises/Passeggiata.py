# Durante una passeggiata, ci sono N strade, che Dario deve percorrere tutte.
# Ad ogni passo Dario consuma un panino, che può trovare all'inizio di ogni strada in un chiosco.
# I chioschi possono avere prezzi diversi per i panini, e bisogna calcolare quanto può spendere al minimo
# per percorrere tutti i tratti di strada.

import sys

def main():
    prezzi = []
    input = list(map(int, sys.stdin.read().split()))
    i = 1
    while i < len(input[1:]):
        tratti = input[i]
        percorsi = input[i+1 : i + 1 + tratti]
        costi = input[i + 1 + tratti : i + 1 + tratti * 2]
        num = 0
        minimo = 0
        tot_panini = []
        prezzi_panini = []
        while num < len(costi):
            prezzo = costi[num]
            if num == 0:
                tot_panini.append(prezzo)
                prezzi_panini.append(prezzo * percorsi[num])
            elif prezzo < tot_panini[-1]:
                tot_panini.append(prezzo)
                prezzi_panini.append(prezzo * percorsi[num])
            else:
                prezzi_panini[-1] += tot_panini[-1] * percorsi[num]

            num += 1

        minimo = sum(prezzi_panini)
        prezzi.append(minimo)
        i += tratti * 2 + 1
    return prezzi

# Sarebbe stato meglio calcolare il minimo dei prezzi e ogni volta usare quello
# scorrendoli ma in questo modo è equivalente dato che vado a registrare i minimi
# e usare quelli finché non ne trovo un altro

if __name__ == '__main__':
    caso = 0
    prices = main()
    while caso < len(prices):
        print(f"Case #{caso + 1}: {prices[caso]}")
        caso += 1