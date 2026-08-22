# Un two pointer è un metodo per evitare algoritmi da n², in cui è necessario usare due for annidati per esempio
# per cercare due o più elementi in un iterabile che rispecchiano certe condizioni.
# Con un two pointer, si usano due variabili che partono rispettivamente dall'inizio e dal fondo,
# vengono confrontate e in base al risultato una delle due cresce o diminuisce. Per esempio:

def somma_11():
    nums = [8, 2, 1, 7, 6, 5, 8, 9, 12]
    nums.sort()
    grow = 0
    fall = len(nums) - 1
    
    while grow <= fall:
        if nums[grow] + nums[fall] == 11:
            return True
        elif nums[grow] + nums[fall] > 11:
            fall -= 1
        else:
            grow += 1
    
    return False

if __name__ == '__main__':
    print(somma_11())
