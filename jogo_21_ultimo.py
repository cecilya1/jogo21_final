import random
import os
from time import sleep
SISTEMA = os.name
LIMPA_TELA = 'clear'
if SISTEMA == 'nt':
    LIMPA_TELA = 'cls'
DINHEIRO = 50
VALORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
APOSTA = [25, 50, 100]
def nome() -> None:
    '''
    Exibir o nome Black jack de forma organizada
    '''
    print('''
</></></></></>      </></>              </></></></>     </></></></>< >  </></>        </></>        
</></></></></></>   </></>              </></></></>     </></></></></>  </></>      </></>                 
</></>      </></>   </></>           </></>      </></>  </></>           </></>  </></>                   
</></></></></></>   </></>           </></>      </></>  </></>           </></></></></>                    
</></>      </></>   </></>           </></></></></></>  </></>           </></>     </></>              
</></></></></></>   </></></></></>  </></>      </></>  </></></></></>  </></>       </></>       
</></></></></>      </></></></></>  </></>      </></>  </></></></></>  </></>         </></>        

            </></>     </></></></>     </></></></></>  </></>         </></>        
            </></>     </></></></>     </></></></></>  </></>      </></>                        
            </></>  </></>      </></>  </></>           </></>  </></>                
            </></>  </></>      </></>  </></>           </></></></></>                                
</></>      </></>  </></></></></></>  </></>           </></>     </></>                  
</></></></></></>  </></>      </></>  </></></></></>  </></>       </></>         
</></></></></></>  </></>      </></>  </></></></></>  </></>         </></>  
''')
def cartas_para_cima(lista: list[str]) -> None:
    '''
    Exibe a frente das cartas do jogador ou do computador de forma bonita.
    Parâmentros:
        - lista: A lista que contém as cartas do computador ou do jogador.
    '''
    print(f"╭{'╶'*5}╮  "*len(lista))
    print(f"│{' '*5}│  "*len(lista))
    for x in lista:
        if x == '10':
            print(f"│{' '*1}{x}{' '*2}│  ", end='')
        else:
            print(f"│{' '*2}{x}{' '*2}│  ", end='')
    print()
    print(f"│{' '*5}│  "*len(lista))
    print(f"╰{'╶'*5}╯  "*len(lista))
def cartas_para_baixo(lista: list[str]) -> None:
    '''
    Mostra a furmatação bonita das cartas do computador viradas para baixo.
    Parâmentros:
        - lista: A lista que contém as cartas do computador
    '''
    print(f"╭{'╶'*5}╮  "*len(lista))
    print(f"│{' '*5}│  "*len(lista))
    for x in lista:
        print(f"│ </> │  ", end='')
    print()
    print(f"│{' '*5}│  "*len(lista))
    print(f"╰{'╶'*5}╯  "*len(lista))
def calcular_pontuação(lista: list[str]) -> int: 
    '''
    Calcula a pontuação do jogador ou do computador.

    O primeiro for percorre as cartas do computador ou do jogador e analisa, dentro da constante global VALORES, qual a pontuação dessa carta.  A pontuação que a carta tem é somada à pontuação do computador ou do jogador. Isso ocorre até as cartas do jogador ou computador acabarem.

    O segundo for serve para analisar qual o valor que o Ás irá receber dependendo da ocasião, se a pontuação passou de 21, o Ás vale 1, se não vale 11.
    Parâmetros:
       - lista: Lista com as cartas do computador ou do jogador.

   Retorna:
       A pontuação, soma do valor de cada carta, do jogador ou do computador
    '''
    pontuacao=0
    for x in lista:
        pontuacao += VALORES[x]  
    for y in lista:
        if pontuacao > 21 and 'A' == y:
            pontuacao-=10
    return pontuacao
def dar_cartas_iniciais(baralho: list[str], cartas_jogador: list[str], cartas_computador: list[str]) -> None:
    '''
    Dar as duas cartas iniciais do jogador e do computador.

    O for roda duas vezes para ser puxado, duas cartas para cada um. Num é a última carta do baralho que é removida, após isso, o num é adicionado à lista de cartas do jogador ou do computador.
    Parâmetros:
       - baralho: Lista com todas as cartas do baralho atualizada.
       - cartas_jogador: Lista com as cartas do jogador.
       - cartas_computador: Lista com as cartas do computador.

    '''
    for x in range(2):
        num = baralho.pop() 
        cartas_jogador.append(num)
        num = baralho.pop()
        cartas_computador.append(num)
    return
