# Un furgone deve portare al mercato del pesce che arriva ogni minuto al porto,
# impiegando un minuto ad andare e uno a tornare, quindi impiegando 2 minuti totali per le consegne.
# Si pagano due penali: una di P euro per ogni minuto in cui il pesce è arrivato ma il furgone
# non si trovava al porto ed è stato al sole; la seconda di 1 euro per ogni minuto in cui il pesce
# si trovava al porto ma non è partito per il mercato.
# Bisogna calcolare quando far partire il furgone per pagare il meno possibile,
# e restituire il pagamento minimo.

import sys

sys.stdin = open('Terry_tests.py', 'r')

def main():
    data_momentanea = map(int, sys.stdin.read().split())
    n_casi = next(data_momentanea)
    data = list(data_momentanea)
    i = 0
    minimo = []
    # si può osservare che il furgone deve partire sempre alla fine, ma è necessario decidere quando prima
    while i < len(data):
        n_penali = data[i]
        penali = data[i + 1: i + n_penali + 1]
        furgone = "resta"
        pen_tempo = 0
        pen_momentanea = 0
        pen_sole = 0
        pacchi_attendenti = 0

        # calcoliamo gli indici in cui far partire il furgone e le spese; una strategia potrebbe essere
        # che se la penale dopo è di 1 lo faccio partire,  così non si accumulano troppo le penali di attesa (pen_temp)

        # buona per piccoli casi specifici, ma non corretta perché bisogna tenere conto anche dei casi futuri
        # per determinare se partire o no
        for ind, penale in enumerate(penali):
            if furgone == "resta":
                if ind != n_penali - 2 and (ind == n_penali - 1 or penali[ind + 1] <= pacchi_attendenti + 1):
                    furgone = "in viaggio"
                    pen_tempo += pen_momentanea
                    pacchi_attendenti = 0
                    pen_momentanea = 0
                else:
                    pacchi_attendenti += 1
                    pen_momentanea += pacchi_attendenti
            else:
                pen_sole += penali[ind]
                pacchi_attendenti += 1
                pen_momentanea += pacchi_attendenti
                furgone = "resta"

        minimo.append(pen_tempo + pen_sole)

        i += n_penali + 1

    return minimo

# per provare veramente, dovrei tentare con le disposizioni con ripetizione tutti i casi possibili tenendo conto
# dei vincoli, e tenere il risultato minore ottenuto. Questa è la DP: Programmazione Dinamica

if __name__ == '__main__':
    tasse = main()
    for case, tassa in enumerate(tasse):
        print(f"Case #{case + 1}: {tassa}")