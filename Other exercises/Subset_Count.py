# Esercizio difficile, ti vengono dati in input prima di tutto il numero di casi che ci saranno,
# poi il numero di elementi da analizzare e la differenza massima in valore assoluto tra gli elementi
# di due sottoinsiemi A e B creati dal gruppo, di cui poi dovremo calcolare la somma del numero di elementi
# che costituiscono entrambi, per ogni caso
import sys

def main():
    input = list(map(int, sys.stdin.read().split()))
    results = []
    i = 1
    while i < len(input[1:]):
        elem = 0
        num = input[i]
        differenza = input[i + 1]
        group = input[i + 2 : i + num + 2]
        group.sort()
        possibili_comb = []

        for indice, elem in enumerate(group):
            conta = 0
            while (indice + conta) < len(group) and group[indice + conta] <= (group[indice] + differenza):
                conta += 1
            possibili_comb.append((conta, indice + conta - 1))

        n = len(possibili_comb)
        miglior_da = [0] * n
        miglior_da[n - 1] = possibili_comb[n - 1][0]
        for k in range(n - 2, -1, -1):
            miglior_da[k] = max(possibili_comb[k][0], miglior_da[k + 1])

        migliore_risposta = 0
        for lunghezza, fine in possibili_comb:
            if fine + 1 < len(group):
                candidato = lunghezza + miglior_da[fine + 1]
            else:
                candidato = lunghezza
            migliore_risposta = max(migliore_risposta, candidato)
        results.append(migliore_risposta)

        i += num + 2

    return results


if __name__ == '__main__':
    risultati = main()
    for risultato in risultati:
        print(risultato)