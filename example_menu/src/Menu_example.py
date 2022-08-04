from operator import indexOf
from Lib.interface._init_ import *
from Lib.arquivo.open_arq import *

data = "C:\\Users\\inafu\\OneDrive\\Área de Trabalho\\Git\\Py_Projects\\example_menu\\data\\data.txt"

if not arquivoExiste(data):
    criarArquivo(data)

from time import sleep
# Para 3 opções:
while True:
    resp = menu(["Ver Cadastros", "Cadastrar", "Sair do sistema"])
    if(resp == 1):
        print("Opção 1")
        lerArquivo(data)
    elif(resp == 2):
        print("Opção 2")
        intro("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        novoCadastro(data, nome, idade)
    elif(resp == 3):
        print("Saindo do sistema...  Até logo!!!")
        break
    elif(resp == -1):
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(1)