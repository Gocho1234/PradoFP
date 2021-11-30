# 103124 - Gonçalo Sampaio Bárias - goncalo.barias@tecnico.ulisboa.pt

##########################################################################
##                                                                      ##
##                         O Prado                                      ##
##                                                                      ##
##  Projeto 2 - Fundamentos da Programação 21/22                        ##
##  Licenciatura em Engenharia Informática e de Computadores (Alameda)  ##
##  Instituto Superior Técnico                                          ##
##                                                                      ##
##########################################################################


##### TAD posicao ###############################################################
## REPRESENTAÇÃO INTERNA: as posições são representadas por coordenadas na     ##
## forma de lista, em que a primeira entrada é a coordenada horizontal (x) e a ##
## segunda entrada é a coordenada vertical (y).                                ##
##                                                                             ##
## OPERAÇÕES BÁSICAS: cria_posicao: int x int → posicao                        ##
##                    cria_copia_posicao: posicao → posicao                    ##
##                    obter_pos_x: posicao → int                               ##
##                    obter_pos_y: posicao → int                               ##
##                    eh_posicao: universal → booleano                         ##
##                    posicoes_iguais: posicao x posicao → booleano            ##
##                    posicao_para_str: posicao → str                          ##
#################################################################################


def cria_posicao(x, y):
    # cria_posicao: int x int → posicao
    '''Recebe duas coordenadas de uma posição e retorna essa posição.

    Levanta um ValueError se as coordenadas não são válidas para gerar uma
    posição. Uma coordenada válida, tem de ter componentes inteiras, maiores ou
    iguais a zero.
    '''
    if not (type(x) == type(y) == int and y >= 0 and x >= 0):
        raise ValueError("cria_posicao: argumentos invalidos")

    return [x, y]


def cria_copia_posicao(posicao):
    # cria_copia_posicao: posicao → posicao
    '''
    Retorna uma cópia da posição recebida.
    '''
    return posicao.copy()


def obter_pos_x(posicao):
    # obter_pos_x: posicao → int
    '''
    Devolve a componente x da posição recebida.
    '''
    return posicao[0]


def obter_pos_y(posicao):
    # obter_pos_y: posicao → int
    '''
    Devolve a componente y da posição recebida.
    '''
    return posicao[1]


def eh_posicao(arg):
    # eh_posicao: universal → booleano
    '''Verifica se o seu argumento corresponde a uma posição válida.

    Para este efeito, o argumento tem de respeitar a representação interna e as
    condições que geram uma posição, ou seja, o argumento tem de ser uma lista
    com componentes inteiras, maiores ou iguais a zero.
    '''
    if not (isinstance(arg, list) and len(arg) == 2): return False

    COMP_X, COMP_Y = obter_pos_x(arg), obter_pos_y(arg)

    return (type(COMP_X) == type(COMP_Y) == int
            and COMP_Y >= 0 and COMP_X >= 0)


def posicoes_iguais(posicao1, posicao2):
    # posicoes_iguais: posicao x posicao → booleano
    '''
    Verifica se duas posições têm componentes exatamente iguais.
    '''
    return (obter_pos_x(posicao1) == obter_pos_x(posicao2)
            and obter_pos_y(posicao1) == obter_pos_y(posicao2))


def posicao_para_str(posicao):
    # posicao_para_str: posicao → str
    '''
    Recebe uma posição e transforma-a numa string, de acordo com a
    representação externa.
    '''
    return f"({obter_pos_x(posicao)}, {obter_pos_y(posicao)})"


def obter_posicoes_adjacentes(posicao):
    # obter_posicoes_adjacentes: posicao → tuplo
    '''Obtém as posições adjacentes a essa posição.

    Recebe uma posição e retorna um tuplo que contém as posições adjacentes a
    essa posição, seguindo o sentido horário, que tem início diretamente acima
    da posição. Todas as posições adjacentes com componentes negativas são
    removidas, pois não são posições válidas.
    '''
    posicoes_adjacentes = [(obter_pos_x(posicao), obter_pos_y(posicao) - 1),
                           (obter_pos_x(posicao) + 1, obter_pos_y(posicao)),
                           (obter_pos_x(posicao), obter_pos_y(posicao) + 1),
                           (obter_pos_x(posicao) - 1, obter_pos_y(posicao))]
        # Cria todas as posições adjacentes (válidas ou não).

    posicoes_adjacentes = filter(lambda pos: pos[0] >= 0 and pos[1] >= 0,
                                posicoes_adjacentes)
        # Filtra todas as posições com componentes negativas.

    posicoes_adjacentes = map(lambda pos: cria_posicao(pos[0], pos[1]),
                             posicoes_adjacentes)
        # Cria as posições que são consideradas válidas.

    return tuple(posicoes_adjacentes)


