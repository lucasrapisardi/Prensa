import math
from resmat import separator, nome_mats, mat_esc


class Calculos:

    @classmethod
    def tensaoCis(cls):
        separator()
        print('')
        print(f"Função selecionada: Tensão de cisalhamento sobre o(s) rebite(s).\n")
        Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
        n = float(input(f"Número de rebites: "))
        N = float(input(f"Quantidade de pontos onde o rebite sofrerá cisalhamento: "))
        d = float(input(f"Diâmetro do(s) rebite(s) [mm]: "))

        #calculo da tensão de cisalhamento sobre o(s) rebite(s)
        result_cis = round(Q/(n*N*(math.pi/4)*math.pow(d, 2)))

        #exibe o resultado do cálculo em MPa
        print(f"\nTensão de cisalhamento sobre os rebites: {result_cis}MPa")

        #compara o resultado do cálculo com os valores da biblioteca de materiais,
        #retornando o valor mais próximo disponível
        result = [mat_esc - result_cis for mat_esc in mat_esc]
        resultIndex = min([result for result in result if result > 0])
        posIndex = result.index(resultIndex)

        #encontra o material que possui a propriedade 
        #com o valor encontrado na comparação acima
        posNome = nome_mats[posIndex]
        posCis = mat_esc[posIndex]

        if posIndex == 0:
            return print("""Nenhum dos materiais da base de materiais possui resistência suficiente para a aplicação.
    Tente aumentar a quantidade de rebites ou seu diâmetro.\n"""), separator()

        else:
            return print(f"""O material mais indicado para sua aplicação, considerando a resistência do material, é o {posNome}, 
    com uma tensão limite de {posCis}MPa.\n"""), separator()

    
    @classmethod #Momento Fletor
    def momFletor(cls):
        separator()
        print(f"\nFunção selecionada: Cálculo de Momento Fletor.")

        F = float(input(f"Intensidade da força que origina o Momento Fletor [N]: "))
        l = float(input(f"Distância entre o ponto de referência e o ponto onde a força é aplicada[m]: "))

        resMomento = F*l

        return print(f"\nO valor do momento fletor é de {round(resMomento, 2)}Nm\n"), separator()

    @classmethod #Tensão máxima de flexão
    def maxFlexao(cls):
        separator()
        print(f"\nFunção selecionada: Tensão Máxima de Flexão.")

        M = float(input(f"Momento fletor sobre a peça [Nm]: "))
        y = float(input(f"Raio do rebite [m]: "))
        I = float(input(f"Momento de inércia da geometria [m⁴]: "))

        flexao = M*y/I*(1e-6)

        return print(f"""
    A tensão máxima de flexão para o rebite é de {round(flexao, 2)}MPa
    """), separator()

    @classmethod
    def tensNormal():
        A = float(input(f"Área da peça [m²]: "))
        N = float(input(f"Força a ser aplicada: "))

        E = N/A

        return E