def puxar_mais_uma_carta_jogador(baralho: list[str], cartas_jogador: list[str]) -> None:
    '''
    Puxar mais uma carta para o jogador.
    Num é a última carta do baralho que é removida, após isso, o num é adicionado à lista de cartas do jogador.
    Parâmetros:
       - baralho: Lista com todas as cartas do baralho atualizada.
       - cartas_jogador: Lista com as cartas do jogador.
    '''
    num = baralho.pop() 
    cartas_jogador.append(num)
    return
def jogadas_normais(aposta_jogador: int, aposta_computador: int, nome_jogador:str, cartas_computador: list[str],cartas_jogador: list[str]) -> None:
    '''
    Exibe o nome computador e ao lado a aposta do mesmo, em baixo mostra a furmatação organizada das cartas do computador viradas para baixo. Após isso, exibe o nome jogador, a pontuação e ao lado a aposta do mesmo, em baixo mostra a furmatação organizada das cartas do jogador viradas para cima.
    Parâmentros:
       - aposta_jogador: A aposta escolhida pelo jogador na partida.
       - aposta_computador: A aposta computador na partida.
       - nome_jogador: Nome do jogador da partida.
       - cartas_computador: Lista com as cartas do computador.
       - cartas_jogador: Lista com as cartas do jogador.
    '''
    print()
    print(f"Computador {' '*5} APOSTA: R${aposta_computador}")
    cartas_para_baixo(cartas_computador)
    print()
    cartas_para_cima(cartas_jogador)
    print(f"{nome_jogador} ")
    print(f"Pontuação: {calcular_pontuação(cartas_jogador)} {' '*5} APOSTA: R${aposta_jogador}")
def jogada_computador(baralho: list[str], cartas_computador: list[str]) -> bool:
    '''
    Puxar mais uma carta para o computador, se for necessário.

    O if analisa se a pontuação do computador é menor que 11, se sim, escolhe outra carta para o mesmo, adiciona essa carta à lista de cartas do computador. O primeiro eleif verifica se a pontuação foi maior ou igual a 18, se sim ele returna False, isso significa que ele não quer mais cartas. O segundo if analisa se a probabilidade1 for maior ou iqual a probabilidade2, se sim escolhe outra carta para o mesmo, adiciona essa carta à lista de cartas do computador. Por fim, o else verifica se a probabilidade1 for menor que a probabilidade1, se sim, só returna False,  isso significa que ele não quer mais cartas.

    Parâmentros:
       - baralho: Lista com todas as cartas do baralho atualizada.
       - cartas_computador: Lista com as cartas do computador.
    Retorna:
       Se o computador quis puxar uma carta True, ou False, se não quis puxar uma nova carta.
    '''
    probabilidade1 = 1 - ((calcular_pontuação(cartas_computador)-11)/9) 
    probabilidade2 = random.random()
    if calcular_pontuação(cartas_computador) <= 11:
        num = baralho.pop() 
        cartas_computador.append(num)
        return True
    elif calcular_pontuação(cartas_computador) >= 18:
        return False
    if probabilidade1 >= probabilidade2:
        num = baralho.pop() 
        cartas_computador.append(num)
        return True
    else:
        return False
def jogada_final(aposta_jogador: int, aposta_computador: int, nome_jogador: str, cartas_computador: list[str],cartas_jogador:list[str]) -> None:
    '''
    Exibe as cartas do computador e do jogador viradas para cima.

    Parte do Computador: 
    Mostra a pontuação do computador ao final da partida, chama a função calcular_pontuação para fazer isso. Em baixo mostra a aposta do computador. E para finalizar, a parte do computador exibe as cartas dele viradas para cima.

    Parte do jogador: 
    Exibe as cartas do jogador viradas para cima, após isso o nome do jogador, em continuação à pontuação do jogador ao final da partida, chama a função calcular_pontuação para fazer isso, ao lado tem a aposta que o jogador fez. 

    Parâmetros:
       - aposta_jogador: A aposta escolhida pelo jogador na partida.
       - aposta_computador: A aposta computador na partida.
       - nome_jogador: Nome do jogador da partida.
       - cartas_computador: Lista com as cartas do computador.
       - cartas_jogador: Lista com as cartas do jogador.
    '''
    print()
    print(f"Pontuação: {calcular_pontuação(cartas_computador)}")
    print(f"Computador {' '*5} APOSTA: R${aposta_computador}")
    cartas_para_cima(cartas_computador)
    print()
    print()
    cartas_para_cima(cartas_jogador)
    print(f"{nome_jogador} ")
    print(f"Pontuação: {calcular_pontuação(cartas_jogador)} {' '*5} APOSTA: R${aposta_jogador}")
    print()
