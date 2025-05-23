class Torre:
    def __init__(self, discos, numero):
        self.numero = numero
        self.discos = discos

    def add_disco(self, destino):
        if len(self.discos) > 0 and self.discos[-1] < destino.discos[-1]:
            return ("Não é possível adicionar um disco maior em cima de um disco menor.")
        destino.discos.append(self.discos.pop())

    def remover_disco(self):
        if not self.discos:
            return ("Não é possível movimentar o disco pois a torre selecionada está vazia.")
        self.discos.pop()

torre1 = Torre([5, 4, 3, 2, 1], 1)
torre2 = Torre([], 2)
torre3 = Torre([], 3)

def exibir_detalhes():
    print(f"Torre 1: {torre1.discos}")
    print(f"Torre 2: {torre2.discos}")
    print(f"Torre 3: {torre3.discos}")

torres = [torre1, torre2, torre3]

def run():
    print("Bem vindo à Torre de Hanoi!")
    print("Seu objetivo neste jogo é fazer com que os 5 discos sejam movidos à torre 3, de forma crescente.")
    print("É possível movimentar apenas um disco por vez, onde um disco maior nunca pode ficar em cima de um disco menor.")
    print("Selecione a torre de origem e a torre de destino para movimentação das peças.")
    while True:

        exibir_detalhes()
        
        origem = int(input("Qual a torre de origem?"))
        destino = int(input("Qual a torre de destino?"))

        for Torre in torres:
            if destino != Torre.numero or origem != Torre.numero:
                return ("Digite números de torre de 1 a 3.")
            destino = Torre.numero
            origem = Torre.numero
            destino.add_disco()
            origem.remover_disco()

        if torre3.discos == [5, 4, 3, 2, 1]:
            break



    
