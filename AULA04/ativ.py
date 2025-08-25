def buble_sort(lista):
    tamanho_lista = len(lista)
    troca = 0

    for i in range(tamanho_lista):
        for j in range(0, tamanho_lista - i - 1):
            if lista[i] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca += 1
               # temp = lista[j]
               # lista[j] = lista[j+1]
               # lista[j+1] = temp
    return lista, troca

lista = [10, 20, 30, 40, 50, 5]
print(buble_sort(lista))

## ORGANIZA OS NÚMEROS DO MENOR AO MAIOR