def menu_inicial() -> None:
    '''
    Exibe o menu inicial

    Mostra primeiro os elementos do menu inicial, depois pergunta o que a pessoa quer fazer, o if verifica se a pessoa quer jogar e pergunta o nome do jogador para começar a jogar, o primeiro elif verifica se a pessoa quer ver o ranking do Black Jack se sim e mostra o ranking atualizado, depois mostra novamente o menu inicial e, por fim, o segundo elif verifica se a escolha da pessoa é sair e finaliza o programa.
    '''
    pontos=0
    while True:
        print('Menu:')
        print('1. Jogar.')
        print('2. Ranking.')
        print('3. Sair.')
        escolha = int(input('Qual a escolha: '))
        if escolha == 1:
            os.system(LIMPA_TELA)
            nome()
            nome_jogador = input('Qual seu nome: ')
            print()
            os.system(LIMPA_TELA)
            nome()
            jogar(nome_jogador, pontos)
        elif escolha == 2:
            os.system(LIMPA_TELA)
            nome()
            cadastro = open('cadastro.txt', 'a')
            cadastro.close()
            ranking()
            print()
        elif escolha == 3:
            return 
def ranking() -> None:
    '''
    Calcular o ranking entre os jogadores.
    Inicialmente, abri o arquivo ranking.txt, passa todo o conteudo dele para a lista conteudo e, após isso, fecha o arquivo. O for percorre conteudo, exclui o último palavra de cada elemento da lista e pega como separador o sinal de igual onde de tiver antes do sinal coloca na variável nome e se tiver depois coloca como pontuacao, após isso adiciona a lista ranking a pontuacao, inteiro, e o nome em formado de lista (ranking vira uma matriz, lista com lista dentro dela). Organiza a matriz ranking de forma crescente. Por fim, analisa se no ranking tem pelo menos 5 pessoas, se sim percorre roda 5 vezes o for para mostra de forma organizada a colocação até 5 jogadores, o nome do jogador e os pontos, quantia recebida ou perdida ao final da partida. Pórem, se tiver menos de 5 pessoas mostra as pessoas nas suas colocações e as que sobram para formar 5 é apenas mostrada vazia, a cada loop é adicionado um para o “cont”, que serve como a colocação dos jogadores nesse caso.
    '''
    cadastro = open('cadastro.txt')
    conteudo = cadastro.readlines()
    cadastro.close()
    ranking=[]
    for x in conteudo:
        nome = x[:-1].split('=')[0]
        pontuacao = x[:-1].split('=')[1]
        nome_pontuacao = [int(pontuacao), nome]
        ranking.append(nome_pontuacao)
    ranking = sorted(ranking, reverse=True)
    print()
    print('----Ranking----')
    cont=1
    if len(ranking) >= 5:
        for l in range(5):
            print(f'|{l+1}°- {ranking[l][1]} = {ranking[l][0]}')
    else:
        for l in ranking:
            print(f'|{cont}° - {l[1]} = {l[0]}')
            cont+=1
        for z in range(len(ranking), 5):
            print(f'|{z+1}° - ')
