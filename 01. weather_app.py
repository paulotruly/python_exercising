# ---------------------------------------------------------------------------------------------------------

# Exercício 1

# Um aplicativo meteorológico para obter a temperatura, as condições climáticas
# e se é dia ou noite de uma determinada cidade 

# ---------------------------------------------------------------------------------------------------------

class Cidade:

    def __init__(self, Nome="", Temperatura=0, CondiçãoClimática="", Dia = bool):
        self.Nome = Nome
        self.Temperatura = Temperatura
        self.CondiçãoClimática = CondiçãoClimática
        self.Dia = Dia
        
    def GetNome(self):
        return self.Nome
    def SetNome(self, Nome):
        self.Nome = Nome
        
    def GetTemperatura(self):
        return self.Temperatura
    def SetTemperatura(self, Temperatura):
        self.Temperatura = Temperatura
    
    def GetCondiçãoClimática(self):
        return self.CondiçãoClimática
    def SetCondiçãoClimática(self, CondiçãoClimática):
        self.CondiçãoClimática = CondiçãoClimática
        
    def GetDia(self):
        return self.Dia
    def SetDia(self, Dia):
        self.Dia = Dia
        
    def __str__(self):
        return ("Cidade: {0}\nTemperatura: {1}°\nCondição climática: {2}\nÉ de dia?: {3}".format(self.Nome, self.Temperatura, self.CondiçãoClimática, self.Dia))

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

Imprimindo = Cidade(Nome_Cidade, Temperatura_Cidade, CondiçãoClimática_Cidade, Dia_Cidade)
print(Imprimindo)