def ordenar_posicoes(posicoes):
    # ordenar_posicoes: tuplo → tuplo
    '''Ordena várias posições de acordo com a ordem de leitura do prado.

    Recebe um tuplo com várias posições e ordena-as, juntando primeiro as
    posições que se encontram na mesma linha e depois organiza cada linha, da
    esquerda para a direita, cima para baixo. Posto isto, vai organizar a
    próxima linha com posições e segue os mesmos moldes para organizar as
    restantes linhas.
    '''
    posicoes_ordenadas = sorted(posicoes,
                         key = lambda pos: (obter_pos_y(pos), obter_pos_x(pos)))

    return tuple(posicoes_ordenadas)


##### TAD animal ##################################################################
## REPRESENTAÇÃO INTERNA: os animais são representados por uma lista, que contém ##
## por ordem, a sua espécie, idade, frequência de reprodução, fome e frequência  ##
## de alimentação. A sua espécie tem de ser uma string não vazia. A sua idade,   ##
## frequência de reprodução, fome e frequência de alimentação, têm de ser todos  ##
## inteiros maiores ou iguais a zero, com a exceção da frequência de reprodução, ##
## que tem de ser estritamente maior que zero.                                   ##
##                                                                               ##
## OPERAÇÕES BÁSICAS: cria_animal: str x int x int → animal                      ##
##                    cria_copia_animal: animal → animal                         ##
##                    obter_especie: animal → str                                ##
##                    obter_freq_reproducao: animal → int                        ##
##                    obter_freq_alimentacao: animal → int                       ##
##                    obter_idade: animal → int                                  ##
##                    obter_fome: animal → int                                   ##
##                    aumenta_idade: animal → animal                             ##
##                    reset_idade: animal → animal                               ##
##                    aumenta_fome: animal → animal                              ##
##                    reset_fome: animal → animal                                ##
##                    eh_animal: universal → booleano                            ##
##                    eh_predador: universal → booleano                          ##
##                    eh_presa: universal → booleano                             ##
##                    animais_iguais: animal x animal → booleano                 ##
##                    animal_para_char: animal → str                             ##
##                    animal_para_str: animal → str                              ##
###################################################################################


def cria_animal(especie, freq_r, freq_a):
    # cria_animal: str x int x int → animal
    '''Cria um animal com a informação fornecida.

    Cria um animal de uma determinada espécie, com uma frequência de reprodução
    e uma frequência de alimentação (igual a 0 se for presa). Levanta um ValueError
    caso o seu primeiro argumento não seja uma string e se os outros dois
    argumentos não sejam inteiros positivos (não nulos ou nulos, respetivamente).
    '''
    if not (isinstance(especie, str) and type(freq_r) == type(freq_a) == int
            and especie != '' and freq_r > 0 and freq_a >= 0):
        raise ValueError("cria_animal: argumentos invalidos")

    return [especie, 0, freq_r, 0, freq_a]


def cria_copia_animal(animal):
    # cria_copia_animal: animal → animal
    '''
    Recebe um animal e devolve uma cópia do mesmo.
    '''
    return animal.copy()


def obter_especie(animal):
    # obter_especie: animal → str
    '''
    Retorna a espécie do animal.
    '''
    return animal[0]


def obter_freq_reproducao(animal):
    # obter_freq_reproducao: animal → int
    '''
    Retorna a frequência de reprodução do animal.
    '''
    return animal[2]


def obter_freq_alimentacao(animal):
    # obter_freq_alimentacao: animal → int
    '''
    Retorna a frequência de alimentação do animal (sempre 0 para as presas).
    '''
    return animal[4]


def obter_idade(animal):
    # obter_idade: animal → int
    '''
    Retorna a idade do animal.
    '''
    return animal[1]


def obter_fome(animal):
    # obter_fome: animal → int
    '''
    Retorna a fome do animal (sempre 0 para as presas).
    '''
    return animal[3]


def aumenta_idade(animal):
    # aumenta_idade: animal → animal
    '''
    Aumenta a idade do animal que recebe e devolve-o imediatamente a seguir.
    '''
    animal[1] += 1
    return animal


def reset_idade(animal):
    # reset_idade: animal → animal
    '''
    Reduz a idade do animal que recebe até 0 e devolve-o imediatamente a seguir.
    '''
    animal[1] = 0
    return animal


