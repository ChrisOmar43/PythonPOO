import random

def busqueda_lineal(lista, objetivo, numero_de_pasos = 0):
    match = False

    for elemento in lista:

        numero_de_pasos += 1
        if elemento == objetivo:
            match = True
            break

    return (match, numero_de_pasos)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    pasos = 0
    encontrado = busqueda_lineal(lista, objetivo, pasos)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta "} en la lista')
    print(f'Los pasos necesarios fueron {pasos}')