import time


#implementacion iterativa
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -=1

    return respuesta


#implementacion recursiva
def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)

if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    #print(factorial(n))
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    #print(factorial_r(n))
    factorial(n)
    final = time.time()
    print(final - comienzo)