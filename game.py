def menu():
    continuar = 1
    while continuar:
        continuar = int(input("0. Sair\n1. Jogar novamente\n"))
        if continuar:
            for i in range(3):
                for j in range(3):
                    board[i][j] = 0
            game()
        else:
            print("Saindo....")
def game():
    jogada = 0
    while ganhou() == 0 and deu_velha() == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha = int(input("\nLinha: "))
        coluna = int(input("Coluna: "))
        if board[linha -1][coluna-1] == 0:
            if (jogada%2+1)==1:
                board[linha - 1][coluna-1] = 1
            else:
                 board[linha - 1][coluna-1] = -1
        else:
            print("Nao esta vazio")
            jogada -= 1
        if ganhou():
            print("Jogador ", jogada%2+1, " ganhou apos ", jogada+1, " rodadas")
        if deu_velha():
            print("Jogo empatado")
        jogada += 1
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]
        if soma == 3 or soma == -3:
            return 1
    #checando colunas
    for j in range(3):
        soma = board[1][j] + board[2][j] + board[0][j]
        if soma == 3 or soma == -3:
            return 1
    #checando diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1
    return 0
def deu_velha():
    numero_de_espacos_vazios = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                numero_de_espacos_vazios += 1
    if numero_de_espacos_vazios == 0:
        return 1
    return 0
            
def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(' X ', end=' ')
            elif board[i][j] == -1:
                print(' O ', end=' ')
        print()
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
menu()