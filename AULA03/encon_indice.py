def encontrar_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

lista = [10, 20, 30, 40, 50]
print(encontrar_indice(lista, 30))  # Saída: 2
print(encontrar_indice(lista, 100)) # Saída: None