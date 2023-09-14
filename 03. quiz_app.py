# ---------------------------------------------------------------------------------------------------------

# Exercício 2

# Um aplicativo de quiz que testa seus conhecimentos respondendo perguntas 
# 1. O usuário pode ver uma pergunta com 4 respostas possíveis
# 2. Após selecionar uma resposta, exibe a próxima pergunta ao usuário, faça isso até que o teste termine
# 3. No final o utilizador poderá ver as seguintes estatísticas
#    - Quantas respostas corretas ele obteve
#    - Uma mensagem mostrando se ele "passou" ou "reprovou" no teste

# ---------------------------------------------------------------------------------------------------------

print("----------------------------")
print("Questões sobre a Guerra Fria")
print("----------------------------")

print("A Guerra Fria é o período compreendido entre 1947 a 1991 quando as relações internacionais foram marcadas\npela disputa entre Estados Unidos e União Soviética.\nEste tema é crucial para entender o mundo moderno e muito cobrado no ENEM e nos vestibulares.\nPor isso, preparamos 5 questões com gabarito comentado para você se preparar. Boa sorte!")

Resultado = 0
QuestõesCorretas = 0

print("----------------------------")

print("Questão 1 - Por que o período histórico chamado “Guerra Fria” ganhou este nome?")
print("a) A rivalidade entre EUA e URSS se deu apenas no campo cultural, comercial e político e não bélico.")
print("b) As disputas do mundo bipolar passavam por fortalecer internamente o modelo político sem importar com a opinião exterior.")
print("c) O arsenal de ambas as potências não era suficiente para garantir a destruição do adversário.")
print("d) Não houve enfrentamentos de fogo direto entre os EUA e a URSS, apenas em zonas onde os dois países disputavam sua influência.")

print("----------------------------")

Q1_Resposta = input(("Selecione a resposta correta: "))
if (Q1_Resposta == "d"):
    print("Resposta correta!")
    Resultado = Resultado + 2
    QuestõesCorretas = 0 + 1
else: 
    print("Resposta incorreta!")

print("----------------------------")

print("Questão 2 - Duas organizações militares foram fundadas pela União Soviética e os Estados Unidos com o objetivo de garantir alianças dentro da lógica bipolar que o mundo vivia durante a Guerra Fria.")
print("a) ONU e OTAN.")
print("b) Pacto de Varsóvia e ONU.")
print("c) Pacto de Varsóvia e OTAN.")
print("d) ONU e OEA.")
print("----------------------------")

Q2_Resposta = input(("Selecione a resposta correta: "))
if (Q2_Resposta == "c"):
    print("Resposta correta!")
    Resultado = Resultado + 2
    QuestõesCorretas = 0 + 1
else: 
    print("Resposta incorreta!")
    
print("----------------------------")

print("Questão 3 - Dentre os conflitos que ocorreram por conta da disputa ideológica durante a Guerra Fria podemos citar:")
print("a) Revolução Francesa.")
print("b) Revolução Cubana.")
print("c) Guerra Russo-Japonesa.")
print("d) Guerra Hispano-Americana.")
print("----------------------------")

Q3_Resposta = input(("Selecione a resposta correta: "))
if (Q3_Resposta == "b"):
    print("Resposta correta!")
    Resultado = Resultado + 2
    QuestõesCorretas = 0 + 1
else: 
    print("Resposta incorreta!")
    
print("----------------------------")

print("Questão 4 - A Corrida Espacial foi um dos acontecimentos mais espetaculares da Humanidade, no entanto, o objetivo não era apenas explorar o universo.\nAssinale a alternativa que expressa quais eram outros propósitos da Corrida Espacial:")
print("a) Desenvolver mísseis intercontinentais e construir um escudo que protegesse cada nação dos mísseis do país inimigo.")
print("b) Canalizar o patriotismo e desviar a atenção dos cidadãos para os problemas que decorriam da Guerra Fria.")
print("c) Criar uma central de inteligência e espionagem que permitisse conectar com todos os aliados e combater os inimigos das duas potências.")
print("d) Entender o funcionamento da Terra e de todo o Sistema Solar com o objetivo de colonizá-lo caso ocorresse uma guerra nuclear.")
print("----------------------------")

Q4_Resposta = input(("Selecione a resposta correta: "))
if (Q4_Resposta == "a"):
    print("Resposta correta!")
    Resultado = Resultado + 2
    QuestõesCorretas = 0 + 1
else: 
    print("Resposta incorreta!")

print("----------------------------")

print("Questão 5 - O Chile apresentava uma oportunidade única para demonstrar ao mundo que o socialismo era capaz de triunfar usando via eleitoral e pacífica. Nisto consistia sua atração e sua importância política para todo mundo, especialmente para as forças de esquerda.\nQuais foram as consequências da eleição de Salvador Allende, para a presidência no Chile, em 1970?")
print("a) Instituição de um governo de caráter popular que seria reeleito em 1974.")
print("b) Reconhecimento do governo Allende pelas forças conservadoras tanto interna como externamente.")
print("c) Na América Latina, se verificam eleições de governantes de partidos de esquerda.")
print("d) Nacionalização de empresas estrangeiras e apoio dos Estados Unidos às Forças Armadas chilenas.")
print("----------------------------")

Q5_Resposta = input(("Selecione a resposta correta: "))
if (Q5_Resposta == "d"):
    print("Resposta correta!")
    Resultado = Resultado + 2
    QuestõesCorretas = 0 + 1
else: 
    print("Resposta incorreta!")

print("----------------------------")  
    
print("Questões corretas: {0}".format(QuestõesCorretas))
print("Resultado: {0}".format(Resultado))

if (Resultado >= 7):
    print("Aprovado!")
else:
    print("Reprovado!")

print("Gabarito: d-c-b-a-d")

print("----------------------------")
