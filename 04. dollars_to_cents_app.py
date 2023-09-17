# ---------------------------------------------------------------------------------------------------------

# Exercício 3

# Sua tarefa é permitir que o usuário insira um valor em dólar (float), assumindo que ele também pode aceitar
# centavos extras (ex. $2,75). Depois disso, converta em moedas. Use um algoritmo que divida o valor em dólares
# entre os quatro tipos de moedas e produza o menor número possível de moedas.

# ---------------------------------------------------------------------------------------------------------

## Dólar = float(input("Informe o valor em dólar: "))
## Real = float(Dólar * 4.87)
## print("Convertendo para real: R${0}".format(Real))

UmCentavo = 1
CincoCentavos = 5
DezCentavos = 10
VinteCincoCentavos = 25
CinquentaCentavos = 50
UmReal = 1

######### testando #########

# Erros (muitos)
# Real = 50.05: os centavos contam 4, o WHILE de 5 centavos não é puxado e vai pro de 1 centavo que não funciona também
# Real = 50.10: funciona perfeitamente
# Real = 50.25: funciona perfeitamente
# Real = 50.50: funciona perfeitamente, só dá um erro no "testando centavos" porque não tem condição
# Real = 50.75: funciona mas fica sobrando 1 centavo [?], o WHILE de 1 centavo tá muito errado 
# Real = 50.80: funciona perfeitamente 
# Real = 50.85: funciona mas fica sobrando 1 centavo [?], o WHILE de 1 centavo tá muito errado
# Real = 50.90: funciona perfeitamente 

Real = 50.90
ContandoMoedas = 0
print(Real)

######### 1 real #########

while Real >= 1:
    for contador in range(1, int(Real+1)):
        # print(contador)
        ContandoMoedas = ContandoMoedas + 1
    print("Serão utilizadas {0} moeda/s de 1 real.".format(ContandoMoedas))
    break

######### testando centavos ######### 

Decimais = str(Real-ContandoMoedas)
#print(Decimais[2])
#print(Decimais[3])
Centavos = int(Decimais[2] + Decimais[3])
print("Centavos: {0}".format(Centavos))

######### 50 centavos #########

while Centavos >= CinquentaCentavos:
    Centavos = Centavos - CinquentaCentavos
    Centavos = Centavos + 1
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1
    print("Será utilizada {0} moeda de 50 centavos.".format(ContandoCentavos))
    print("Centavos que sobram: {0}".format(Centavos))
    break

######### 25 centavos #########

while Centavos >= VinteCincoCentavos:
    Centavos = Centavos - VinteCincoCentavos
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1 
    print("Serão utilizadas {0} moeda/s de 25 centavos.".format(ContandoCentavos))   
    print("Centavos que sobram: {0}".format(Centavos))
    break

######### 10 centavos #########

while Centavos >= DezCentavos:
    Centavos = Centavos - DezCentavos
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1
    print("Serão utilizadas {0} moeda/s de 10 centavos.".format(ContandoCentavos))
    print("Centavos que sobram: {0}".format(Centavos))
    break

######### 5 centavos #########

while Centavos == CincoCentavos:
    Centavos = Centavos - CincoCentavos
    ContandoCentavos = 0
    ContandoCentavos = ContandoCentavos + 1
    print("Serão utilizadas {0} moeda/s de 5 centavos.".format(ContandoCentavos))
    print("Centavos que sobram: {0}".format(Centavos))
    break

######### 1 centavo #########

while Centavos >= UmCentavo:
    for contador in range(1, Centavos):
        ContandoCentavos = 0
        ContandoCentavos = ContandoCentavos + 1
    print("Serão utilizadas {0} moeda/s de 1 centavo.".format(ContandoCentavos))
    print("Centavos que sobram: {0}".format(Centavos))
    break

