from stack import Stack
import time
from datetime import datetime

pila1 = Stack()
pila2 = Stack()
pila3 = Stack()

movimiento = 1

''' 
    LOS DISCOS TIENEN QUE SER MENOS QUE 10, 
    YA QUE SI LOS MOVIMIENTOS MINIMOS SON
    MÁS DE 995, PYTHON NOS MOSTRARÁ UNA EXCEPCIÓN
    RELACIONADA CON LAS RECURSIONES. 
    
    ES UNA RESTRICCIÓN/LIMITACIÓN DE PYTHON
'''
discos = 6

minMov = pow(2, discos) - 1

print(f"MOVIMIENTOS MINIMOS: {minMov}")

# UTILIDAD
def moveFromTo(pila_inicial, pila_destino):
    if 0 in [pila_inicial.pick(), pila_destino.pick()]:
        if pila_inicial.pick() != 0:
            pila_destino.add(pila_inicial.pop())
    else:
        if pila_inicial.pick() < pila_destino.pick():
            if pila_inicial.pick() != 0:
                pila_destino.add(pila_inicial.pop())

# UTILIDAD
def print_all():
    print("Pila1")
    pila1.print()
    print("Pila2")
    pila2.print()
    print("Pila3")
    pila3.print()
    print("-------------------------")


# PROGRAMA PRINCIPAL
def hanoi(pila_inicial, pila_auxiliar, pila_destino, discos, movimiento):

    # LLENAR STACK NADA MAS EMPEZAR
    if movimiento == 1:
        if pila_inicial.is_empty():
            for x in reversed(range(1, discos+1)):
                pila_inicial.add(x)
        print_all()

    if movimiento == minMov:
        # time.sleep(1)
        print("BLOQUE IF", datetime.now())
        moveFromTo(pila_inicial, pila_destino)
        print_all()

        # PREVENIR LOOP INFINITO. SE ACABA EL PROGRAMA DANDO EL RESULTADO FINAL
        # NECESARIO A PARTIR DE CUATRO DISCOS
        if(pila3.length() == discos):
            quit()
    else:
        # time.sleep(1)
        print("PRIMER HANOI EN ELSE", datetime.now())

        # INTERCAMBIAMOS TORRES Y DAMOS UN PASO
        ''' 
            PRIMERO SE EJECUTA ESTO TANTAS VECES COMO 
            MOVIMIENTOS MINIMOS HAYA QUE HACER

            VA A ESTAR REALIZANDO PERMUTACIONES Y EMPUJANDO 
            AL PROGRAMA A EJECUTAR EL BLOQUE IF
        '''
        hanoi(pila_inicial, pila_destino, pila_auxiliar, discos, movimiento+1)
        '''
            CUANDO LA LINEA ANTERIOR DA LA CONDICION:
            MOVIMIENTO == MOVIMIENTOS MINIMOS,
            SALTA AL BLOQUE IF Y HACE MOVIMIENTOS

            UNA VEZ SE EJECUTA EL IF, SE ALTERNAN ENTRE LA 
            SEGUNDA LLAMADA A HANOI Y EL IF. 
            
            POR LA MEMOIZACIÓN A CAUSA DE EL ORDEN DE EJECUCIÓN, 
            EL PROGRAMA RECUERDA QUE LA VARIABLE movimiento ESTÁ 
            EN OTRO ESTADO.

            ENTONCES VOLVERÁ A EJECUTAR LA PRIMERA LLAMADA DE 
            HANOI DENTRO DEL ELSE Y LA RECURSIÓN CONTINUA HASTA
            QUE EL TAMAÑO DE LA PILA 3 ES IGUAL A EL NUMERO DE
            DISCOS, LO QUE PROVOCA QUE EL PROGRAMA TERMINE
        '''
        moveFromTo(pila_inicial, pila_destino)
        print_all()
        print("SEGUNDO HANOI EN ELSE", datetime.now())
        hanoi(pila_auxiliar, pila_inicial, pila_destino, discos, movimiento+1)

# COMIENZO DEL PROGRAMA
hanoi(pila1, pila2, pila3, discos, movimiento)
