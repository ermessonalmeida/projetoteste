# Contador de Notas em python

notas001 = int(input("Insira o valor da nota: "))
print("valor da nota é: ", notas001)
# notas de 100
notas100 = notas001 // 100
notas001 = notas001 % 100

notas050 = notas001 // 50
notas001 = notas001 % 50

notas020 = notas001 // 20
notas001 = notas001 % 20

notas010 = notas001 // 10
notas001 = notas001 % 10

notas005 = notas001 // 5
notas001 = notas001 % 5

notas002 = notas001 // 2
notas001 = notas001 % 2

print(f"{notas100} Notas de 100")
print(f"{notas050} Notas de 50")
print(f"{notas020} Notas de 20")
print(f"{notas010} Notas de 10")
print(f"{notas005} Notas de 5")
print(f"{notas002} Notas de 2")
print("Segue o Resultado da sua divisão")
