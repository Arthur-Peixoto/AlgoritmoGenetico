import random as rd
import math as math
import matplotlib.pyplot as plt

# Função de aptidão (fitness) - Esta é a função que queremos otimizar
def funcao(individuo):
    valor = math.sqrt(individuo[0] ** 3 + 2 * individuo[1] ** 4)

    if valor == 0:
        return -1

    return 1 / valor

# Função para converter um número decimal em uma representação binária de 3 bits
def decimalParaBinario(decNumero):
    remstack = []

    if decNumero == 0:
        return "000"
    while decNumero > 0:
        rem = decNumero % 2
        remstack.append(rem)
        decNumero = decNumero // 2

    binString = ""
    while len(remstack) != 0:
        binString = binString + str(remstack.pop())

    while len(binString) < 3:
        binString = "0" + binString

    return binString

# Função para converter uma representação binária de 3 bits em um número decimal
def binarioParaDecimal(numBinario):
    binario = int(numBinario)

    decimal, i, n = 0, 0, 0
    while binario != 0:
        dec = binario % 10
        decimal = decimal + dec * pow(2, i)
        binario = binario // 10
        i += 1
    return decimal

# Função para criar uma população inicial aleatória de tamanho tamPopulacao
def criarPopulacao(tamPopulacao):
    populacao = []
    for x in range(tamPopulacao):
        populacao.append((rd.randint(0, 7), rd.randint(0, 7)))

    return populacao

def selecao(populacao):
    selecionados = []
    aptidoes = [funcao(individuo) for individuo in populacao]

    total_aptidoes = sum(aptidoes)
    probabilidade_selecao = [aptidao / total_aptidoes for aptidao in aptidoes]

    for _ in range(len(populacao)):
        selecionado1 = rd.choices(populacao, probabilidade_selecao)[0]
        selecionado2 = rd.choices(populacao, probabilidade_selecao)[0]
        selecionados.append((selecionado1, selecionado2))

    return selecionados

# Função de cruzamento de indivíduos selecionados (melhorada)
def cruzamento(selecionados):
    nova_populacao = []

    for pai1, pai2 in selecionados:
        # Escolher dois pontos de corte distintos
        pontos_de_corte = sorted(rd.sample(range(len(pai1)), 2))

        ponto_corte1, ponto_corte2 = pontos_de_corte[0], pontos_de_corte[1]

        # Realizar o cruzamento de dois pontos
        filho1 = pai1[:ponto_corte1] + pai2[ponto_corte1:ponto_corte2] + pai1[ponto_corte2:]
        filho2 = pai2[:ponto_corte1] + pai1[ponto_corte1:ponto_corte2] + pai2[ponto_corte2:]

        # Aplicar a mutação aos filhos
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)

        nova_populacao.append(filho1)
        nova_populacao.append(filho2)

    return nova_populacao

plotgrafico = []
num = 0

# Função principal do algoritmo genético
def main(tamPopulacao):
    conteVezesRepetidas = 1
    MelhoresValoresEmCadaGeracao = []
    populacao = criarPopulacao(tamPopulacao)

    teste = False
    while teste != True:
        resultadoV = []

        for individuo in populacao:
            resultadoV.append((funcao(individuo), individuo))

        resultadoV.sort()
        MelhoresValoresEmCadaGeracao.append(resultadoV[0][0])
        plotgrafico = MelhoresValoresEmCadaGeracao

        # Condição de parada
        if resultadoV[0][0] == -1:
            teste = True
            plt.plot(MelhoresValoresEmCadaGeracao)
            plt.title("Algoritmo Genético")
            plt.show()

        # Mostrar iteração e o resultado da geração
        print(f"Geração {conteVezesRepetidas}")
        print(resultadoV[0][0], " : ", resultadoV[0][1])

        selecionadosCruzamento = selecao(resultadoV)
        populacao = cruzamento(selecionadosCruzamento)
        conteVezesRepetidas += 1
        num = conteVezesRepetidas

main(4)