def aumenta_fome(animal):
    # aumenta_fome: animal → animal
    '''
    Aumenta a fome do animal que recebe e devolve-o imediatamente a seguir.
    Caso o animal seja uma presa, não aumenta nada.
    '''
    if eh_predador(animal): animal[3] += 1
    return animal


def reset_fome(animal):
    # reset_fome: animal → animal
    '''
    Reduz a fome do animal que recebe até 0 e devolve-o imediatamente a seguir.
    Caso o animal seja uma presa, não reduz nada.
    '''
    if eh_predador(animal): animal[3] = 0
    return animal


def eh_animal(arg):
    # eh_animal: universal → booleano
    '''Verifica se o seu argumento corresponde a um animal válido.

    Assim, o argumento tem de ser uma lista com 5 elementos, respeitando a
    representação interna; os elementos têm de ser, respetivamente, a espécie,
    idade, frequência de reprodução, fome e frequência de alimentação. A primeira
    tem de ser uma string e as restantes valores inteiros.
    '''
    if not isinstance(arg, list) or len(arg) != 5: return False

    ESPECIE = obter_especie(arg)
    IDADE, FREQ_R = obter_idade(arg), obter_freq_reproducao(arg)
    FOME, FREQ_A = obter_fome(arg), obter_freq_alimentacao(arg)

    return (type(IDADE) == type(FREQ_R) == type(FOME) == type(FREQ_A) == int
            and IDADE >= 0 and FREQ_R > 0 and FOME >= 0 and FREQ_A >= 0
            and isinstance(ESPECIE, str) and ESPECIE != '')


def eh_predador(arg):
    # eh_predador: universal → booleano
    '''
    Verifica se o seu argumento é um animal com frequência de alimentação
    diferente de 0, pois só assim é um predador.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) != 0


def eh_presa(arg):
    # eh_presa: universal → booleano
    '''
    Verifica se o seu argumento é um animal com frequência de alimentação
    igual a 0, pois só assim é uma presa.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(animal1, animal2):
    # animais_iguais: animal x animal → booleano
    '''
    Verifica se os seus argumentos são animais e se a informação de um animal
    (primeiro argumento) é exatamente igual à do outro (segundo argumento).
    '''
    if not (eh_animal(animal1) and eh_animal(animal2)):
        return False

    if obter_especie(animal1) != obter_especie(animal2):
        return False

    if obter_idade(animal1) != obter_idade(animal2):
        return False

    if obter_freq_reproducao(animal1) != obter_freq_reproducao(animal2):
        return False

    if obter_fome(animal1) != obter_fome(animal2):
        return False

    if obter_freq_alimentacao(animal1) != obter_freq_alimentacao(animal2):
        return False

    return True


def animal_para_char(animal):
    # animal_para_char: animal → str
    '''
    Devolve a primeira letra do animal em maiúscula se for predador, ou
    minúscula em caso contrário.
    '''
    primeira_letra = obter_especie(animal)[0]

    if eh_presa(animal):
        return primeira_letra.lower()
    else:
        return primeira_letra.upper()


def animal_para_str(animal):
    # animal_para_str: animal → str
    '''
    Transforma o animal numa string com a sua informação toda, variando de
    acordo com o seu tipo (presa ou predador).
    '''
    ESPECIE = obter_especie(animal)
    FREQ_R, IDADE = obter_freq_reproducao(animal), obter_idade(animal)
    FREQ_A, FOME = obter_freq_alimentacao(animal), obter_fome(animal)

    if eh_predador(animal):
        return f"{ESPECIE} [{IDADE}/{FREQ_R};{FOME}/{FREQ_A}]"
    else:
        return f"{ESPECIE} [{IDADE}/{FREQ_R}]"


def eh_animal_fertil(animal):
    # eh_animal_fertil: animal → booleano
    '''
    Verifica se o animal está pronto a reproduzir-se, ou seja, se a sua idade é
    superior ou igual à frequência de reprodução.
    '''
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    # eh_animal_faminto: animal → booleano
    '''
    Verifica se o animal é um predador faminto, ou seja, se a sua fome é igual à
    frequência de alimentação. Caso o animal seja uma presa, nunca está faminto.
    '''
    return (eh_predador(animal)
            and obter_fome(animal) == obter_freq_alimentacao(animal))


