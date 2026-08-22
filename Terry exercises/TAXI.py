import sys

def main():
    taxi = []
    casi_test = list(map(int, sys.stdin.read().split()))
    conta_persone = 0
    num_persone = -1
    for indice, caso in enumerate(casi_test[1:]):
        if conta_persone == num_persone:
            taxi.append(len(set(casi_test[indice - num_persone + 2: indice + 2])))
            conta_persone = 0
        elif conta_persone == 0:
            num_persone = caso
            conta_persone += 1
        else:
            conta_persone += 1
    return taxi

if __name__ == '__main__':
    risultati = main()
    for index, elemento in enumerate(risultati):
        print(f"Case #{index+1}: {elemento}")