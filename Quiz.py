class Questao:
    def __init__(self, texto):
        self.texto = texto
        self.respostas = []
        self.alternativa_correta = ""

class Perguntas:
    def __init__(self):
        self.questoes = []

    def add_questao(self, pergunta):
        self.questoes.append(Questao(pergunta))

    def add_respostas(self, indice, resposta, alternativa_correta):
        self.questoes[indice].respostas.append(resposta)
        self.questoes[indice].alternativa_correta = alternativa_correta.upper()

    def mostrar_questao(self):
        pontuacao = 0
        for i, q in enumerate(self.questoes):
            print(f"Pergunta {i+1}: {q.texto}")
            print("")
            print ("Alternativas:")
            for resposta in q.respostas:
                print (resposta)
            
            user_alternative = input ("Digite a alternativa correta: ").strip().upper()
            print ("")
            if user_alternative != q.alternativa_correta:
                print ("Que pena! Você errou :(")
                print (f"A resposta correta era {q.alternativa_correta}")
                print (f"Pontuação: {pontuacao}")
                print ("")
                print ("-------------------------------------------------------------")
                print ("")
                continue
                    
            print ("Parabéns! Você acertou!")
            pontuacao += 1
            print (f"Pontuação: {pontuacao}")
            print ("")
            print ("-------------------------------------------------------------")
            print ("")
            continue

        else:
            print (f"Jogo encerrado! Essa foi sua pontuação final: {pontuacao}/{len(self.questoes)}")

quiz = Perguntas()
quiz.add_questao("Quem descobriu o Brasil?")
quiz.add_respostas(0, [
    'A) Pedro Álvares Cabral',
    'B) Cristóvão Colombo',
    "C) Dom Pedro II",
    "D) Zumbi dos Palmares",
    "E) Pero Vaz de Caminha"
], "A")

quiz.add_questao("Quantos estados o Brasil possui?")
quiz.add_respostas(1, [
    "A) 25",
    "B) 15",
    "C) 26",
    "D) 31",
    "E) 18"
], "C")

quiz.add_questao("Em Python, como incrementamos o valor 1 em uma variável?")
quiz.add_respostas(2, [
    "A) var =+ 1",
    "B) var ++ 1",
    "C) var += var",
    "D) var += 1",
    "E) var ++"
], "D")

quiz.mostrar_questao()