def menu_secundário(nome_jogador:str, pontos:int) -> int: 
    '''
    Menu para perguntar se o jogador quer jogar outra partida.

    Mostra primeiro os elementos do menu secundário, depois pergunta o que a pessoa quer fazer. O if verifica se a pessoa quer jogar outra partida, se sim, inicia outra partida com o mesmo jogador, chama a função jogar para isso, o elif verifica se a escolha da pessoa é sair e, se sim, abre o arquivo ranking para escrita apenas no final, preservando o conteúdo existente, adiciona ao arquivo o nome do jogador e os pontos (quantia que o jogador ganhou ou perdeu na(s) partida(s) ) do mesmo, e após isso fecha o arquivo. Ao final, sai do menu secundário e depois disso volta para o menu inicial, com a função menu_inicial.

    Parâmetros:
       - nome_jogador: Nome do jogador da partida.
       - pontos: Quantia recebida ou perdida ao final da partida pelo jogador.
    Retorna:
       A quantia recebida ou perdida ao final da partida pelo jogador.
    '''
    while True:
        print()
        print("\nDeseja continuar jogando ou sair?")
        print("1. Continuar Jogando.")
        print("2. Sair.")
        escolha = input("Escolha: ")
        if escolha == '1':
            os.system(LIMPA_TELA)
            nome()
            pontos = jogar(nome_jogador, pontos) # Continua o jogo com o mesmo jogador
            break
        elif escolha == '2':
            cadastro = open('cadastro.txt', 'a')
            cadastro.write(nome_jogador + '=' + str(pontos) + '\n')
            cadastro.close()
            print("Voltando ao menu principal...")
            os.system(LIMPA_TELA)
            break
        else:
            print("Opção inválida! Tente novamente.")
    return pontos

def verificação_final(cartas_jogador:list[str], aposta_jogador:int, aposta_computador:int, cartas_computador:list[str], pontos:int) -> int:
    '''
    Ao final da partida verificar quem ganhou ou se empatou

    O primeiro if verifica todas as possibilidades do jogador ter ganhado (se o computador passou de 21, ou se o jogador passou a pontuação do computador sem estourar a mão), se isso acontecer, mostra que o jogador ganhou essa partida e amostra também quanto o jogador ganhou em reais nessa partida. 
    O primeiro eleif analisa, todas as possibilidades de o computador ter ganhado (se o jogador passou de 21, ou se o computador passou a pontuação do jogador sem estourar a mão), se isso acontecer, mostra que o computador ganhou essa partida e amostra também quando o computador ganhou em reais nessa partida. 
    Após isso, o elif analisa todas as possibilidades de a partida ter dado empate (se a pontuação do jogador e o computador for igual, ou se o computador e o jogador passaram de 21), se isso acontecer, mostra que a partida deu empate. Por fim, returna os pontos.

    Parâmetros:
       - cartas_jogador: Lista com as cartas do jogador.
       - aposta_jogador: A aposta escolhida pelo jogador na partida.
       - aposta_computador: A aposta computador na partida.
       - cartas_computador: Lista com as cartas do computador.
       - pontos: Quantia que o jogador ganhou ou perdeu na partida.
    Retorna:
      A quantia recebida ou perdida ao final da partida pelo jogador.
    '''
    if calcular_pontuação(cartas_jogador) > calcular_pontuação(cartas_computador) and calcular_pontuação(cartas_jogador) <= 21 and calcular_pontuação(cartas_computador) <= 21:
        pontos+=aposta_computador
        print('Você acabou de ganhar do computador!')
        print(f'Você ganhou R${aposta_computador}')
    elif calcular_pontuação(cartas_computador) > 21:
        pontos+=aposta_computador
        print('O computador estourou a mão!! Você acabou de ganhar do computador!')
        print(f'Você ganhou R${aposta_computador}')
    elif calcular_pontuação(cartas_computador) > calcular_pontuação(cartas_jogador) and calcular_pontuação(cartas_computador) <= 21 and calcular_pontuação(cartas_jogador) <= 21:
        pontos -= aposta_jogador
        print('O computador ganhou essa rodada!')
        print(f'O computador ganhou R${aposta_jogador}')
    elif calcular_pontuação(cartas_jogador) > 21:
        pontos -= aposta_jogador
        print('Você estourou a mão!! O computador ganhou essa rodada!')
        print(f'O computador ganhou R${aposta_jogador}')
    elif calcular_pontuação(cartas_jogador) == calcular_pontuação(cartas_computador) or calcular_pontuação(cartas_jogador) > 21 and calcular_pontuação(cartas_computador) > 21:
        pontos += 0
        print('Empate')
    for x in range(1, 4):
        sleep(1)
    os.system(LIMPA_TELA)
    nome()
    print()
    return pontos