def reproduz_animal(animal):
    # reproduz_animal: animal → animal
    '''
    Reduz a idade do animal para 0 e cria um novo animal com a mesma espécie e
    frequências de reprodução e alimentação que o animal original.
    '''
    animal = reset_idade(animal)

    return (cria_animal(obter_especie(animal),
                        obter_freq_reproducao(animal),
                        obter_freq_alimentacao(animal)))


###### TAD prado ###############################################################
## REPRESENTAÇÃO INTERNA: o prado é representado por um dicionário com 4      ##
## entradas, a primeira para a posição da montanha do canto inferior direito, ##
## a segunda para um tuplo com as posições dos rochedos, a terceira para um   ##
## tuplo com animais nesse prado e por fim a quarta para um tuplo com as      ##
## posições desses animais. Todas as posições no prado têm de ser válidas e   ##
## os animais que lá constam também têm de ser válidos para o prado ser       ##
## criado.                                                                    ##
##                                                                            ##
## OPERAÇÕES BÁSICAS: cria_prado: posicao x tuplo x tuplo x tuplo  prado      ##
##                    cria_copia_prado: prado → prado                         ##
##                    obter_tamanho_x: prado → int                            ##
##                    obter_tamanho_y: prado → int                            ##
##                    obter_numero_predadores: prado → int                    ##
##                    obter_numero_presas: prado → int                        ##
##                    obter_posicao_animais: prado → tuplo posicoes           ##
##                    obter_animal: prado x posicao → animal                  ##
##                    eliminar_animal: prado x posicao → prado                ##
##                    mover_animal: prado x posicao x posicao → prado         ##
##                    inserir_animal: prado x animal x posicao → prado        ##
##                    eh_prado: universal → booleano                          ##
##                    eh_posicao_animal: prado x posicao → booleano           ##
##                    eh_posicao_obstaculo: prado x posicao → booleano        ##
##                    eh_posicao_livre: prado x posicao → booleano            ##
##                    prados_iguais: prado x prado → booleano                 ##
##                    prado_para_str: prado → str                             ##
################################################################################


# <função auxiliar>

def verifica_posicoes(posicoes, lim_prado):
    # verifica_posicoes: tuplo x posicao → booleano
    '''Verifica se as posições que recebe são válidas para um determinado prado.

    É uma função auxiliar de baixo nível, apenas utilizada por operações básica.
    Recebe um tuplo de posições e uma posição que delimita um prado. Posto isto,
    verifica se essas posições são válidas e se estão contidas no respetivo prado.
    '''
    for posicao in posicoes:
        if not eh_posicao(posicao):
            return False
            # Verifica se é uma posição válida.

        if (obter_pos_x(posicao) == 0
            or obter_pos_x(posicao) >= obter_pos_x(lim_prado)):
            return False

        if (obter_pos_y(posicao) == 0
            or obter_pos_y(posicao) >= obter_pos_y(lim_prado)):
            return False
        # Verifica se a posição está dentro dos limites do prado.

    return True

# </função auxiliar>


def cria_prado(lim_prado, rochedos, animais, posicoes_animais):
    # cria_prado: posicao x tuplo x tuplo x tuplo → prado
    '''Cria um prado com a informação que lhe é fornecida.

    Levanta ValueError caso algum dos seus argumentos seja inválido. Os argumentos
    válidos têm de ser uma posição que delimite o prado, um tuplo com posições
    válidas para rochedos (pode estar vazio) e outro com posições válidas para
    animais (não pode estar vazio) e por fim um tuplo com animais válidos
    (tem de ter animais para cada posição).
    '''
    if not (type(rochedos) == type(animais) == type(posicoes_animais) == tuple
            and eh_posicao(lim_prado)):
        raise ValueError("cria_prado: argumentos invalidos")

    if len(animais) == 0 or len(animais) != len(posicoes_animais):
        raise ValueError("cria_prado: argumentos invalidos")
        # Verifica se existe pelo menos um animal num prado e se cada animal tem
        # uma respetiva posição nesse prado.

    if not (verifica_posicoes(rochedos, lim_prado)
            and verifica_posicoes(posicoes_animais, lim_prado)):
        raise ValueError("cria_prado: argumentos invalidos")

    for animal in animais:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")

    return {'lim_prado': lim_prado,
            'rochedos': list(rochedos),
            'animais': list(animais),
            'posicoes_animais': list(posicoes_animais)}


def cria_copia_prado(prado):
    # cria_copia_prado: prado → prado
    '''
    Recebe um prado e devolve uma cópia exata do mesmo (deep copy).
    '''
    prado_copia = {}
    prado_copia['lim_prado'] = cria_copia_posicao(prado['lim_prado'])
    prado_copia['rochedos'] = list(map(cria_copia_posicao, prado['rochedos']))
    prado_copia['animais'] = list(map(cria_copia_animal, prado['animais']))
    prado_copia['posicoes_animais'] = list(map(cria_copia_posicao,
                                               prado['posicoes_animais']))
    return prado_copia


