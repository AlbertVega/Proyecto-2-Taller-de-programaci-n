import random
import time

start_time = time.time()

def quick_sort(lista):
    quick_sort_auxiliar(lista, 0, len(lista) - 1)

def quick_sort_auxiliar(lista, inicio, fin):
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)

        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)

def particionar(lista, inicio, fin):
    pivote = lista[inicio]

    izquierda = inicio + 1
    derecha = fin
    terminado = False

    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1

        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1

        if derecha < izquierda:
            terminado = True
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

    return derecha


numeros = random.sample(range(0,100000), 10000)

quick_sort(numeros)

end_time = time.time() - start_time

print(end_time)
