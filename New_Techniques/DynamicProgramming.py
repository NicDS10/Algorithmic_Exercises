# La programmazione dinamica è una tecnica molto potente che si basa sul salvare i risultati
# mentre si esegue una recursione (Memoization, non memorization),
# o salvarli durante un ciclo iterativo (Bottom-Up), per non ripetere calcoli non necessari,
# e far passare un algoritmo da O(2^n) a O(n)

## ESEMPI:

import time
import sys

# Fibonacci con solo recursione

def fib_lento(n):    # n rappresenta il numero della sequenza di fibonacci che ci interessa ottenere
    if n == 1 or n == 2:    # caso base, se è 1 o 2 ritorna 1, perché i primi due sono sempre 1
        return 1
    return fib_lento(n - 1) + fib_lento(n - 2)

print(fib_lento(5), "\n")
time.sleep(1)
print(fib_lento(10), "\n")
time.sleep(1)
print(fib_lento(20), "\n")
time.sleep(1)
print(fib_lento(40), "\n")
time.sleep(1)
print("------------------------")

# Fibonacci con Memoization

def fib_memo(n, memo=None):
    if memo is None:
        memo = [None] * (n + 1)
    if n == 1 or n == 2:
        memo[n] = 1
        return memo[n]
    elif memo[n] is not None:
        return memo[n]
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

print(fib_memo(5), "\n")
time.sleep(1)
print(fib_memo(10), "\n")
time.sleep(1)
print(fib_memo(20), "\n")
time.sleep(1)
print(fib_memo(40), "\n")
time.sleep(1)
print(fib_memo(80), "\n")
time.sleep(1)
print("------------------------")

# Fibonacci con Bottom-Up
def fib_bu(n):
    if n == 1 or n == 2:
        return 1
    tabulation = [None] * (n + 1)
    tabulation[1] = 1
    tabulation[2] = 1
    for i in range(3, n + 1):
        tabulation[i] = tabulation[i - 1] + tabulation[i - 2]
    return tabulation[n]

print(fib_bu(5), "\n")
time.sleep(1)
print(fib_bu(10), "\n")
time.sleep(1)
print(fib_bu(20), "\n")
time.sleep(1)
print(fib_bu(40), "\n")
time.sleep(1)
print(fib_bu(80), "\n")
time.sleep(1)
print(fib_memo(200), "\n")
time.sleep(1)
print(fib_memo(400), "\n")
time.sleep(1)
print(fib_memo(800), "\n")
time.sleep(1)
print(fib_memo(1000), "\n")
time.sleep(1)

sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(100000)

print(fib_bu(100000), "\n")
print("Questo è il potere della dp!")