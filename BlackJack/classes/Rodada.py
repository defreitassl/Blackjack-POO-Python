from variaveis import cartas, cartas_ja_distribuidas
import funcoes
from classes.Dealer import Dealer
from classes.Jogador import Jogador

class Rodada:

    def __init__(self, jogador: Jogador, dealer: Dealer) -> None:
        
        self.jogador = jogador
        self.dealer = dealer
        self.baralho = cartas
        self.n_rodada = 1
        self.fichas = 0


    def iniciar_rodada(self) -> str:
        """
         - Verifica se o jogador tem fichas suficientes, para encerrar ou não o jogo, retornando True para encerrar_jogo
         - Defini o prêmio total da rodada através da função definir_aposta_dealer()
         - Dá início a rodada distribuindo as cartas e mostrando as mãos dos jogadores e o prêmio da rodada
         - Verifica se o jogador conseguiu um Blackjack e ganhou a rodada de início retornando True para vitoria_jogador
         - Se não retorna True para continuar_jogo
        """

        vitoria_jogador = False
        continuar_jogo = False
    
        encerrar_jogo = self.jogador.fazer_aposta()
        
        if encerrar_jogo == True:
            return vitoria_jogador, continuar_jogo, encerrar_jogo

        funcoes.definir_aposta_dealer(self.jogador, self.dealer, self)

        funcoes.iniciar_rodada(self)
        self.dealer.distribuir_cartas(self.baralho, self.jogador)
        
        print(f"\nRodada {self.n_rodada}:")
        print(f'\nValendo {self.fichas} fichas.')
        print(f"\nAposta Dealer = {self.dealer.aposta}")
        funcoes.mostrar_mao_jogador(self.jogador.mao)
        
        vitoria_jogador = False
        continuar_jogo = False
        
        if self.jogador.valor_mao == 21:
            vitoria_jogador = True
            print(f"\nJogador: {self.jogador.nome} ganha a rodada com um BlackJack e ganhou {self.fichas} fichas!")

            self.jogador.vitorias += 1
            self.jogador.fichas += self.fichas
            self.fichas = 0
            return vitoria_jogador, continuar_jogo, encerrar_jogo
            
        else:
            continuar_jogo = True
            print(self.jogador.valor_mao_atual()) 
                
            funcoes.mostrar_mao_dealer(self.dealer.mao)
            print(self.dealer.valor_mao_atual())
            return vitoria_jogador, continuar_jogo, encerrar_jogo
    
    
    def continuar_rodada(self):
        """
         - Cria um loop com base na decisão do jogador de pegar mais uma carta ou parar e verificar o vencedor
         - Se ele decide continuar, recebe mais uma carta e então, verifica se o jogador ultrapassou 21 pontos, alcançou 21 pontos ou nenhuma das opções
         - Se nenhuma das opções acontece, o loop é reiniciado, dando ao jogador a opção de continuar ou parar de novo e assim sucessivamente
         - Se o jogador ultrapassa os 21 pontos, retorna True para vitoria_dealer, mas se ele alcança os 21 pontos, retorna True para vitoria_jogador
         - Se o jogador decide parar o jogo, é então verificado a condição de vitória, vencendo quem possui mais pontos
        """

        acao = funcoes.acao_continuar_rodada(self)

        while acao == 1:
            self.dealer.dar_carta(self.baralho, self.jogador)

            print(f"\nRodada {self.n_rodada}")
            funcoes.mostrar_mao_jogador(self.jogador.mao)
            print(self.jogador.valor_mao_atual())
            
            vitoria_dealer, continuar_jogo = self.jogador.verificar_valor_max()
            vitoria_jogador = False

            if not vitoria_dealer:
                funcoes.mostrar_mao_dealer(self.dealer.mao)
                print(self.dealer.valor_mao_atual())

                if self.jogador.valor_mao == 21:
                    vitoria_jogador = True
                    continuar_jogo = False
                    print(f"\nJogador {self.jogador.nome} ganhou a rodada com exatos 21 pontos e ganhou {self.fichas} fichas!")

                    self.jogador.vitorias += 1
                    self.jogador.fichas += self.fichas
                    self.fichas = 0
                    return vitoria_jogador, vitoria_dealer
                
                elif continuar_jogo:

                    acao = funcoes.acao_continuar_rodada(self)
            
            else:
                print(f"\nMão do Dealer: ")
                for carta in self.dealer.mao:
                    simbolo = carta[0]
                    naipe = carta[1]
                    print(f" - {simbolo} de {naipe}")
                
                print(f"\nDealer ganhou a rodada com {self.dealer.valor_mao} pontos e ganhou {self.fichas} fichas!")                
                
                self.dealer.vitorias += 1
                self.fichas = 0
                return vitoria_jogador, vitoria_dealer
        
        else:
            vitoria_jogador, vitoria_dealer = self.verificar_vencedor()
            return vitoria_jogador, vitoria_dealer
    
    def encerrar_rodada(self) -> None:
        """
        Encerra a rodada, incrementando 1 no número da rodada e resetando todos os atributos de rodada, como mão dos jogadores, cartas já distribuídas e valor da mão dos Players
        """

        self.n_rodada += 1
        
        self.jogador.mao.clear()
        self.dealer.mao.clear()

        for carta in cartas_ja_distribuidas:
            cartas.append(carta)
        
        cartas_ja_distribuidas.clear()

        self.jogador.valor_mao = 0
        self.dealer.valor_mao = 0

        self.fichas = 0
    
    def verificar_vencedor(self):
        """
         - Calcula o total de pontos dos Players e verifica quem tem mais pontos, ou se foi empate
         - Retorna True para vitoria_jogador ou vitoria_dealer caso algum ganhe, ou retorna True para ambos caso seja empate
        """

        vitoria_jogador = False
        vitoria_dealer = False

        self.dealer.calc_valor_mao()
        self.jogador.calc_valor_mao()
        
        if self.dealer.valor_mao > self.jogador.valor_mao:
            vitoria_dealer = True
            print(f"\nDealer ganhou a rodada com {self.dealer.valor_mao} pontos e ganhou {self.fichas} fichas!")
            
            self.dealer.vitorias += 1
            self.fichas = 0

            return vitoria_jogador, vitoria_dealer
        
        elif self.jogador.valor_mao > self.dealer.valor_mao:
            vitoria_jogador = True
            print(f"\nPlayer {self.jogador.nome} ganhou a rodada com {self.jogador.valor_mao} pontos e ganhou {self.fichas} fichas!")
            
            self.jogador.vitorias += 1
            self.jogador.fichas += self.fichas
            self.fichas = 0

            return vitoria_jogador, vitoria_dealer
        
        else:
            vitoria_dealer = True
            vitoria_jogador = True
            print(f"\nEmpate! Ambos ficaram com {self.jogador.valor_mao} pontos...")
            self.dealer.vitorias += 1
            self.jogador.vitorias += 1

            return vitoria_jogador, vitoria_dealer
        
    
    def __str__(self) -> str:
        return f"""
            RODADA n{Rodada.rodada}
            JOGANDO:
             - JOGADOR N_1: {self.jogador.nome}
             - DEALER
        """