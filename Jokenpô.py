import random

class Escolha:
    def __init__(self):
        self.escolhas = [
            "pedra",
            "papel",
            "tesoura"
        ]

        self.userPick = ""
        self.robotPick = ""
        self.userWins = 0
        self.robotWins = 0

    def robot_pick(self):
        self.robotPick = random.choice(self.escolhas)
    
    def user_pick(self, pick):
        if pick not in [1, 2, 3]:
            print ("Digite um número de 1 a 3.")
            return False
        
        self.userPick = self.escolhas[pick - 1]
        return True

    def winner(self):

        if self.robotPick == self.userPick:

            print (f"A máquina jogou {self.robotPick}, empate na rodada!")
            print (f"Placar: Máquina {self.robotWins} x {self.userWins} Usuário")
        
        elif (self.userPick == "pedra" and self.robotPick == "tesoura") or \
            (self.userPick == "papel" and self.robotPick == "pedra") or \
            (self.userPick == "tesoura" and self.robotPick == "papel"):
            self.userWins += 1
            print (f"A máquina jogou {self.robotPick}, vitória do usuário na rodada!")
            print (f"Placar: Máquina {self.robotWins} x {self.userWins} Usuário")
        
        else:
            self.robotWins += 1
            print (f"A máquina jogou {self.robotPick}, vitória da máquina na rodada!")
            print (f"Placar: Máquina {self.robotWins} x {self.userWins} Usuário")
    

def run():
    print ("")
    print ("Bem vindo ao Jokenpô vs Máquina!")
    print ("Você terá 3 opções de jogada, tendo como objetivo, ganhar da máquina.")
    print ("As regras são simples: Pedra ganha de tesoura, tesoura ganha de papel e papel ganha de pedra.")
    print ("Vamos começar!")
    print ("-" * 40)
    print ("")

    escolha_usuario = Escolha()
    rodada = 1

    while True:  

        print (f"Rodada: {rodada}")
        print ("")
        try:
            pick = int(input("Digite 1 para pedra, 2 para papel ou 3 para tesoura: "))

        except ValueError:

            print("Entrada inválida! Digite apenas números.")
            continue

        if not escolha_usuario.user_pick(pick):
            continue
        
        escolha_usuario.robot_pick()
        escolha_usuario.winner()
        rodada += 1

        print ("")
        stop = input ("Deseja continuar jogando? (S/N) ").strip().upper()
        print ("")

        if stop == "N":
            print ("Jogo encerrado!")
            print ("-" * 40)
            break

        elif stop != "S":
            print ("Entrada inválida. Digite S ou N!")
            print ("-" * 40)
            print("")

run()