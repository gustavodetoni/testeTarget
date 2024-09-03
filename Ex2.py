def pertence_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    while a < n:
        a, b = b, a + b

    return a == n

numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência.")
else:
    print(f"O número {numero} NÃO pertence à sequência.")

