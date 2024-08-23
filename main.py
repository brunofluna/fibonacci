#Crie um programa que receba do usuário um número inteiro positivo, e o programa retorne a quantidade de números informada da sequência de Fibonacci.
'''
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci(n - 1)
        next_number = sequencia[-1] + sequencia[-2]
        sequencia.append(next_number)
        return sequencia

n = int(input('Informe um numero a ser calculado: '))
result = fibonacci(n)
print(result)
'''


#programa abaixo da apostila:
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

n = int(input('Informe o número de sequências a ser calculada: '))
for x in range(n):
    print(calcular_fibonacci(x))