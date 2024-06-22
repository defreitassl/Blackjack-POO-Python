import os
from classes.Rodada import Rodada
from classes.Dealer import Dealer
from classes.Jogador import Jogador
from funcoes import *

#Inicia o jogo e verifica se o jogador quer jogar ou não
os.system('cls')
print("Bem vindo ao Cassino Super!")
print("Que tal uma partida de BlackJack? \n")
entrar = input("Pressione ENTER para entrar ou 0 para sair...")
os.system('cls')

#Condição de inicio de rodada
iniciar = True

#Verifica se o jogador escolheu a opção para sair 
if entrar == '0':
    iniciar = False

#Verifica se ele tem mais de 18 anos
nome, idade = criar_jogador() #Retorna o nome e a idade do jogador para ser criado posteriormente
if int(idade) < 18:
    print(f'\nDesculpe {nome} mas infelizmente você precisa ter 18 anos para poder jogar.')
    iniciar = False

#Se idade for maior que 18, cria 
if int(idade) >= 18:
    jogador_1 = Jogador(nome, idade) #Cria o objeto jogador
    dealer = Dealer() #Cria o objeto Dealer
    rodada = Rodada(jogador_1, dealer) #Cria o objeto Rodada
    os.system('cls')
    print(dealer) #Imprime a apresentação do dealer

    jogar = input("\nPressione ENTER para jogar ou 0 para sair...")

    #Verifica se o jogador esccolheu a opção de iniciar a rodada
    if jogar == '0':
        iniciar = False
    os.system('cls')

#Cria um loop com base na condição iniciar
while iniciar: 

    #Inicia a rodada e retorna as possíveis seguintes ações
    vitoria_jogador, continuar_jogo, encerrar_jogo = rodada.iniciar_rodada()

    #Verifica se o jogador ganhou com um BlackJack e encerra a rodada
    if vitoria_jogador:
        rodada.encerrar_rodada()
        print("Fim da rodada...")
        input()
        os.system('cls')
        encerrar = opcao_encerrar_jogo(jogador_1, dealer, rodada)
        iniciar = verificar_encerrar_jogo(encerrar)
    
    #Verifica se nenhum dos Players ganhou e inicia a função de continuar a rodada
    elif continuar_jogo:
        
        #Continua a rodada e retorna as possíveis seguintes ações
        vitoria_jogador, vitoria_dealer = rodada.continuar_rodada()

        #Se o jogador estourar e ultrapassar 21 pontos ou fazer um "Stand" e estiver com menos pontos que o Dealer, o Dealer ganha e executa o seguinte bloco
        if vitoria_dealer:
            rodada.encerrar_rodada() #Encerra a rodada e reinicia todos os atributos de rodada, começando outra do início
            print("\nFim da rodada...")
            input()
            os.system('cls')
            encerrar = opcao_encerrar_jogo(jogador_1, dealer, rodada) #Verifica se o jogador deseja encerrar o jogo ou começar outra rodada
            iniciar = verificar_encerrar_jogo(encerrar) #Verifica a opção escolhida acima pelo jogador e modifica a condição de início de rodada

        #Se o jogador alcançar 21 pontos, ou fazer um "Stand" e estiver com mais pontos que o Dealer, o Jogador ganha e executa o seguinte bloco 
        elif vitoria_jogador:
            rodada.encerrar_rodada() #Encerra a rodada e reinicia todos os atributos de rodada, começando outra do início
            print("\nFim da rodada...")
            input()
            os.system('cls')
            encerrar = opcao_encerrar_jogo(jogador_1, dealer, rodada) #Verifica se o jogador deseja encerrar o jogo ou começar outra rodada
            iniciar = verificar_encerrar_jogo(encerrar) #Verifica a opção escolhida acima pelo jogador e modifica a condição de início de rodada

        # Se ambos estiverem com 21 pontos ou o jogador decidir para e estiver com a mesma pontuação que o Dealer, é contabilizado um empate e ambos ganham a rodada mas as fichas continuam na banca para a próxima rodada
        elif vitoria_jogador and vitoria_dealer:
            rodada.encerrar_rodada() #Encerra a rodada e reinicia todos os atributos de rodada, começando outra do início
            print("\nFim da rodada...")
            input()
            os.system('cls')
            encerrar = opcao_encerrar_jogo(jogador_1, dealer, rodada) #Verifica se o jogador deseja encerrar o jogo ou começar outra rodada
            iniciar = verificar_encerrar_jogo(encerrar) #Verifica a opção escolhida acima pelo jogador e modifica a condição de início de rodada
    
    # Caso as fichas do Jogador cheguem a 0 o jogo encerra sem chances de começar outra rodada
    else:
        os.system('cls')
        break

print("\nObrigado e até a próxima!")
