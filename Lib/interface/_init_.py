from tkinter.tix import InputOnly

def linha(tam = 42):
    return "-"*tam

def intro(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def option(n, on):
    print(f"{n} - {on}")

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar nenhum valor.\033[m")
            print("\033[31mFinalizando...\033[m".center(42))
            return -1
        except(ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        else:
            return n
    
def menu(list):
    intro("MAIN MENU")
    c = 1
    for item in list:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+= 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc