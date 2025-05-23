class Torre:
    def __init__(self, discos, numero):
        self.numero = numero
        self.discos = discos

    def add_disco(self, destino):
        if not self.discos:
            print("A torre de origem está vazia. Não há discos para mover.")
            return

        if destino.discos and self.discos[-1] > destino.discos[-1]:
            print("Não é possível adicionar um disco maior em cima de um disco menor.")
            return

        destino.discos.append(self.discos.pop())
    

torre1 = Torre([5, 4, 3, 2, 1], 1)
torre2 = Torre([], 2)
torre3 = Torre([], 3)

def exibir_detalhes():
    print(f"Torre 1: {torre1.discos}")
    print(f"Torre 2: {torre2.discos}")
    print(f"Torre 3: {torre3.discos}")

torres = [torre1, torre2, torre3]

def buscar_torre(numtorre):
        for torre in torres:
            if torre.numero == numtorre:
                return torre
        print("Essa Torre não existe! Tente um número de 1 a 3!")
        return None

def run():
    print("Bem vindo à Torre de Hanoi!")
    print("Seu objetivo neste jogo é fazer com que os 5 discos sejam movidos à torre 3, de forma crescente, " \
    "onde 1 é o número do menor disco e 5 do maior.")
    print("É possível movimentar apenas um disco por vez, onde um disco maior nunca pode ficar em cima de um disco menor.")
    print("Selecione a torre de origem e a torre de destino para movimentação das peças.")
    while True:

        contador = -1
        for i in range(100000):
            contador += 1
            print(f"Movimento #{contador}")
            exibir_detalhes()
                
            origem = int(input("Qual a torre de origem? "))
            destino = int(input("Qual a torre de destino? "))
            if origem < 1 or origem > 3 or destino < 1 or destino > 3 or origem == None or destino == None:
                return ("Digite o número da torre entre 1 e 3.")
            
            origem = buscar_torre(origem)
            destino = buscar_torre(destino)
            origem.add_disco(destino)

            if torre3.discos == [5, 4, 3, 2, 1]:
                exibir_detalhes()
                print("Parabéns, você venceu!!")
                break
        
        break

run()