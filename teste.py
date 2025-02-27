def soma(a, b): # def soma(a, b) ---- É a variável
    return a + b # Aqui ele aprende que vamos fazer uma soma

n1 = 5  # Aqui eu escolho os números
n2= 4   # Aqui eu escolho o outro numero 
r=soma(n1, n2) # Seria a operação final n1= a = 5 / n2= b = 4
print(r) 




def função(numero):
    if numero % 2 == 0:
        return "par"      #função --- condição --- resultado
    else:
        return "impar"
    
numero = 12
resultado = função(numero)
print(resultado)  




numeros = [10, 20]
maior_numero = numeros[0]
for nume in numeros:
    if nume > maior_numero:
        maior_numero = nume
print(maior_numero)



tabuada = 5
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))




soma = sum(range(1,101))
print(soma)