def obter_tamanho_x(prado):
    # obter_tamanho_x: prado → int
    '''
    Devolve o tamanho do prado correspondente à componente x (Nx).
    '''
    LIM_PRADO = prado['lim_prado']

    return obter_pos_x(LIM_PRADO) + 1


def obter_tamanho_y(prado):
    # obter_tamanho_y: prado → int
    '''
    Devolve o tamanho do prado correspondente à componente y (Ny).
    '''
    LIM_PRADO = prado['lim_prado']

    return obter_pos_y(LIM_PRADO) + 1


def obter_numero_predadores(prado):
    # obter_numero_predadores: prado → int
    '''
    Recebe um prado e filtra-o, apenas para obter os predadores e depois devolve
    o número de predadores nesse prado.
    '''
    ANIMAIS = prado['animais']

    predadores = list(filter(eh_predador, ANIMAIS))

    return len(predadores)


def obter_numero_presas(prado):
    # obter_numero_presas: prado → int
    '''
    Recebe um prado e filtra-o, apenas para obter as presas e depois devolve o
    número de presas nesse prado.
    '''
    ANIMAIS = prado['animais']

    presas = list(filter(eh_presa, ANIMAIS))

    return len(presas)


def obter_posicao_animais(prado):
    # obter_posicao_animais: prado → tuplo posicoes
    '''
    Recebe um prado e devolve as suas posições com animais, organizadas de
    acordo com a ordem de leitura do prado.
    '''
    posicoes_animais = prado['posicoes_animais']

    return ordenar_posicoes(tuple(posicoes_animais))


def obter_animal(prado, posicao):
    # obter_animal: prado x posicao → animal
    '''Obtém um animal do prado que se encontra numa certa posição.

    Recebe um prado e vai percorrer todas as posições com animais até encontrar
    aquela que corresponde à posição recebida também como argumento. No fim,
    devolve o animal nessa posição.
    '''
    ANIMAIS = prado['animais']
    POSICOES_ANIMAIS = prado['posicoes_animais']

    posicao_cont = 0
    while not posicoes_iguais(posicao, POSICOES_ANIMAIS[posicao_cont]):
        posicao_cont += 1

    return ANIMAIS[posicao_cont]


def eliminar_animal(prado, posicao):
    # eliminar_animal: prado x posicao → prado
    '''Elimina um animal do prado numa certa posição.

    Recebe um prado e depois percorre as posições do prado com animais até
    achar aquela que corresponde à posição recebida também como argumento.
    No fim, elimina destrutivamente o animal nessa posição e devolve o prado
    modificado.
    '''
    animais = prado['animais']
    posicoes_animais = prado['posicoes_animais']

    posicao_cont = 0
    while not posicoes_iguais(posicao, posicoes_animais[posicao_cont]):
        posicao_cont += 1

    del posicoes_animais[posicao_cont]
    del animais[posicao_cont]

    return prado


def mover_animal(prado, posicao1, posicao2):
    # mover_animal: prado x posicao x posicao → prado
    '''Move um animal no prado entre duas posições.

    Recebe um prado e depois percorre as posições do prado com animais até
    achar aquela que corresponde à posição recebida como segundo argumento.
    No fim, altera destrutivamente essa posição com um animal, movendo-o
    para a posição recebida como terceiro argumento e devolve o prado modificado.
    '''
    posicoes_animais = prado['posicoes_animais']

    posicao_cont = 0
    while not posicoes_iguais(posicao1, posicoes_animais[posicao_cont]):
        posicao_cont += 1

    posicoes_animais[posicao_cont] = posicao2

    return prado


def inserir_animal(prado, animal, posicao):
    # inserir_animal: prado x animal x posicao → prado
    '''
    Recebe um prado e adiciona-lhe o animal (segundo argumento) numa
    determinada posição (terceiro argumento) e no fim devolve o prado
    modificado.
    '''
    animais = prado['animais']
    posicoes_animais = prado['posicoes_animais']

    animais.append(animal)
    posicoes_animais.append(posicao)

    return prado


