def soma(a, b):
	print ("Soma = ", a+b)

def subtrai(a, b):
	print ("Subtração = ", a-b)

def multiplica(a, b):
	print ("Produto = ", a*b)

def divide(a, b):
	# Correção do bug.
        if b==0:
                print("Não é possível dividir por zero")
        else:
                print ("Divisão = ", a/b)

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)