def computador_continuar_escolhendo_cartas(cartas_computador:list[str], baralho: list[str], cartas_jogador: list[str], aposta_jogador: int, aposta_computador: int, nome_jogador:str) -> None:
    '''
    O computador quer continuar escolhendo carta, depois que o jogador acabou de escolher as suas cartas.

    O primeiro if verifica se o jogador não já estourou a mão. A função analisa se o computador quer escolher mais uma carta ou não, aparti da função jogada_computador que se o return dessa fonção for True o computador ainda escolhe outra caso (Não executei dentro do if a jogada do computador, pois na hora de testar se foi True ele já compra uma nova carta, nesse caso não é necessário chamar a função novamente) e se for false para se escolher as cartas Além disso, se a pontuação do computador já tiver passado de 21 ele mostra que já passou e para a função.

    Parâmetros:
       - cartas_computador: Lista com as cartas do computador.
       - baralho: Lista com todas as cartas do baralho atualizada.
       - cartas_jogador: Lista com as cartas do jogador.
       - aposta_jogador: A aposta escolhida pelo jogador na partida.
       - aposta_computador: A aposta computador na partida.
       - nome_jogador: Nome do jogador da partida.
    '''
    while True:
        if calcular_pontuação(cartas_jogador) > 21:
            return
        if jogada_computador(baralho, cartas_computador) == True:
            print('O computador ainda está puxando as cartas dele!!!')
            jogadas_normais(aposta_jogador, aposta_computador, nome_jogador, cartas_computador,cartas_jogador)
            for x in range(1, 3):
                sleep(2)
            os.system(LIMPA_TELA)
            nome()
            print()
        else:
            return
        if calcular_pontuação(cartas_computador) > 21:
            return
def escolher_mais_cartas(baralho: list[str], cartas_jogador: list[str], nome_jogador: str, aposta_jogador: int, aposta_computador: int, cartas_computador: list[str]) -> None:
    '''
    Verifica se o jogador quer mais cartas.

    Primeiro analisa se o computador já passou de 21, se sim o jogador não precisa nem escolher outra carta, pois ele já ganhou. Pergunta se o jogador quer mais uma carta. Se sim, puxa uma nova carta para o jogador e analisa se o jogador ou o computador já passaram de 21. Após isso, faz a jogada do computador. Porém, se o jogador responder que não quiser mais cartas, analisa se o computador quer escolher mais cartas. Ao final de tudo, mostra de forma organizada as cartas do computador e do jogador. No entanto, se o jogador não quiser mais cartas, simplesmente termina o loop. 

    Parâmetros:
       - baralho: Lista com todas as cartas do baralho atualizada.
       - cartas_jogador: Lista com as cartas do jogador.
       - nome_jogador: Nome do jogador da partida.  
       - aposta_jogador: A aposta escolhida pelo jogador na partida.
       - aposta_computador: A aposta computador na partida.
       - cartas_computador: Lista com as cartas do computador.
    '''
    while True:
        if calcular_pontuação(cartas_computador) > 21: 
            jogadas_normais(aposta_jogador, aposta_computador, nome_jogador, cartas_computador,cartas_jogador)
            print()
            break
        print()
        mais_cartas = input('Quer puxar mais uma carta [s/n]: ').lower()
        quer_mais_carta_computador = True 
        if mais_cartas == 's':
            os.system(LIMPA_TELA)
            nome()
            puxar_mais_uma_carta_jogador(baralho, cartas_jogador)
            if calcular_pontuação(cartas_jogador) > 21: # Verifica se o jogador já estourou a mão
                jogadas_normais(aposta_jogador, aposta_computador, nome_jogador, cartas_computador,cartas_jogador)
                print()
                break
            quer_mais_carta_computador = jogada_computador(baralho, cartas_computador)
            jogadas_normais(aposta_jogador, aposta_computador, nome_jogador, cartas_computador,cartas_jogador)
        elif mais_cartas == 'n':  
            if quer_mais_carta_computador == True:
                os.system(LIMPA_TELA)
                nome()
                computador_continuar_escolhendo_cartas(cartas_computador, baralho, cartas_jogador, aposta_jogador, aposta_computador, nome_jogador)
            break
        else:
            print('Resposta inválida!! Tende novamenete.')