def eh_prado(arg):
    # eh_prado: universal → booleano
    '''Verifica se o seu argumento é um prado.

    Para ser um prado, tem de respeitar a representação interna e tem de ter uma
    posição que delimite o prado, um tuplo com posições válidas para rochedos
    (pode estar vazio) e outro com posições válidas para animais (não pode estar
    vazio) e por fim um tuplo com animais válidos (tem de ter animais para cada
    posição).
    '''
    if not (isinstance(arg, dict) and 'lim_prado' in arg and 'rochedos' in arg
            and 'animais' in arg and 'posicoes_animais' in arg and len(arg) == 4):
        return False
        # Verifica se o seu argumento respeira a representação interna do prado.

    LIM_PRADO = arg['lim_prado']
    ROCHEDOS = arg['rochedos']
    ANIMAIS = arg['animais']
    POSICOES_ANIMAIS = arg['posicoes_animais']

    if not (type(ROCHEDOS) == type(ANIMAIS) == type(POSICOES_ANIMAIS) == list
            and eh_posicao(LIM_PRADO)):
        return False

    if len(ANIMAIS) == 0 or len(ANIMAIS) != len(POSICOES_ANIMAIS):
        return False

    if not (verifica_posicoes(tuple(ROCHEDOS), LIM_PRADO)
            and verifica_posicoes(tuple(POSICOES_ANIMAIS), LIM_PRADO)):
        return False

    for animal in ANIMAIS:
        if not eh_animal(animal): return False

    return True


def eh_posicao_animal(prado, posicao):
    # eh_posicao_animal: prado x posicao → booleano
    '''
    Recebe um prado e percorre todas as posições com animais, verificando se
    alguma dessas posições é igual à posição recebida como segundo argumento.
    '''
    POSICOES_ANIMAIS = prado['posicoes_animais']

    for posicao_animal in POSICOES_ANIMAIS:
        if posicoes_iguais(posicao, posicao_animal): return True

    return False


def eh_posicao_obstaculo(prado, posicao):
    # eh_posicao_obstaculo: prado x posicao → booleano
    '''Recebe um prado e uma posição.

    Verifica inicialmente se essa posição situa-se nas margens do prado que têm
    sempre obstáculos. Caso isto não se verifique, então percorre as posições do
    prado com rochedos e verifica se alguma delas é igual à nossa posição.
    '''
    ROCHEDOS = prado['rochedos']

    if (obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0
        or obter_pos_x(posicao) == obter_tamanho_x(prado) - 1
        or obter_pos_y(posicao) == obter_tamanho_y(prado) - 1):
        return True
        # Se a posição estiver nas margens do prado é um rochedo.

    for rochedo in ROCHEDOS:
        if posicoes_iguais(posicao, rochedo): return True

    return False


def eh_posicao_livre(prado, posicao):
    # eh_posicao_livre: prado x posicao → booleano
    '''
    Recebe um prado e verifica se não há animal nem obstáculo na posição
    recebida como segundo argumento.
    '''
    return not (eh_posicao_animal(prado, posicao)
                or eh_posicao_obstaculo(prado, posicao))


def prados_iguais(prado1, prado2):
    # prados_iguais: prado x prado → booleano
    '''Verifica se dois prados são iguais.

    Para este efeito, têm de ter a mesma dimensão, rochedos nas mesmas posições,
    os mesmos tipos de animais com características idênticas e que ocupam as
    mesmas posições em cada prado.
    '''
    LIM_PRADO1, LIM_PRADO2 = prado1['lim_prado'], prado2['lim_prado']
    ROCHEDOS1, ROCHEDOS2 = prado1['rochedos'], prado2['rochedos']
    ANIMAIS1, ANIMAIS2 = prado1['animais'], prado2['animais']
    POSICOES_ANIMAIS1 = prado1['posicoes_animais']
    POSICOES_ANIMAIS2 = prado2['posicoes_animais']

    if not (posicoes_iguais(LIM_PRADO1, LIM_PRADO2)
            and len(ROCHEDOS1) == len(ROCHEDOS2)
            and len(ANIMAIS1) == len(ANIMAIS2)):
        return False
        # Verifica se os prados têm o mesmo limite e o mesmo número de posições.

    for rochedo in range(len(ROCHEDOS1)):
        if not posicoes_iguais(ROCHEDOS1[rochedo], ROCHEDOS2[rochedo]):
            return False

    for animal in range(len(ANIMAIS1)):
        if not animais_iguais(ANIMAIS1[animal], ANIMAIS2[animal]):
            return False

        if not posicoes_iguais(POSICOES_ANIMAIS1[animal],
                               POSICOES_ANIMAIS2[animal]):
            return False

    return True


