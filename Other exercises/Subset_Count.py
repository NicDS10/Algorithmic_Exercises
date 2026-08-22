# Esercizio difficile, ti vengono dati in input prima di tutto il numero di casi che ci saranno,
# poi il numero di elementi da analizzare e la differenza massima in valore assoluto tra gli elementi
# di due sottoinsiemi A e B creati dal gruppo, di cui poi dovremo calcolare la somma del numero di elementi
# che costituiscono entrambi, per ogni caso
import sys

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    results = []
    i = 1
    
    while i < len(input_data):
        num = input_data[i]
        differenza = input_data[i + 1]
        group = input_data[i + 2 : i + num + 2]
        group.sort()
        
        ranges = []
        for indice in range(len(group)):
            conta = 0
            while (indice + conta) < len(group) and group[indice + conta] <= (group[indice] + differenza):
                conta += 1
            ranges.append((conta, indice + conta - 1))
        
        n = len(ranges)
        best_from = [0] * n
        best_from[n - 1] = ranges[n - 1][0]
        
        for k in range(n - 2, -1, -1):
            best_from[k] = max(ranges[k][0], best_from[k + 1])
        
        best_answer = 0
        for length, end_idx in ranges:
            if end_idx + 1 < len(group):
                candidate = length + best_from[end_idx + 1]
            else:
                candidate = length
            best_answer = max(best_answer, candidate)
        
        results.append(best_answer)
        i += num + 2
    
    return results


if __name__ == '__main__':
    risultati = main()
    for risultato in risultati:
        print(risultato)
