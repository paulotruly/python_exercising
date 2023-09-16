# ---------------------------------------------------------------------------------------------------------

# Exercício 3

# Sua tarefa é permitir que o usuário insira um valor em dólar (float), assumindo que ele também pode aceitar
# centavos extras (ex. $2,75). Depois disso, converta em moedas. Use um algoritmo que divida o valor em dólares
# entre os quatro tipos de moedas e produza o menor número possível de moedas.

# ---------------------------------------------------------------------------------------------------------

Dólar = int(input("Informe o valor em dólar: "))
Dólar = (Dólar * 4.87)

print("Convertendo para real: {0}".format(Dólar))

UmCentavo = 0.01
CincoCentavos = 0.05
DezCentavos = 0.10
VinteCincoCentavos = 0.25
CinquentaCentavos = 0.50
UmReal = 1.00

# Essas variavéis que criei foi só pra visualizar quantas moedas de cada valor seriam
# necessárias para atingir o total

da = (Dólar/CincoCentavos)
db = (Dólar/DezCentavos)
dc = (Dólar/VinteCincoCentavos)
de = (Dólar/CinquentaCentavos)
df = (Dólar/UmReal)
dg = (Dólar/UmCentavo)

# Tentando fazer um looping que subtraia 1.00 real do valor até sobrar os centavos,
# passando pra 0.5, 0.25, 0.10, 0.05 e 0.01 até que sobre zero. Legal ter uma variável
# que conte quantas vezes cada moeda foi subtraída pra que encerre imprimindo quantas moedas
# de cada foram utilizadas para atingir o valor inicial 

while (Dólar > UmReal):
    Subtraindo = (Dólar - UmReal)
    print(Subtraindo)
    break

        