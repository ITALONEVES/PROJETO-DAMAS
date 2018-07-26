JOGADAS = 1
QUANT_AZUIS = 12
QUANT_VERDES = 12
VAZIO = "      "
AZUL = "AZUL  "
VERDE = "VERDE "
DAMA_AZUL = "DAMA-A"
DAMA_VERDE = "DAMA-V"




cores = {"padrao":"\033[m","verde":"\033[0;30;42m","azul":"\033[0;30;44m", "preto":"\033[0;30;47m"}



def imprimir_tabuleiro ():
    for i in tabuleiro:
        for t in i:
            if t =="AZUL  " or t=="DAMA-A":
                print(cores["azul"],t,cores["padrao"], end=" | ")
            elif t == "VERDE " or t =="DAMA-V":
                print(cores["verde"],t,cores["padrao"], end=" | ")
            else:
                print(cores["preto"],t,cores["padrao"],end=" | ")

        print("\n")


def  mov_das_pecas  (destino_linha, destino_coluna, inicio_linha, inicio_coluna):

    """ESSA FUNÇÃO ANALISA SE O MOVIMENTO DE UMA PEÇA(SEJA ELA AZUL OU VERDE) É VALIDO."""

    global JOGADAS

    # CONDIÇÕES PARA AS PEÇAS AZUL SEREM MOVIMENTADAS
    if JOGADAS % 2 != 0:     #JOGADOR 1 É AS AZUIS
        if destino_linha > inicio_linha and destino_linha - inicio_linha==1 and (destino_coluna - inicio_coluna==-1 or destino_coluna-inicio_coluna==1) and destino_linha != inicio_linha and destino_coluna != inicio_coluna and \
                        tabuleiro[destino_linha][destino_coluna]==VAZIO and tabuleiro[inicio_linha][inicio_coluna]==AZUL:
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = AZUL
            # CONDIÇÃO PARA UMA PEÇA SE TORNAR UMA DAMA AZUL
            if destino_linha == 8:
                tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
        else:
            JOGADAS-=1      #DIMINUI 1 NO NÚMERO DE JOGADAS PARA RETORNAR A JOGADA PARA O JOGADOR QUE TENTOU MOVIMENTAR AS PEÇAS DE FORMA ERRADA.
            print("É A VEZ DE VOCÊ  MOVIMENTAR AS PEÇAS AZUIS E VOCÊ MOVIMENTOU ELAS DE FORMA ERRADA.JOGUE NOVAMENTE!""\n")     #MENSAGEM DE ERRO CASO A PEÇA NÃO POSSA SER MOVIMENTADA.

    # CONDIÇÕES PARA A PEÇA VERDE SER MOVIMENTADA
    elif JOGADAS % 2 == 0:#JOGADOR 2 É AS VERDES
        if destino_linha < inicio_linha and inicio_linha - destino_linha == 1 and((destino_coluna - inicio_coluna==-1) or (destino_coluna-inicio_coluna==1))  and destino_linha != inicio_linha \
                and destino_coluna != inicio_coluna and tabuleiro[destino_linha][destino_coluna] == VAZIO and tabuleiro[inicio_linha][inicio_coluna]==VERDE:
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = VERDE
            # CONDIÇÃO PARA PEÇA SE TORNAR UMA DAMA VERDE
            if destino_linha == 1:
                tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
        else:
            JOGADAS -= 1  #DIMINUI 1 NO NÚMERO DE JOGADAS PARA RETORNAR A JOGADA PARA O JOGADOR QUE TENTOU MOVIMENTAR AS PEÇAS DE FORMA ERRADA
            print("É A VEZ DE VOCÊ  MOVIMENTAR AS PEÇAS VERDES E VOCÊ MOVIMENTOU ELAS DE FORMA ERRADA.JOGUE NOVAMENTE!""\n")  #MENSAGEM DE ERRO CASO A PEÇA NÃO POSSA SER MOVIMENTADA.
