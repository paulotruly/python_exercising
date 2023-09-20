# ---------------------------------------------------------------------------------------------------------

# Exercício 3

# Sua tarefa é permitir que o usuário insira um valor em dólar (float), assumindo que ele também pode aceitar
# centavos extras (ex. $2,75). Depois disso, converta em moedas. Use um algoritmo que divida o valor em dólares
# entre os quatro tipos de moedas e produza o menor número possível de moedas.

# ---------------------------------------------------------------------------------------------------------

dolar = float(input("Informe o valor em dólar: "))
real = float(dolar * 4.87)
print("Convertendo para real: R${0}".format(real))

centavos = int((real - int(real)) * 100 + 0.5) 

contandoMoedas = 0

# Contando quantas moedas de 1 real serão necessárias

contando_umreal = int(real)

while contando_umreal >= 1:
    contando_umreal -= 1
    contandoMoedas += 1 

if contandoMoedas > 0:
    print("Serão necessárias {0} moeda/s de 1 real. ".format(contandoMoedas))

if centavos > 0:
    print("Centavos: {0}".format(centavos))
    
moedas = [50, 25, 10, 5, 1]
nome_moedas = ['de 50 centavos', 'de 25 centavos', 'de 10 centavos', 'de 5 centavos', 'de 1 real']

for i in range(len(moedas)):
    qtd_moedas = centavos//moedas[i]
    if qtd_moedas > 0:
        print("Serão utilizadas {0} moeda/s {1}".format(qtd_moedas, nome_moedas[i]))
        centavos %= moedas[i]
    
print("Centavos que sobram: {0}".format(centavos))