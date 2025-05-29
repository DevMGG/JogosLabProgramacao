import random


class Forca():
    def _init_(self,nome):
        self.nome=nome
    
    def run(self):
        print("--- FORCA ---")
        print("Adivinhe a palavra! Você tem 6 tentativas.\n")
        
        banco=["python", "computador", "desenvolvedor", "interface", "janela", "programa", "algoritmo", "funcao"]
        palavra = random.choice(banco).upper()
        
        letras_descobertas = ["_" for _ in palavra]
        letras_tentadas=[]
        erros=0
        
        while erros!=6 and "_" in letras_descobertas:
            print("Palavra: ", " ".join(letras_descobertas))
            print("Letras Tentadas: ", ",".join(letras_tentadas))
            print(f"Erros cometidos: {erros}")
            
            letra=str(input("Insira a Letra: ")).upper()
            
            if not letra.isalpha() or len(letra) != 1:
                print("Insira uma letra somente!!")
                print("---------------------------")
                continue
                
            if letra in letras_tentadas:
                print("Esta letra já foi tentada!!")
                print("---------------------------")
                continue
            
            letras_tentadas.append(letra)
            
            for i in range(0, len(palavra), 1):
                if letra == palavra[i]:
                    letras_descobertas[i]=letra
            
            if letra not in palavra:
                print("Essa letra não pertence a palavra!")
                erros+=1
            print("---------------------------")

        if erros==6:
            print("Infelizmente você perdeu!!")
            print("A palavra era: ", palavra)
        else:
            print("Parabéns você venceu!!")
            print("A palavra era: ", palavra)

jogo = Forca()
jogo.run()