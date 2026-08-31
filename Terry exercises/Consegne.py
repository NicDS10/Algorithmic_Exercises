# Un furgone deve portare al mercato del pesce che arriva ogni minuto al porto,
# impiegando un minuto ad andare e uno a tornare, quindi impiegando 2 minuti totali per le consegne.
# Si pagano due penali: una di P euro per ogni minuto in cui il pesce è arrivato ma il furgone
# non si trovava al porto ed è stato al sole; la seconda di 1 euro per ogni minuto in cui il pesce
# si trovava al porto ma non è partito per il mercato.
# Bisogna calcolare quando far partire il furgone per pagare il meno possibile,
# e restituire il pagamento minimo.

import sys

sys.stdin = open("Terry_tests.py", 'r')

def solve(N, P):
  INF = float('inf')
  dp = [INF] * (N + 2)
  dp[0] = 0

  for m in range(N):
    if dp[m] == INF:
      continue
    low_j = m if m == 0 else m + 1

    for j in range(low_j, N + 1):
      last = min(j, N - 1)
      size = last - m + 1
      tax = size * (j - m) - size * (size - 1) // 2
      cost = dp[m] + tax
      if j + 1 < N:
        cost += P[j + 1]
      target = j + 1
      if cost < dp[target]:
        dp[target] = cost

  return min(dp[N], dp[N + 1])


def main():
  data_momentanea = map(int, sys.stdin.read().split())
  try:
    n_casi = next(data_momentanea)
  except StopIteration:
    return []

  data = list(data_momentanea)
  i = 0
  minimo = []

  while i < len(data):
    n_penali = data[i]
    penali = data[i + 1 : i + 1 + n_penali]

    # Invocazione della funzione DP
    risultato = solve(n_penali, penali)
    minimo.append(risultato)

    i += n_penali + 1

  return minimo

# Questo esempio risulta O(N²) ma lo tengo perché è stato un buon allenamento

if __name__ == '__main__':
  tasse = main()
  for case, tassa in enumerate(tasse):
    print(f"Case #{case + 1}: {tassa}")