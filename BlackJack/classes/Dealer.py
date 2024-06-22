import random, time, os
from variaveis import cartas, cartas_ja_distribuidas
from classes.Jogador import Jogador

class Dealer:
    def __init__(self) -> None:
        self.mao = []
        self.valor_mao = 0
        self.vitorias = 0
        self.aposta = 0
    

    def distribuir_cartas(self, baralho: list, jogador: Jogador) -> None:
        """
         - Distribui 2 cartas para o jogador e 2 cartas para o Dealer com uma seleção aleatória.
         - Adiciona as cartas escolhidas a lista de cartas já distribuídase remove-as das cartas à serem escolhidas.
         - Adiciona as cartas às mãos dos Jogadores e calcula o valor da mão
        """
        
        carta1 = random.choice(baralho)
        cartas_ja_distribuidas.append(carta1)
        baralho.remove(carta1)
        
        carta2 = random.choice(baralho)
        cartas_ja_distribuidas.append(carta2)
        baralho.remove(carta2)
        
        cartaDealer1 = random.choice(baralho)
        cartas_ja_distribuidas.append(cartaDealer1)
        baralho.remove(cartaDealer1)
        
        cartaDealer2 = random.choice(baralho)
        cartas_ja_distribuidas.append(cartaDealer2)
        baralho.remove(cartaDealer2)
        
        jogador.receber_carta(carta1) 
        jogador.receber_carta(carta2) 
        
        self.mao.append(cartaDealer1)
        self.mao.append(cartaDealer2)
        self.calc_valor_mao()

    def dar_carta(self, baralho: list, jogador: Jogador) -> None:
        """
        Dá apenas uma carta ao jogador e adiciona-la a sua mão com função jogador.receber_carta()
        """
        
        carta = random.choice(baralho)
        cartas_ja_distribuidas.append(carta)
        baralho.remove(carta)

        print("Recebendo carta...")
        time.sleep(3.0)
        os.system('cls')
        jogador.receber_carta(carta)

    def calc_valor_mao(self) -> None:
        """
        Calcula o valor total da mão do Dealer com base nas cartas em sua mão e adiciona o valor a self.valor_mao()
        """

        valor_total = 0
        As = 11 if valor_total <= 10 else 1

        for carta in self.mao:
            simbolo = carta[0]

            if simbolo in ['J', 'Q', 'K']:
                valor_total += 10
           
            elif simbolo == 'A':
                valor_total += As
            
            else:
                valor_total += int(simbolo)
        
        self.valor_mao = valor_total
    
    def valor_mao_atual(self):
        """
        Cacula e imprime o valor da primeira carta da mão do Dealer já que só é revelada uma carta de sua mão
        """

        carta = self.mao[0]
        simbolo = carta[0]
        valor_carta = 0
        
        if simbolo in ['J', 'Q', 'K']:
            valor_carta += 10
           
        elif simbolo == 'A':
            valor_carta += 11
            
        else:
            valor_carta += int(simbolo)
        
        return f"\nPontuação total = {valor_carta}"

    
    def __str__(self) -> str:
        """
        Imprime uma apresentação do Dealer
        """

        return "\nOlá, eu sou o Dealer. Que tal uma partida?"