def verificar_aposta(pontos: int) -> int:
    '''
    Verificar de aposta do jogador é válida

    A partir do saldo, mostra as apostas válidas e analisa se a escolha da pessoa é válida. Se não for, continua pedindo até que a pessoa digite uma aposta válida.

    Parâmetros:
       - pontos: Quantia que o jogador ganhou ou perdeu na partida.
    Retorna:
       A aposta do jogador para a partida.
    "
    '''
    while True:
        if DINHEIRO + (pontos) >=100:
            print(f'Seu saldo é de R$ {DINHEIRO + (pontos)},00')
            print('APOSTAS VÁLIDAS')
            print("R$25   R$50   R$100")
            aposta_jogador = int(input('Qual a sua aposta: '))
            if aposta_jogador == 25 or aposta_jogador == 50 or aposta_jogador == 100:
                return aposta_jogador
            else:
                print('Aposta inválida!!')
                os.system(LIMPA_TELA)
                nome()
        if DINHEIRO + (pontos) >= 50:
            print(f'Seu saldo é de R$ {DINHEIRO + (pontos)},00')
            print('APOSTAS VÁLIDAS')
            print("R$25   R$50")    
            aposta_jogador = int(input('Qual a sua aposta: '))
            if aposta_jogador == 25 or aposta_jogador == 50:
                return aposta_jogador
            else:
                print('Aposta inválida!!')
                os.system(LIMPA_TELA)
                nome()
        elif DINHEIRO + (pontos) == 25:
            print(f'Seu saldo é de R$ {DINHEIRO + (pontos)},00')
            print(f'Então a sua aposta é de R$25,00.')
            aposta_jogador = 25
            return aposta_jogador
def jogar(nome_jogador: str, pontos:int) -> int:
    '''
    Executa a partida completa do Black Jack.

    Inicialmente, define a aposta do computador e pergunta qual é a aposta do jogador. No primeiro id analisa se o saldo não está zerado, se não estiver zerado a pessoa pode jogar. Chama a função para verificar se a aposta do jogador é válida. Após a validação da aposta, distribue as cartas iniciais para o computador e o jogador. Mostra de forma organizada as cartas do computador, viradas para baixo, e as cartas do jogador, viradas para cima. A variável pontos é o return da verificação se o jogador deseja mais cartas. Analisa se o computador deve continuar a escolher cartas depois que o jogador acabou de escolher as suas cartas. Exibi as cartas do computador e do jogador viradas para cima. A variável pontos é o return da verificação final, analisar quem ganhou ou se empatou. Por fim, exibe o menu secundário.

    Parâmetros:
       - nome_jogador: Nome do jogador da partida.  
       - pontos: Quantia que o jogador ganhou ou perdeu na partida.
    Retorna:
       A quantia recebida ou perdida ao final da partida pelo jogador.

    '''
    aposta_computador = int(random.choice(APOSTA))
    if DINHEIRO + (pontos) == 0:
        print('Não tem mais saldo, por isso não pode mais jogar!')
        return
    aposta_jogador = verificar_aposta(pontos)
    os.system(LIMPA_TELA)
    nome()
    baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
    random.shuffle(baralho)
    cartas_jogador = [] # Lista com as cartas do jogador
    cartas_computador = [] # Lista com as cartas do Computador
    os.system(LIMPA_TELA)
    nome()
    dar_cartas_iniciais(baralho, cartas_jogador, cartas_computador)
    jogadas_normais(aposta_jogador, aposta_computador, nome_jogador, cartas_computador,cartas_jogador)
    escolher_mais_cartas(baralho, cartas_jogador, nome_jogador, aposta_jogador, aposta_computador, cartas_computador)
    os.system(LIMPA_TELA)
    nome()
    jogada_final(aposta_jogador, aposta_computador, nome_jogador, cartas_computador, cartas_jogador)
    pontos = verificação_final(cartas_jogador, aposta_jogador, aposta_computador, cartas_computador, pontos)
    pontos = menu_secundário(nome_jogador, pontos)
    return pontos

if __name__ == '__main__':
    nome()
    menu_inicial()