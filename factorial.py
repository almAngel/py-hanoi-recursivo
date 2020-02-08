# EJEMPLO DE RECURSIVIDAD

resultado = 0

def factorial(n):
    res = 1
    if n == 0 or n == 1:
        return res
    else:
        return n * factorial(n-1)


num = int(input("Introduce un numero: "))

print(factorial(num))