def comer_peca_verde (destino_linha, destino_coluna, inicio_linha, inicio_coluna):

    """ESSA FUNÇÃO ANALISA SE A TENTATIVA DO JOGADOR 1 DE COMER UMA PEÇA VERDE DO JOGADOR 2 É VÁLIDA"""

    global JOGADAS
    global QUANT_VERDES

    if JOGADAS % 2 != 0:  #VERIFICA SE A VEZ É REALMENTE DO JOGADOR 1 (PEÇAS AZUIS)
        if inicio_coluna < destino_coluna and inicio_linha< destino_linha and tabuleiro[destino_linha][destino_coluna] ==VAZIO \
                and tabuleiro[inicio_linha + 1][inicio_coluna + 1] == VERDE  or tabuleiro[inicio_linha + 1][inicio_coluna + 1] == DAMA_VERDE\
                and destino_coluna-inicio_coluna==2 and destino_linha-inicio_linha==2:    #CONDIÇÕES PARA COMER UMA PEÇA VERDE PARA O LADO DIREITO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha + 1][inicio_coluna + 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = AZUL
            QUANT_VERDES-=1
            if destino_linha == 8:     #CONDIÇÃO PARA A PEÇA AZUL VIRAR UMA DAMA-AZUL NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA VERDE PARA O LADO DIREITO
                tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL

        elif inicio_coluna > destino_coluna  and inicio_linha< destino_linha and tabuleiro[inicio_linha + 1][inicio_coluna - 1] == VERDE \
                or tabuleiro[inicio_linha + 1][inicio_coluna - 1] == DAMA_VERDE and tabuleiro[destino_linha][destino_coluna]==VAZIO\
                and inicio_coluna-destino_coluna==2 and destino_linha-inicio_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA VERDE PARA O LADO ESQUERDO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha + 1][inicio_coluna - 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = AZUL
            QUANT_VERDES-=1
            if destino_linha == 8:  #CONDIÇÃO PARA A PEÇA AZUL VIRAR UMA DAMA-AZUL NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA VERDE PARA O LADO ESQUERDO
                tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
        else:
            JOGADAS-=1
            print("VOCÊ MOVIMENTOU A PEÇA AZUL DE FORMA ERRADA. JOGUE NOVAMENTE!") #MENSAGEM DE ERRO, PARA SE CASO ELE MOVIMENTAR A PEÇA DELE PARA O LUGAR ERRADO
    else:
        JOGADAS -= 1
        print("VOCÊ MOVIMENTOU A PEÇA ERRADA. A VEZ DE JOGAR É DO JOGADOR 2, O JOGADOR DAS PEÇAS VERDES!")  #MENSAGEM DE ERRO, PARA SE O JOGADOR FOR MEXER A PEÇA ERRADA
def comer_peca_azul(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    """ESSA FUNÇÃO ANALISA SE A TENTATIVA DO JOGADOR 2 DE COMER UMA PEÇA AZUL DO JOGADOR 1 É VÁLIDA"""

    global JOGADAS
    global QUANT_AZUIS
    if JOGADAS%2==0:  #VERIFICA SE A VEZ É REALMENTE DO JOGADOR 2 (PEÇAS VERDES)
        if inicio_linha>destino_linha and inicio_coluna<destino_coluna and tabuleiro[inicio_linha-1][inicio_coluna+1]== AZUL \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and destino_coluna-inicio_coluna==2 and inicio_linha-destino_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA AZUL PARA O LADO DIREITO

            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha - 1][inicio_coluna + 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = VERDE
            QUANT_AZUIS-=1
            if destino_linha == 1: #CONDIÇÃO PARA A PEÇA VERDE VIRAR UMA DAMA-VERDE NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA AZUL PARA O LADO DIREITO
                tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE



        elif inicio_linha > destino_linha and inicio_coluna > destino_coluna and tabuleiro[inicio_linha - 1][inicio_coluna - 1]== AZUL \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and inicio_coluna-destino_coluna==2 and inicio_linha-destino_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA AZUL PARA O LADO ESQUERDO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha-1][inicio_coluna-1]=VAZIO
            tabuleiro[destino_linha][destino_coluna] = VERDE
            QUANT_AZUIS-=1
            if destino_linha == 1:  #CONDIÇÃO PARA A PEÇA VERDE VIRAR UMA DAMA-VERDE NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA AZUL PARA O LADO ESQUERDO
                tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
        else:
            JOGADAS-=1
            print("VOCÊ MOVIMENTOU A PEÇA VERDE DE FORMA ERRADA. JOGUE NOVAMENTE!") #MENSAGEM DE ERRO, PARA SE CASO ELE MOVIMENTAR A PEÇA DELE PARA O LUGAR ERRADO
    else:
        JOGADAS -= 1
        print("VOCÊ MOVIMENTOU A PEÇA ERRADA. A VEZ DE JOGAR É DO JOGADOR 1, O JOGADOR DAS PEÇAS AZUIS!") #MENSAGEM DE ERRO, PARA SE O JOGADOR FOR MEXER A PEÇA ERRADA
def mover_dama_azul(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
      global JOGADAS
      if JOGADAS % 2 != 0:
         coluna = inicio_coluna
         cont_vazias = 0
         if destino_linha>inicio_linha:
             if destino_coluna > inicio_coluna :
                for i in range(inicio_linha+1,destino_linha+1):   #MOVIMENTO PARA A DIREITA E BAIXO
                    coluna+=1
                    if tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL:
                        print("VOCÊ NÃO PODE MOVER A PEÇA AZUL POR ESSE CAMINHO, POIS POSSUI OUTRA PEÇA AZUL NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif  tabuleiro[i][coluna] == VAZIO and (destino_coluna - inicio_coluna == destino_linha - inicio_linha):
                        cont_vazias+=1
                        if cont_vazias == (destino_linha-inicio_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
                            cont_vazias = 0
                    elif (tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE) and (destino_coluna - inicio_coluna == destino_linha - inicio_linha)\
                            and tabuleiro[i+1][coluna+1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i+1][coluna+1] = DAMA_AZUL
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA AZUL DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
             elif inicio_coluna> destino_coluna:   #MOVIMENTO PARA A ESQUERDA E BAIXO
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha+1,destino_linha+1):
                    coluna-=1
                    if tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL:
                        print("VOCÊ NÃO PODE MOVER A PEÇA AZUL POR ESSE CAMINHO, POIS POSSUI OUTRA PEÇA AZUL NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (inicio_coluna - destino_coluna == destino_linha-inicio_linha):
                        cont_vazias+=1
                        if cont_vazias == (destino_linha-inicio_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE) and (inicio_coluna - destino_coluna == destino_linha-inicio_linha)\
                            and tabuleiro[i+1][coluna-1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i+1][coluna-1] = DAMA_AZUL
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA AZUL DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
         else:
             if destino_coluna> inicio_coluna: #MOVIMENTO PARA DIREITA E PARA CIMA
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha-1,destino_linha-1, -1):
                    coluna+=1
                    if tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL:
                        print("VOCÊ NÃO PODE MOVER A PEÇA AZUL POR ESSE CAMINHO, POIS POSSUI OUTRA PEÇA AZUL NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (destino_coluna-inicio_coluna ==inicio_linha-destino_linha):
                        cont_vazias+=1
                        if cont_vazias == (inicio_linha-destino_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE) and (destino_coluna-inicio_coluna ==inicio_linha-destino_linha)\
                            and tabuleiro[i-1][coluna+1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i-1][coluna+1] = DAMA_AZUL
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA AZUL DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
             else:       #MOVIMENTO PARA ESQUERDA E PARA CIMA
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha-1,destino_linha-1, -1):
                    coluna-=1
                    if tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL:
                        print("VOCÊ NÃO PODE MOVER A DAMA AZUL DESSA FORMA, POIS POSSUI OUTRA PEÇA AZUL NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (inicio_coluna - destino_coluna == inicio_linha -destino_linha):
                        cont_vazias+=1
                        if cont_vazias == (inicio_linha-destino_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_AZUL
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE) and (inicio_coluna - destino_coluna == inicio_linha -destino_linha)\
                            and tabuleiro[i-1][coluna-1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i-1][coluna-1] = DAMA_AZUL
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA AZUL DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break

      else:
          JOGADAS-=1
          print("NÃO É A SUA VEZ DE JOGADOR. A VEZ É DO JOGADOR DAS PEÇAS VERDES")
def mover_dama_verde(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
      global JOGADAS
      if JOGADAS % 2 == 0:
         coluna = inicio_coluna
         cont_vazias = 0
         if destino_linha>inicio_linha:
             if destino_coluna > inicio_coluna :
                for i in range(inicio_linha+1,destino_linha+1):   #MOVIMENTO PARA A DIREITA E BAIXO
                    coluna+=1
                    if tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE:
                        print("VOCÊ NÃO PODE MOVER A DAMA VERDE DESSA FORMA, POIS POSSUI OUTRA PEÇA VERDE NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif  tabuleiro[i][coluna] == VAZIO and (destino_coluna - inicio_coluna == destino_linha - inicio_linha):
                        cont_vazias+=1
                        if cont_vazias == (destino_linha-inicio_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
                            cont_vazias = 0
                    elif (tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL) and (destino_coluna - inicio_coluna == destino_linha - inicio_linha)\
                            and tabuleiro[i+1][coluna+1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i+1][coluna+1] = DAMA_VERDE
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA VERDE DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
             elif inicio_coluna> destino_coluna:   #MOVIMENTO PARA A ESQUERDA E BAIXO
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha+1,destino_linha+1):
                    coluna-=1
                    if tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE:
                        print("VOCÊ NÃO PODE MOVER A DAMA VERDE DESSA FORMA, POIS POSSUI OUTRA PEÇA VERDE NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (inicio_coluna - destino_coluna == destino_linha-inicio_linha):
                        cont_vazias+=1
                        if cont_vazias == (destino_linha-inicio_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL) and (inicio_coluna - destino_coluna == destino_linha-inicio_linha)\
                            and tabuleiro[i+1][coluna-1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i+1][coluna-1] = DAMA_VERDE
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA VERDE DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
         else:
             if destino_coluna> inicio_coluna: #MOVIMENTO PARA DIREITA E PARA CIMA
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha-1,destino_linha-1, -1):
                    coluna+=1
                    if tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE:
                        print("VOCÊ NÃO PODE MOVER A DAMA VERDE DESSA FORMA, POIS POSSUI OUTRA PEÇA VERDE NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (destino_coluna-inicio_coluna ==inicio_linha-destino_linha):
                        cont_vazias+=1
                        if cont_vazias == (inicio_linha-destino_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL) and (destino_coluna-inicio_coluna ==inicio_linha-destino_linha)\
                            and tabuleiro[i-1][coluna+1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i-1][coluna+1] = DAMA_VERDE
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA VERDE DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break
             else:       #MOVIMENTO PARA ESQUERDA E PARA CIMA
                 coluna = inicio_coluna
                 cont_vazias = 0
                 for i in range(inicio_linha-1,destino_linha-1, -1):
                    coluna-=1
                    if tabuleiro[i][coluna] == DAMA_VERDE or tabuleiro[i][coluna] == VERDE:
                        print("VOCÊ NÃO PODE MOVER A DAMA VERDE DESSA FORMA, POIS POSSUI OUTRA PEÇA VERDE NO CAMINHO")
                        JOGADAS-=1
                        break
                    elif tabuleiro[i][coluna] == VAZIO and (inicio_coluna - destino_coluna == inicio_linha -destino_linha):
                        cont_vazias+=1
                        if cont_vazias == (inicio_linha-destino_linha):
                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[destino_linha][destino_coluna] = DAMA_VERDE
                            cont_vazias=0
                    elif (tabuleiro[i][coluna] == DAMA_AZUL or tabuleiro[i][coluna] == AZUL) and (inicio_coluna - destino_coluna == inicio_linha -destino_linha)\
                            and tabuleiro[i-1][coluna-1]== VAZIO:

                            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
                            tabuleiro[i][coluna]= VAZIO
                            tabuleiro[i-1][coluna-1] = DAMA_VERDE
                            print("VOCÊ CAPTUROU UMA PEÇA DO SEU ADVERSÁRIO COM A DAMA E TEM DIREITO A OUTRA JOGADA. JOGUE NOVAMENTE!\n")
                            JOGADAS-=1
                            break
                    else:
                        JOGADAS-=1
                        print("VOCÊ MOVIMENTOU A DAMA VERDE DE FORMA ERRADA, JOGUE NOVAMENTE!")
                        break

      else:
          JOGADAS-=1
          print("NÃO É A SUA VEZ DE JOGADOR. A VEZ É DO JOGADOR DAS PEÇAS VERDES")

def limpar_tela():
    print("\n" * 20, "                                      JOGO DE DAMAS", "\n" * 3)

print("                       SEJA BEM VINDO AO JOGO DE DAMAS!!\n\n"
      "O JOGADOR 1 MOVERÁ APENAS AS PEÇAS AZUIS E O JOGADOR 2 MOVERÁ AS PEÇAS VERDES.\n"
      "PARA JOGAR PRIMEIRO VOCÊ DEVE DIGITAR O NÚMERO DA LINHA E EM SEGUIDA O NÚMERO DA COLUNA.\n"
      "EXEMPLO: 31(NESSE CASO VOCÊ VAI ESTAR INFORMANDO QUE A PEÇA ESTÁ NA LINHA 3, COLUNA 1.\n\n")

tabuleiro = [['   ', '   1  ', '   2  ', '   3  ', '  4   ', '   5  ', '   6  ', '   7  ', '   8  '],
            ['1  ',AZUL,VAZIO,AZUL, VAZIO,AZUL, VAZIO,AZUL, VAZIO],
            ['2  ', VAZIO, AZUL, VAZIO, AZUL, VAZIO, AZUL, VAZIO, AZUL],
            ['3  ', VAZIO, VAZIO, AZUL, VAZIO, DAMA_AZUL, VAZIO, VAZIO, VAZIO],
            ['4  ', VAZIO, VERDE, VAZIO, VAZIO, VAZIO, VERDE, VAZIO, VAZIO],
            ['5  ', VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
            ['6  ', VAZIO, VERDE, VAZIO, VERDE, VAZIO, VERDE, VAZIO, VERDE],
            ['7  ', VERDE, VAZIO, DAMA_AZUL, VAZIO, VERDE, VAZIO, VERDE, VAZIO],
            ['8  ', VAZIO, VERDE, VAZIO, VERDE, VAZIO, VERDE, VAZIO, VERDE]]

imprimir_tabuleiro()

while True:
    if QUANT_AZUIS>0 and QUANT_VERDES>0:
        if JOGADAS%2!=0:
            print("JOGADOR 1 - PEÇAS AZUIS\n")
        elif JOGADAS%2==0:
            print("JOGADOR 2 - PEÇAS VERDES\n")

        posicao_atual = input("DIGITE A POSIÇÃO ATUAL DA PEÇA: ")
        if  len(posicao_atual)!=2 or  posicao_atual.isdigit() == False: #VERIFICA SE TEM APENAS DOIS DIGITOS E SE REALMENTE SÃO DIGITOS
            print("VOCÊ DIGITOU A POSIÇÃO ATUAL DE FORMA ERRADA.DIGITE NOVAMENTE!")
            continue
        posicao_destino = input("DIGITE A POSIÇÃO DESTINO DA PEÇA: ")
        if len(posicao_destino) != 2 or posicao_destino.isdigit() == False: #VERIFICA SE TEM APENAS DOIS DIGITOS E SE REALMENTE SÃO DIGITOS
            print("VOCÊ DIGITOU A POSIÇÃO DESTINO DE FORMA ERRADA.DIGITE NOVAMENTE!")
            continue

        inicio_linha = int(posicao_atual[0:1])
        inicio_coluna = int(posicao_atual[1:])
        destino_linha = int(posicao_destino[0:1])
        destino_coluna = int(posicao_destino[1:])

        if destino_linha>8 or destino_linha <1 or destino_coluna>8 or destino_coluna<1 \
                or inicio_linha>8 or inicio_coluna<1 or inicio_coluna>8 or inicio_coluna<1: #VBRIFICA SE DIGITOU DE 1 ATÉ 8
            print("A POSIÇÃO ATUAL E A POSIÇÃO DESTINO DA LINHA É DE 1 ATÉ 8, VOCÊ NÃO OBEDECEU A ESSE PADRÃO. DIGITE NOVAMENTE!")
            continue


        if tabuleiro[inicio_linha][inicio_coluna]== DAMA_AZUL and destino_linha!=inicio_linha and destino_coluna!=inicio_coluna:
             limpar_tela()
             mover_dama_azul(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             imprimir_tabuleiro()

        elif tabuleiro[inicio_linha][inicio_coluna] == DAMA_VERDE:
             limpar_tela()
             mover_dama_verde(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             imprimir_tabuleiro()

        elif inicio_linha - destino_linha == 1 or destino_linha - inicio_linha ==1 and (destino_coluna - inicio_coluna==-1 or destino_coluna-inicio_coluna==1):
            limpar_tela()
            mov_das_pecas(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()

        elif (tabuleiro[inicio_linha + 1][inicio_coluna - 1] == VERDE or tabuleiro[inicio_linha + 1][inicio_coluna + 1] == VERDE) \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and destino_linha-inicio_linha==2 and (inicio_coluna-destino_coluna==2 or  destino_coluna-inicio_coluna==2):
            limpar_tela()
            comer_peca_verde(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()

        elif (tabuleiro[inicio_linha-1][inicio_coluna+1]== AZUL or tabuleiro[inicio_linha - 1][inicio_coluna - 1]== AZUL) and inicio_linha > destino_linha \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO:
            limpar_tela()
            comer_peca_azul(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()
        else:
            JOGADAS -= 1
            limpar_tela()
            print("JOGADA INVÁLIDA. JOGUE NOVAMENTE! \n")
            imprimir_tabuleiro()
        JOGADAS += 1
    else:
        if QUANT_AZUIS > 0 and QUANT_VERDES == 0:
             print("O JOGADOR DAS PEÇAS AZUIS VENCEU!!")
             break
        elif QUANT_AZUIS == 0 and QUANT_VERDES > 0:
             print("O JOGADOR DAS PEÇAS VERDES VENCEU!!")
             break
        elif QUANT_AZUIS == 1 and QUANT_VERDES == 1:
             print("O JOGO DEU EMPATE!!")
             break