def prado_para_str(prado):
    # prado_para_str: prado → str
    '''Representa um prado em string com a sua dimensão.

    Os símbolos '+' e '|' representam os rochedos nas margens e '@' representa
    os rochedos no interior do prado, depois temos a rotina animal_para_char
    a representar cada animal e por fim temos '.' a representar as posições livres.
    '''
    LIM_PRADO_X = obter_tamanho_x(prado)
    LIM_PRADO_Y = obter_tamanho_y(prado)
    ROCHEDOS, POSICOES_ANIMAIS = prado['rochedos'], prado['posicoes_animais']
    POSICOES = ROCHEDOS + POSICOES_ANIMAIS

    inicial_final = ('+' + ''.join(list('-' for x in range(LIM_PRADO_X - 2))) + '+')
    meio = ('|' + ''.join(list('.' for x in range(LIM_PRADO_X - 2))) + '|\n')
    # Cria um exemplar de linha para o ínicio ou fim do prado e uma linha do meio.
    prado_para_str = ([inicial_final + '\n']
                      + list(meio for x in range(LIM_PRADO_Y - 2))
                      + [inicial_final])
    # Cria a representação externa do nosso prado.

    for posicao in POSICOES:
        linha = obter_pos_y(posicao)
        coluna = obter_pos_x(posicao)
        if eh_posicao_obstaculo(prado, posicao):
            prado_para_str[linha] = (prado_para_str[linha][:coluna] + '@'
                                     + prado_para_str[linha][coluna + 1:])
            # Adiciona os rochedos nas posições certas do nosso prado.
        else:
            prado_para_str[linha] = (prado_para_str[linha][:coluna]
                                     + animal_para_char(obter_animal(prado, posicao))
                                     + prado_para_str[linha][coluna + 1:])
            # Adiciona os animais nas posições certas do nosso prado.

    return ''.join(prado_para_str)


def obter_valor_numerico(prado, posicao):
    # obter_valor_numerico: prado x posicao → int
    '''
    Dado um prado e uma posição determina o valor que essa posição ocupa no prado.
    Para este efeito começamos a contar no zero a partir do canto superior
    esquerdo do prado e depois da esquerda para a direita, cima para baixo.
    '''
    return obter_tamanho_x(prado) * obter_pos_y(posicao) + obter_pos_x(posicao)


def obter_movimento(prado, posicao):
    # obter_movimento: prado x posicao → posicao
    '''Obtém o proximento movimento a partir de uma posição do prado.

    Dado um prado e uma posição, obtemos as posições adjacentes e delas, guardamos
    as posições que têm presas. Posto isto, verificamos se o nosso animal é um
    predador com presas à volta, caso isso aconteça, as posições adjacentes
    passam a ser as posições com presas. Caso uma dessas condições não se
    verifique, então as posições adjacentes são as posições livres. No fim,
    obtemos a posição adjacente.
    '''
    posicoes_adjacentes = obter_posicoes_adjacentes(posicao)

    so_presas = list(filter(lambda x: eh_posicao_animal(prado, x)
                and eh_presa(obter_animal(prado, x)), posicoes_adjacentes))
    # Guarda só as posições adjacentes com presas
    # (vazio se não houverem presas à volta).
    if so_presas != [] and eh_predador(obter_animal(prado, posicao)):
        posicoes_adjacentes = so_presas
        # Caso o animal na nossa posição seja um predador com presas à volta,
        # então as posições adjacentes passam a ser as presas à volta.
    else:
        posicoes_adjacentes = [pos for pos in posicoes_adjacentes
                               if eh_posicao_livre(prado, pos)]
        # Caso seja predador e não tenha presas à volta ou caso seja uma presa,
        # as posições adjacentes são todas as posições livres.

    p = len(posicoes_adjacentes)
    if p == 0:
        return posicao
        # O animal mantém-se na sua posição.
    else:
        return posicoes_adjacentes[obter_valor_numerico(prado, posicao) % p]


# ### Funções Adicionais ### #


