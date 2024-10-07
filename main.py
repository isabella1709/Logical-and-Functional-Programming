#Isabella, Michele, Yejin

# Importar bibliotecas (to_cnf é a função que converte para FNC)
from sympy import symbols, Not, And, Or, to_cnf, latex
# Módulo de expressões regulares, usado para buscar variáveis dentro das fórmulas.
import re

# Converte o latex para o sympy
def latex_para_sympy(latex_fbf):
    latex_fbf = latex_fbf.replace(r'\neg', '~').replace(r'\lou', '|').replace(r'\le', '&')
    return latex_fbf

# Ler o arquivo de entrada
def ler_arquivo_entrada(entrada):
    with open(entrada, 'r') as file:
        linha = file.readlines()
        num_fbf = int(linha[0].strip())
        fbf_list = [line.strip() for line in linha[1:num_fbf + 1]]
    return fbf_list


# Escrever arquivo de saída
def escrever_arquivo_saida(saida, fnc_lista):
    with open(saida, 'w') as file:
        for fnc in fnc_lista:
            file.write(latex(fnc) + '\n')

# Converter FBF para FNC
def converter_fbf_para_fnc(fbf_lista):
    fnc_lista = []
    for fbf in fbf_lista:
        sympy_fbf = latex_para_sympy(fbf)
        # Encontra todas as letras na fórmula.
        variaveis = re.findall(r'[a-zA-Z]', sympy_fbf)
        # Avaliar a expressão usando eval e a biblioteca sympy
        sympy_expr = eval(sympy_fbf, {var: symbols(var) for var in variaveis})
        fnc = to_cnf(sympy_expr, simplify=True)
        fnc_lista.append(fnc)

    return fnc_lista

def imprimir(fnc_list):
    for i, fnc in enumerate(fnc_list, 1):
        print(f"Fórmula {i}: {fnc}")

def main(input_arquivo, output_arquivo):
    fbf_list = ler_arquivo_entrada(input_arquivo)
    fnc_list = converter_fbf_para_fnc(fbf_list)
    escrever_arquivo_saida(output_arquivo, fnc_list)
    imprimir(fnc_list)

if __name__ == '__main__':
    input_arquivo = 'entrada.txt'
    output_arquivo = 'saida.txt'
    main(input_arquivo, output_arquivo)

