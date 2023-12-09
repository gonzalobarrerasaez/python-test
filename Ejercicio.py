
def eliminar_espacios(string):
    restantes = []  # Lista
    for texto in string:
        if texto != " ":
            restantes.append(texto)
    return restantes


def contar_repeticiones(string):
    conteo = {}
    for letra in eliminar_espacios(string):
        print(letra)
        if letra in conteo:
            conteo[letra] += 1
        if letra not in conteo:
            conteo[letra] = 1
    return conteo


def ordenar_llaves_por_valor(diccionario):
    lista = []
    for llave in diccionario:
        lista.append((diccionario[llave], llave))
    lista.sort(reverse=True)
    return lista


def ordenar_llaves_por_valor(diccionario):
    print(diccionario)
    lista = []
    for llave in diccionario:
        lista.append((diccionario[llave], llave))
        print(lista)
    lista.sort(reverse=True)
    return lista


def tuplas_con_mayor_valor(lista):
    mayor = []
    max_valor = max(lista, key=lambda x: x[1])[1]
    for tupla in lista:
        if tupla[1] == max_valor:
            mayor.append(tupla)
    return mayor

# print(tuplas_con_mayor_valor(
    [("a", 3), ("b", 2), ("c", 4), ("d", 4)]))  # tuplas
