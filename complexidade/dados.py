dados = []           
MAX = 0              
tipo = None           
ponteiro = -1         
spos = 0              
rpos = 0              


def ler_inteiro(mensagem):
    
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido!")


# ==========================================================
# PILHA
# ==========================================================
def pilha_init(tamanho):
    global dados, ponteiro, MAX, tipo
    dados = []
    ponteiro = -1
    MAX = tamanho
    tipo = "pilha"


def pilha_push(valor):
    global dados, ponteiro, MAX
    if ponteiro == MAX - 1:
        print("\nPilha Cheia!!!")
        return
    dados.append(valor)
    ponteiro = ponteiro + 1


def pilha_pop():
    global dados, ponteiro
    if ponteiro < 0:
        print("\nA pilha já está vazia")
        return None
    else:
        valor = dados[ponteiro]
        del dados[ponteiro]
        ponteiro = ponteiro - 1
        return valor


def pilha_show():
    global dados
    print(dados)


# ==========================================================
# FILA
# ==========================================================
def fila_init(tamanho):
    global dados, spos, rpos, MAX, tipo
    MAX = tamanho
    dados = []
    spos = 0
    rpos = 0
    tipo = "fila"


def fila_push(valor):
    global spos, dados
    if spos == MAX:
        print("Fila cheia!!!")
        return
    dados.append(valor)
    spos = spos + 1


def fila_pop():
    global rpos, dados
    if rpos == spos:
        print("Fila Vazia!!")
        return None
    rpos = rpos + 1
    return dados[rpos - 1]


def fila_show():
    global spos, rpos, dados
    if rpos == spos:
        print("Fila vazia!!")
        return
    for i in range(rpos, spos):
        print(dados[i])


def fila_showp():
    print("rpos = ", rpos, " spos = ", spos, " MAX = ", MAX)


# ==========================================================
# FILA CIRCULAR
# ==========================================================
def circ_init(maximo):
    global dados, spos, rpos, MAX, tipo
    MAX = maximo
    dados = []
    for i in range(0, MAX):
        dados.append(None)
    spos = 0
    rpos = 0
    tipo = "circular"


def circ_push(valor):
    global dados, spos
    if (rpos == spos and dados[rpos] != None) or (spos + 1 == MAX and rpos == 0):
        print("Fila cheia!!!")
        return
    if (spos + 1 == MAX) and (rpos != 0):
        spos = 0
    dados[spos] = valor
    spos = spos + 1


def circ_pop():
    global dados, rpos
    if rpos == spos and dados[rpos] == None:
        print("Fila vazia!!!")
        return None
    if rpos + 1 == MAX:
        rpos = 0
    valor = dados[rpos]
    dados[rpos] = None
    rpos = rpos + 1
    return valor


def circ_show():
    for i in range(0, MAX):
        print(dados[i])


def circ_showp():
    print("rpos = ", rpos, " spos = ", spos, " MAX = ", MAX)


# ==========================================================
# ALGORITMOS DE ORDENAÇÃO 
# ==========================================================
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
    return lista


# ==========================================================
# Ligação entre a ordenação e as estruturas
# ==========================================================
def obter_elementos():
   
    if tipo == "pilha":
        return list(dados)
    elif tipo == "fila":
        return list(dados[rpos:spos])
    else:
        elementos = []
        for k in range(MAX):
            valor = dados[(rpos + k) % MAX]
            if valor is not None:
                elementos.append(valor)
        return elementos


def gravar_elementos(ordenados):
   
    global dados, rpos, spos
    if tipo == "pilha":
        dados = ordenados
    elif tipo == "fila":
        dados = ordenados
        rpos = 0
        spos = len(ordenados)
    else: 
        dados = [None] * MAX
        for i in range(len(ordenados)):
            dados[i] = ordenados[i]
        rpos = 0
        spos = len(ordenados) if len(ordenados) < MAX else 0


# ==========================================================
# MENUS
# ==========================================================
def menu_principal():
    print("\n***********************************")
    print("| Estruturas de Dados e Ordenação |")
    print("-----------------------------------")
    print("| 1 - PILHA                       |")
    print("| 2 - FILA                        |")
    print("| 3 - FILA CIRCULAR               |")
    print("| 4 - ORDENAR                     |")
    print("| 5 - SAIR                        |")
    print("-----------------------------------")
    return ler_inteiro("Digite a opção desejada: ")


def menu_estrutura(titulo, f_init, f_push, f_pop, f_show, f_showp=None):
    
    while True:
        print("\n-----------------------------------")
        print("|", titulo.center(31), "|")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteúdo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")
        opt = ler_inteiro("Digite a opção desejada: ")

        if opt == 5:
            print("Voltando ao menu anterior")
            break
        elif opt == 1:
            tamanho = ler_inteiro("Digite o tamanho da estrutura: ")
            f_init(tamanho)
            print("Estrutura criada!")
        elif opt in (2, 3, 4) and tipo != titulo_para_tipo(titulo):
            print("Crie a estrutura primeiro (opção 1)!")
        elif opt == 2:
            valor = ler_inteiro("Digite o valor a armazenar: ")
            f_push(valor)
        elif opt == 3:
            valor = f_pop()
            if valor is not None:
                print("Valor extraído:", valor)
        elif opt == 4:
            f_show()
            if f_showp:
                f_showp()
        else:
            print("Opção inexistente")


def titulo_para_tipo(titulo):
    return {"PILHA": "pilha", "FILA": "fila", "FILA CIRCULAR": "circular"}[titulo]


def menu_ordenar():
    while True:
        print("\n-----------------------------------")
        print("| Ordenar                         |")
        print("-----------------------------------")
        print("| 1 - Bubble Sort                 |")
        print("| 2 - Selection Sort              |")
        print("| 3 - Insertion Sort              |")
        print("| 4 - Voltar ao menu anterior     |")
        print("-----------------------------------")
        opt = ler_inteiro("Digite a opção desejada: ")

        if opt == 4:
            print("Voltando ao menu anterior")
            break
        elif opt in (1, 2, 3):
            if tipo is None:
                print("Nenhuma estrutura criada! Escolha primeiro uma das "
                      "três primeiras opções do menu principal (Pilha, Fila ou Fila Circular).")
                break
            elementos = obter_elementos()
            if len(elementos) == 0:
                print("A estrutura está vazia. Armazene valores antes de ordenar.")
                continue
            print("Antes :", elementos)
            if opt == 1:
                ordenados = bubble_sort(elementos)
            elif opt == 2:
                ordenados = selection_sort(elementos)
            else:
                ordenados = insertion_sort(elementos)
            gravar_elementos(ordenados)
            print("Depois:", ordenados)
        else:
            print("Opção inexistente")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================
while True:
    opt1 = menu_principal()

    if opt1 == 5:
        break
    elif opt1 == 1:
        menu_estrutura("PILHA", pilha_init, pilha_push, pilha_pop, pilha_show)
    elif opt1 == 2:
        menu_estrutura("FILA", fila_init, fila_push, fila_pop, fila_show, fila_showp)
    elif opt1 == 3:
        menu_estrutura("FILA CIRCULAR", circ_init, circ_push, circ_pop, circ_show, circ_showp)
    elif opt1 == 4:
        menu_ordenar()
    else:
        print("Opção inexistente")

print("Programa finalizado")