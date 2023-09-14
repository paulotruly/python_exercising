# ---------------------------------------------------------------------------------------------------------

# Exercício 1

# Um aplicativo meteorológico para obter a temperatura, as condições climáticas
# e se é dia ou noite de uma determinada cidade 

# ---------------------------------------------------------------------------------------------------------

try: 
    Nome_Cidade = (input("Informe o nome da cidade: "))
    Temperatura_Cidade = int(input("Informe a temperatura da cidade: "))
    CondiçãoClimática_Cidade = (input("Informe a condição climática da cidade: "))
    Dia_Cidade = int(input("Está de dia?\n1. Sim\n2. Não"))

    if (Dia_Cidade == 1):
        Dia_Cidade = True
    else: 
        Dia_Cidade = False
        
except ValueError:
    print("Error: Você deveria ter digitado um número!")

print("--------\nCidade: {0}\nTemperatura: {1}°\nCondição climática: {2}\nÉ de dia?: {3}\n--------" .format(Nome_Cidade, Temperatura_Cidade, CondiçãoClimática_Cidade, Dia_Cidade))
