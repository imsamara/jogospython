config = {}
continua = -1
terreno = [[0,1,2,3,4,5]]
pontos = {'armador' : 0, 'andarilho' : 0}


def andar_andarilho():
    passo = ' '
    for i in range(100):
        print(passo)
        passo += '='
    
    atual = 0
    for i in range(len(terreno)-1):
        
        validos = valida_movi(atual)
        print('São válidos os espaços: ', validos)

        escolhe = valida_movi(int(input('Escolha sabiamente um dos espaços válidos: ')))
        
        while escolhe in validos:
            if terreno[i+1][escolhe] == 'O': #verifica se terreno[linha+1] na coluna [escolhe] tem ovo podre
                print('Eca! Você pisou em um ovo podre e perdeu')
                pontos['armador'] += 1
                return
            elif i == len(terreno)-2 and terreno[i+1][escolhe] == 'A': #elif i == 4 e terreno[i-1][escolhe] == 'A'
                print('Parabéns, você atravessou o terreno sem cair nas armadilhas!!')
                pontos['andarilho'] += 1
                return
            atual = escolhe
 
'''def valida_movi(selecao, anterior):
    validos = []
    if selecao == 0:
        validos = [1, 2, 3, 4, 5]
    else:
        validos.append(anterior)
        if anterior - 1 > 0:
            validos.append(anterior-1)
        if anterior + 1 < 6:
            validos.append(anterior+1)
        validos.sort()
    return validos    '''

def valida_movi(anterior):
    validos = []
    if anterior == 0:
        validos = [1, 2, 3, 4, 5]
    elif anterior == 1:
        validos = [1, 2]
    elif anterior == 5:
        validos = [4, 5]
    else:
        validos = [anterior-1, anterior, anterior+1] 
    return validos    

def colocar_ovos():
   
    for line in range(1, 6):
        ovos_na_linha = 0
        ovos_podres = ''
        ninho = ['1', '2', '3', '4', '5', 'n']
        while ovos_na_linha <3 and ovos_podres != 'n':
            ovos_podres = input(f'Em qual coluna da linha {line} você quer esconder ovos podres? [1 a 5].\nSe não desejar colocar, digite "n": ')
            ovos_podres = valida(ovos_podres, ninho)
            if ovos_podres == 'n':
                print('Pulando para a próxima linha.')
            else:
                ovos_podres = int(ovos_podres)
                terreno[line][ovos_podres] = 'O'
                ovos_na_linha += 1
                ninho.remove(str(ovos_podres))

def imprime_terreno():
    global terreno
    for i in range(6):
        for j in range(6):
            print(terreno[i][j],end=' ')
        print(' ')

def criar_terreno():
    global terreno
    for i in range(5):
        linha = []
        for j in range(6):
            if j == 0:
                linha.append(i+1)
            else:
                linha.append('A')
        terreno.append(linha)


def valida(escolha, validos):
    while escolha not in validos:
        print('Valor inválido! Digite um dos seguintes valores, ', validos, ':')
        escolha = input()
    return escolha



def def_armador():
    armador = input('Qual jogador plantará as armadilhas? [1 ou 2]: ')
    armador = int(valida(armador, ['1', '2']))
    config['armador'] = 2
    config['andarilho'] = 1
    if armador == 1:
        config['armador'] = 1
        config['andarilho'] = 2



def menu(opts):
    print('Opções:' )
    for opt in opts.items():
        print(opt[0], '-', opt[1])

# COMEÇO DA EXEC

opt = {1 : 'Definir Armador', 2 : 'Plantar Armadilhas', 3 : 'Iniciar com Andarilho', 4 : 'Mostrar o placar' , 0: 'Finalizar o Jogo'}


criar_terreno()

while continua != 0:
    menu(opt)
    continua = int(valida(input(), ['1', '2', '3', '4', '5', '0']))
    if continua == 1:
        def_armador()
        print('O armador é o jogador: ', config['armador'], '\nO andarilho é o jogador: ', config['andarilho'])
    elif continua == 2:
        if 'armador' in config.keys():
            imprime_terreno()
            print("Jogador", config['armador'], "você pode esconder até 3 ovos podres por linha do terreno.")
            colocar_ovos()
            imprime_terreno()
        else:
            print('É necessário informar o armador primeiro.')
    elif continua == 3:
        if 'armador' in config.keys():
            andar_andarilho()
    elif continua == 4:
        print('Pontuação do jogador', config['armador'], ':',  pontos['armador'])
        print('Pontuação do jogador', config['andarilho'], ':',  pontos['andarilho'])
