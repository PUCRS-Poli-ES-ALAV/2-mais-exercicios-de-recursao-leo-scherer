def fatorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(4))
# -----------------
def soma_ate_zero(n:int) -> int:
    if n == 0:
        return 0
    else:
        return n + soma_ate_zero(n-1)

print(soma_ate_zero(5))
# -----------------
def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
# -----------------
def soma_intervalo(k:int, j:int) -> int:
    if k > j:
        return "Erro"
    elif k == j-1:
        return 0
    else:
        return k+1 + soma_intervalo(k+1, j)

print(soma_intervalo(9,12))
# -----------------
def isPal(s:str) -> bool:
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPal(s[1:-1])

print(isPal('OSSO'))
print(isPal('AULA'))
# -----------------
def convBase2(n:int) -> str:
    if n < 2:
        return str(n)
    else:
        return convBase2(n//2) + str(n%2)

print(convBase2(10))
# -----------------
def soma_vetor(vetor: list) -> tuple:
    if len(vetor) == 0:
        return 0
    else:
        return vetor[len(vetor)-1] + soma_vetor(vetor[0:len(vetor)-1])

print(soma_vetor([1,2,3,4,5]))
# -----------------
def encontra_maior(vetor: list) -> int:
    if len(vetor) == 1:
        return vetor[0]
    else:
        maior = encontra_maior(vetor[1:])
        if vetor[0] > maior:
            return vetor[0]
        else:
            return maior

print(encontra_maior([1,2,3,4,5,70,1]))