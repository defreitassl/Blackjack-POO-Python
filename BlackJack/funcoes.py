import time
import os

def criar_jogador() -> tuple:
    """
    Cria dois inputs para adição de nome e idade do Jogador e retorna-os
    """

    print("\nCADASTRO DE JOGADOR:")
    nome = input("\nJogador 1, insira seu nome ou apelido: ")
    idade = input(f"\n{nome} qual a sua idade?: ")
    return nome, idade


def iniciar_jogo() -> str:
    """
    Cria um input para o Jogador escolher se deseja jogar ou sair e retorna True ou False com base nisso
    """

    jogar = input("\nPressione ENTER para jogar ou 0 para sair...")

    if jogar == '0':
        return False
    else:
        return True


def iniciar_rodada(rodada: object) -> None:
    """
    Imprime informações sobre a ação que está sendo executada no momento 
    """

    print(f"\nRodada {rodada.n_rodada}:")
    print("O Dealer está destribuindo as cartas...")
    time.sleep(5.0)
    os.system('cls')


def acao_continuar_rodada(rodada: object) -> int:
    """
    Cria um menu de escolhas para o jogador pegar mais uma carta ou parar a rodada e verificar o vencedor
    """

    while True:
        print(f""" 
PEGAR CARTA: [1]
PARAR AGORA: [2]
              """)
        acao = input(f"Jogador {rodada.jogador.nome}, deseja pegar mais uma carta ou parar?: ")
        
        try:
            if acao in '12':
                os.system('cls')
                return int(acao)
        except:
            print("Insira um número válido.(1/2)")
            input()
            os.system('cls')


def mostrar_mao_jogador(mao: list):
    """
    Imprime a mão do jogador mostrando suas cartas
    """

    print(f'\nSuas mão da vez é: ')

    for carta in mao:
        simbolo = carta[0]
        naipe = carta[1]
        
        print(f" - {simbolo} de {naipe}")

def mostrar_mao_dealer(mao: list):
    """
    Imprime a mão do Dealer escondendo uma dsa cartas
    """

    carta = mao[0]
    simbolo = carta[0]
    naipe = carta[1]

    print(f'\nMão do Dealer: ')
    print(f" - {simbolo} de {naipe}")
    print(f" - ???")

def opcao_encerrar_jogo(jogador: object, dealer: object, rodada: object):
    """
    Verifica se o jogador deseja encerrar a partida, e se sim, imprime as estatísticas na tela
    """

    while True:
        acao = input(f"\n{jogador.nome} deseja encerrar sua partida?: ")

        try:
            if acao.lower() == 'sim':
                os.system('cls')
                print(f"""
    
PARTIDA ENCERRADA.
    RESULTADOS:
        RODADAS JOGADAS:
            {rodada.n_rodada - 1}
        
        RODADAS VENCIDAS:   
            Dealer: {dealer.vitorias}
            Player1 {jogador.nome}: {jogador.vitorias}

        FICHAS GANHAS:
            Player1 {jogador.nome}: {jogador.fichas}

                    """)
                input()
                os.system('cls')
                return True

            elif acao.lower() == 'nao' or acao.lower() == 'não':
                print("Ok. Continuando jogo...")
                time.sleep(2.0)
                os.system('cls')
                return False
        
        except:
            print('Responda apenas com "Sim" ou "Não".')
            input()
            os.system('cls')

def verificar_encerrar_jogo(encerrar: bool):
    """
    Verifica e opção escolhida na função opcao_encerrar_jogo() é True ou False e então modifica a condição de iniciar outra rodada
    """

    if encerrar == True:
        iniciar = False
        return iniciar
    elif encerrar == False:
        iniciar = True
        return iniciar

def definir_aposta_dealer(jogador: object, dealer: object, rodada: object):
    """
    Define a aposta do Dealer com base na aposta escolhida pelo jogador e adiciona a soma das fichas apostas por ambos ao prêmio total da rodada
    """

    dealer.aposta = jogador.aposta * 1.5
    rodada.fichas = jogador.aposta + dealer.aposta