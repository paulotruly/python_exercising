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
        return ("--------\nCidade: {0}\nTemperatura: {1}°\nCondição climática: {2}\nÉ de dia?: {3}\n--------" .format(self.Nome, self.Temperatura, self.CondiçãoClimática, self.Dia))
    

Paulista = Cidade("Paulista", 23, "Nublado", True)
print(Paulista)
Olinda = Cidade("Olinda", 21, "Ensolarado", True)
print(Olinda)