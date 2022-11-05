import random
def busqueda_binaria(lista, comienzo, final, objetivo,i):
    i = i + 1

    if objetivo > final:
        return False

    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        print ( lista )
        print ( f'El elemento { objetivo } esta en la lista ')
        print ( f'Se han necesitado {i} pasos' )
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,i)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, i)

if __name__ ==  '__main__' :
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int (input('Que numero quieres encontrar? '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, 0) 
    if (encontrado == False):    print(f'{lista}\n El {objetivo} no esta en la lista')