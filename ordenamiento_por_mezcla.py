import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2 
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer las sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda} derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera tu lista?: '))
    lista = [random.randint(1,100) for i in range(tamaño_de_lista)]
    print(f'Tu lista random es: {lista}')
    print('-' * 20)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(f'Tu lista ordenada es: {lista_ordenada}')