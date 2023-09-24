# ---------------------------------------------------------------------------------------------------------

# Exercício 4

# Crie um programa de calendário para organizar sua vida diária. Adicione funcionalidade para adicionar
# eventos e lembretes. Estilize seu próprio calendário de acordo com sua necessidade.

# - O usuário pode criar evento
# - O usuário pode editar o evento
# - O usuário pode excluir o evento

# ---------------------------------------------------------------------------------------------------------

from datetime import datetime, timedelta

hoje = datetime.now()
print("A data de hoje é {0}.".format(hoje.strftime("%d/%m/%y")))
print("Que horas são?: {0}:{1}.".format(hoje.hour, hoje.minute))

class Calendário:
    
    def criarEvento(self, nome_evento="", horario_evento="", fhorario_evento=""):
        self.nome_evento = nome_evento
        extraindoi_stringtotime = datetime.strptime(horario_evento, "%H%M")
        extraindof_stringtotime = datetime.strptime(fhorario_evento, "%H%M")
        self.horario_evento = extraindoi_stringtotime.time()
        self.fhorario_evento = extraindof_stringtotime.time()
        print("Evento '{0}' criado com sucesso!".format(self.nome_evento))

    def imprimirEvento(self):
        print("Nome: {0} | Horário: {1} até {2}".format(self.nome_evento, self.horario_evento.strftime("%H:%M"), self.fhorario_evento.strftime("%H:%M")))
        
    def editarHorário(self, horario_evento = "", fhorario_evento = ""):
        extraindoi_stringtotime = datetime.strptime(horario_evento, "%H%M")
        extraindof_stringtotime = datetime.strptime(fhorario_evento, "%H%M")
        self.horario_evento = extraindoi_stringtotime.time()
        self.fhorario_evento = extraindof_stringtotime.time()
        print("Horário do evento alterado com sucesso!")
        
    def editarNome(self, nome_evento = ""):
        self.nome_evento = nome_evento
        print("Nome do evento alterado com sucesso!")
   
aniversário_paulo = Calendário()
aniversário_paulo.criarEvento('Aniversário do Paulo', '1900', '2100')
aniversário_paulo.imprimirEvento()
aniversário_paulo.editarHorário('2100', '2300')
aniversário_paulo.imprimirEvento()
aniversário_paulo.editarNome('Aniversário do Henrique')
aniversário_paulo.imprimirEvento()

# o que falta nesse exercício:
# - nega a adição ao tentar evento em um horário ocupado
# - imprimir todo o calendário 



