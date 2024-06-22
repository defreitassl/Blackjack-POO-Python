import os
class Jogador:
    def __init__(self, nome: str, idade: int) -> None:
        
        self.nome = nome
        self.idade = idade
        self.mao = []
        self.valor_mao = 0
        self.vitorias = 0
        self.fichas = 500
        self.aposta = 0


    def receber_carta(self, carta: tuple) -> None:
        """
        Adiciona a carta recebida nos argumentos a mão do Jogador e calcula o valor total da mão através de self.calc_valor_mao()        
        """

        self.mao.append(carta)
        self.valor_mao = self.calc_valor_mao()


    def calc_valor_mao(self) -> int:
        """
        Calcula o valor total da mão do Jogador com base em suas cartas e retorna esse valor para ser usado posteriormente
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
        
        return valor_total
    

    def verificar_valor_max(self):
        """
        Verifica se o jogador ultrapassou 21 pontos com base no valor total da sua mão e retorna a condição de encerramento ou continuação de jogo
        """

        vitoria_dealer = False
        continuar_jogo = False
        
        if self.valor_mao > 21:
            vitoria_dealer = True
            print(f"\nVocê estourou a banca com um valor de {self.valor_mao - 21} pontos a mais que o máximo.")
            return vitoria_dealer, continuar_jogo
        else:
            continuar_jogo = True
            return vitoria_dealer, continuar_jogo
    

    def valor_mao_atual(self) -> str:
        """
        Imprime o valor da mão do jogador com Pontuação total
        """
        return f"\nPontuação total =  {self.valor_mao}"

    
    def fazer_aposta(self):
        """
         - Verifica se o jogador possui fichas para apostar
         - Se sim, pergunta quantas fichas ele quer apostar para a próxima rodada e, se válido, adiciona esse valor a self.aposta
         - Se o jogador não tiver fichas suficientes, retorna True para encerrar_jogo
        """

        encerrar_jogo = False

        if self.fichas == 0:
            encerrar_jogo = True
            print("Suas fichas acabaram, boa sorte na próxima!")
            input()
            return encerrar_jogo

        while True:
            os.system('cls')
            print(f"\nVocê tem {self.fichas} fichas.")
            aposta = input("Qual será sua aposta para essa rodada?: ")

            try:
                aposta = int(aposta)
                if (self.fichas - aposta) >= 0: 
                    self.fichas -= aposta
                    self.aposta = aposta
                    break
                else:
                    os.system('cls')
                    print("Você não pode fazer uma aposta maior que a sua quantidadade de fichas.")

            except:
                print("Insira apenas números inteiros válidos!")
        return encerrar_jogo

    def __str__(self) -> str:
        """
        Imprime uma breve apresentação do Jogador
        """
        return f"\nMeu nome é {self.nome} e eu tenho {self.idade} anos."