def geracao(prado):
    # geracao: prado → prado
    '''Realiza uma geração completa no prado que recebe.

    Aumenta a idade e fome da cada animal. Depois verifica o movimento que o
    animal realiza no prado e consoante esse movimento, verifica se o animal
    se pode alimentar, reproduzir ou se morre. Caso ele não se mova, então
    verifica apenas se é faminto.
    '''
    posicoes_animais = obter_posicao_animais(prado)
    pos = 0
    while pos < len(posicoes_animais):
        prox_movimento = obter_movimento(prado, posicoes_animais[pos])
        animal = obter_animal(prado, posicoes_animais[pos])

        aumenta_idade(animal)
        aumenta_fome(animal)
        # Aumenta sempre a idade e fome do animal.
        if not posicoes_iguais(posicoes_animais[pos], prox_movimento):
            # Se o animal não se poder mover de lugar, então nunca se pode
            # alimentar nem reproduzir.
            if (eh_posicao_animal(prado, prox_movimento)
                and eh_presa(obter_animal(prado, prox_movimento))):
                eliminar_animal(prado, prox_movimento)
                reset_fome(animal)
                posicoes_animais = [posicoes_animais[p]
                                    for p in range(len(posicoes_animais))
                                    if not (posicoes_iguais(posicoes_animais[p],
                                    prox_movimento) and p > pos)]
            # Se tiver uma presa na posição para onde se vai mover, então
            # alimenta-se e elimina esse animal. Como essa nova posição está
            # agora ocupada por um animal que já se moveu, então já não é mais
            # verificada.

            if eh_animal_fertil(animal):
                inserir_animal(prado, reproduz_animal(animal),
                               posicoes_animais[pos])
            # Verifica se o animal está pronto a reproduzir-se, caso esteja,
            # então é reproduzido um novo animal na posição antiga do animal.

            mover_animal(prado, posicoes_animais[pos], prox_movimento)
            # Move sempre o animal para uma posição diferente daquela onde estava.

        if eh_animal_faminto(animal): eliminar_animal(prado, prox_movimento)
        # Verifica sempre após tudo o resto, se o animal está faminto, morrendo,
        # caso esteja.
        pos += 1

    return prado


def simula_ecossistema(ficheiro, geracoes, verboso):
    # simula_ecossistema: str x int x booleano → tuplo
    '''Simula um ecossistema com a informação que recebe com um determinado
    número de gerações.

    Lê a informação do prado na geração 0 de um ficheiro que recebe e converte
    essa informação num conteúdo legível pela função cria_prado, criando assim
    um prado inicial.

    Depois realiza vários ciclos em que é efetuada uma geração completa em cada
    um. Antes de cada geração é copiado o prado para ser comparado depois, caso
    o prado não se altere, então damos por concluida a simulação.

    Se o modo verboso estiver ativo, então após cada geração, será mostrada a
    informação se houver pelo menos alguma alteração no número de predadores ou
    presas. No modo quiet, apenas mostramos a informação antes e depois da
    simulação.
    '''
    with open(ficheiro) as file: dados = list(map(eval, file.readlines()))

    dados[1] = tuple(map(lambda x: cria_posicao(x[0], x[1]), dados[1]))
    animais = [cria_animal(animal[0], animal[1], animal[2])
               for animal in dados[2:]]
    posicoes_animais = [cria_posicao(animal[3][0], animal[3][1])
                        for animal in dados[2:]]
    prado = cria_prado(cria_posicao(dados[0][0], dados[0][1]), dados[1],
                       tuple(animais), tuple(posicoes_animais))
    gen = 0
    print(f"Predadores: {obter_numero_predadores(prado)}",
          f" vs Presas: {obter_numero_presas(prado)} (Gen. {gen})\n",
          prado_para_str(prado), sep = '')
    # Mostra o número de predadores e presas do prado antes da simulação.

    while gen < geracoes:
        gen += 1
        prado_antigo = cria_copia_prado(prado)
        geracao(prado)
        if prados_iguais(prado, prado_antigo) or gen == geracoes: break
        if (verboso and
        (obter_numero_predadores(prado) != obter_numero_predadores(prado_antigo)
        or obter_numero_presas(prado) != obter_numero_presas(prado_antigo))):
            print(f"Predadores: {obter_numero_predadores(prado)}",
                  f" vs Presas: {obter_numero_presas(prado)} (Gen. {gen})\n",
                  prado_para_str(prado), sep = '')

    if (not verboso) or (verboso and
       (obter_numero_predadores(prado) != obter_numero_predadores(prado_antigo)
        or obter_numero_presas(prado) != obter_numero_presas(prado_antigo))):
        print(f"Predadores: {obter_numero_predadores(prado)}",
              f" vs Presas: {obter_numero_presas(prado)} (Gen. {geracoes})\n",
              prado_para_str(prado), sep = '')
        # No final é mostrado o número de predadores e presas no prado no
        # final da simulação sempre se estiver no modo quiet, se não, apenas
        # é mostrado caso o número de predadores ou presas altere.

    return (obter_numero_predadores(prado), obter_numero_presas(prado))
