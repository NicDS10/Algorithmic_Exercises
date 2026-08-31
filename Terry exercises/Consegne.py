# Un furgone deve portare al mercato del pesce che arriva ogni minuto al porto,
# impiegando un minuto ad andare e uno a tornare, quindi impiegando 2 minuti totali per le consegne.
# Si pagano due penali: una di P euro per ogni minuto in cui il pesce è arrivato ma il furgone
# non si trovava al porto ed è stato al sole; la seconda di 1 euro per ogni minuto in cui il pesce
# si trovava al porto ma non è partito per il mercato.
# Bisogna calcolare quando far partire il furgone per pagare il meno possibile,
# e restituire il pagamento minimo.

from collections import deque
import sys

# Aumentiamo il limite di ricorsione e buffer I/O per grandi input
sys.setrecursionlimit(200000)

def solve(N, P):
  INF = float('inf')
  dp = [INF] * (N + 2)
  dp[0] = 0

  # Deque memorizza tuple (a, b) della retta y = a*x + b
  lines = deque()

  def check_pop(l1, l2, l3):
    a1, b1 = l1
    a2, b2 = l2
    a3, b3 = l3
    return (b2 - b1) * (a2 - a3) >= (b3 - b2) * (a1 - a2)

  def add_line(m):
    if dp[m] == INF:
      return
    a = -m
    b = dp[m] + (m * m - m) // 2
    new_line = (a, b)

    while len(lines) >= 2 and check_pop(lines[-2], lines[-1], new_line):
      lines.pop()
    lines.append(new_line)

  for j in range(N + 1):
    # Inserimento delle rette valide per il minuto j attuale
    if j == 0:
      add_line(0)
    elif j >= 2:
      add_line(j - 1)

    # Rimozione delle rette non piu ottimali per x = j
    while len(lines) >= 2:
      y1 = lines[0][0] * j + lines[0][1]
      y2 = lines[1][0] * j + lines[1][1]
      if y1 >= y2:
        lines.popleft()
      else:
        break

    best_y = lines[0][0] * j + lines[0][1]
    tax_j = (j * j + j) // 2
    cost = best_y + tax_j

    if j + 1 < N:
      cost += P[j + 1]

    target = j + 1
    if cost < dp[target]:
      dp[target] = cost

  return min(dp[N], dp[N + 1])


def main():
  input_data = sys.stdin.read().split()
  if not input_data:
    return []

  iterator = iter(input_data)
  n_casi = int(next(iterator))

  minimo = []
  for _ in range(n_casi):
    n_penali = int(next(iterator))
    penali = [int(next(iterator)) for _ in range(n_penali)]
    minimo.append(solve(n_penali, penali))

  return minimo


if __name__ == '__main__':
  tasse = main()
  for case, tassa in enumerate(tasse):
    print(f'Case #{case + 1}: {tassa}')