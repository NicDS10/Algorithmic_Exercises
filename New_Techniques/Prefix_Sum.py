# La Prefix Sum è una tecnica che permette di calcolare la somma dei valori di un array
# dato un range, senza dover ripetere il procedimento, ma creando una lista che immagazzina
# la somma fino a quel momento per ogni indice, con O(N), ma che permette di prendere qualsiasi
# somma in calcoli futuri con la formula p[r] - p[l-1].

arr = (1, 5, 8, 4, 6, 3, 5, 9, 6, 2, 1, 3, 3, 7, 7, 8, 9, 10)

p = [arr[0]] # la lista della Prefix Sum
for i in arr[1:]:
    p.append(p[-1] + i)

# è a tutti gli effetti una bottom-up
# p = [1, 6, 14, 18, 24, 27, 32, 41, 47, 49, 50, 53, 56, 63, 70, 78, 87, 97]

# se vogliamo la somma dal numero 5 al 10:
somma_5_10 = p[10] - (p[5 - 1])
print(somma_5_10)

# In alternativa, per far sì che se indichiamo il quinto numero non prenda il sesto,
# mettiamo uno 0 come primo numero in p

p_sum = [0]
for i in arr:
    p_sum.append(p_sum[-1] + i)

somma_quinto_decimo = p_sum[10] - (p_sum[5 - 1])
print(somma_quinto_decimo)

# Alla fine, la prefix sum ci permette di calcolare prima le somme, e ogni volta che abbiamo bisogno della somma
# di un range di un array, non dobbiamo ricalcolarla da capo, ma ci basta la formula p[r] - p[l-1],
# portando la somma a O(1).


## La versione migliore da usare è la combinazione dei due esempi, ovvero creare
# la lista come nel secondo ma prendere i numeri come nel primo, perché altrimenti
# se chiedesse come left lo 0, prenderebbe -1 cioè l'ultimo, invece che il primo

p_sum_final = [0]
for i in arr:
    p_sum_final.append(p_sum_final[-1] + i)

somma_5_10_finale = p_sum_final[10 + 1] - (p_sum_final[5])
# prendo il numero 10, partendo da 0, e il numero 5, indicando con quei numeri
# quelli della lista originale, che corrispondono all'unidesimo e sesto in p.
# La formula è quindi p[r+1] - p[l]

print(somma_5_10_finale)