import random

class AdivinheoNumero:
    def __init__(self, nome):
        self.nome = nome  
        
    def run(self):
        print("\n")
        
        print("--- ADIVINHE O NUMERO!! ---")
        print("O objetivo do jogo é adivinhar o numero com o menor número de chutes que você conseguir!")
        print("Boa sorte!!\n")
        
        print("---------------------------------------\n")
        
        numero = random.randint(1,100)
        choose =int(input("Insira um número de 1 a 100!\n"))
        contagem=1
        
        while choose != numero:
            
            contagem = contagem + 1
            
            if choose > 100 or choose < 1:
                choose = int(input("Insira um número entre 1 e 100!!!\n"))
                continue
            
            elif choose < numero:
                choose = int(input("Insira um número maior:\n"))
                continue
            
            elif choose > numero:
                choose = int(input("Insira um número menor:\n"))
                continue
            
        print("Parabéns você venceu!!")
        print(f"Com {contagem} chutes")
        
jogo1= AdivinheoNumero("Jogo")
jogo1.run()

