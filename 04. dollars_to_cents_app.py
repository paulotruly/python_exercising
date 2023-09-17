# ---------------------------------------------------------------------------------------------------------

# Exercício 3

# Sua tarefa é permitir que o usuário insira um valor em dólar (float), assumindo que ele também pode aceitar
# centavos extras (ex. $2,75). Depois disso, converta em moedas. Use um algoritmo que divida o valor em dólares
# entre os quatro tipos de moedas e produza o menor número possível de moedas.

# ---------------------------------------------------------------------------------------------------------

Dólar = float(input("Informe o valor em dólar: "))
Real = float(Dólar * 4.87)
print("Convertendo para real: R${0}".format(Real))

UmCentavo = 1
CincoCentavos = 5
DezCentavos = 10
VinteCincoCentavos = 25
CinquentaCentavos = 50
UmReal = 1

# Tentando fazer um looping que subtraia 1.00 real do valor até sobrar os centavos,
# passando pra 0.5, 0.25, 0.10, 0.05 e 0.01 até que sobre zero. Legal ter uma variável
# que conte quantas vezes cada moeda foi subtraída pra que encerre imprimindo quantas moedas
# de cada foram utilizadas para atingir o valor inicial 

######### TÔ QUASE LÁ HEHEHE !!!!!!!!!!! #########

Real = 49.65
ContandoMoedas = 0

print(Real)

while Real >= 1:
    for contador in range(1, int(Real+1)):
        # print(contador)
        ContandoMoedas = ContandoMoedas + 1
    print("Fim da repetição")
    print("Serão utilizadas {0} moeda/s de 1 real.".format(ContandoMoedas))
    break

Decimais = str(Real-ContandoMoedas)
#print(Decimais[2])
#print(Decimais[3])
Centavos = int(Decimais[2] + Decimais[3])
#print(Centavos)

while Centavos >= CinquentaCentavos:
    Centavos = Centavos - CinquentaCentavos
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1 
    print("Será utilizada {0} moeda de 50 centavos.".format(ContandoCentavos))
    #print(Centavos)
    break

while Centavos >= VinteCincoCentavos:
    Centavos = Centavos - VinteCincoCentavos
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1 
    print("Serão utilizadas {0} moeda/s de 25 centavos.".format(ContandoCentavos))
    #print(Centavos)
    break

while Centavos >= DezCentavos:
    for contador in range(10, Centavos, 10):
        #print(contador)
        ContandoCentavos = ContandoCentavos + 1
    print("Serão utilizadas {0} moeda/s de 10 centavos.".format(ContandoCentavos))
    #print(Centavos)
    break

while Centavos >= CincoCentavos:
    for contador in range(5, Centavos, 5):
        #print(contador)
        ContandoCentavos = ContandoCentavos + 1
    print("Serão utilizadas {0} moeda/s de 5 centavos.".format(ContandoCentavos))
    #print(Centavos)
    break

#while Real < 0:
#    for contador in range(0, int(Real+1), -1):
#        print(contador)
        


