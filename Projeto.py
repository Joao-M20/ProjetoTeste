import time
import pyautogui

# def Comecar():
#     time.sleep(2)
#     copiar = pyautogui.hotkey('ctrl', 'c')
    
print("")
print("-------------------------------------------------------------")
quantidadeDevolucao = int(input("Quantas devoluções chegaram?"))
print("-------------------------------------------------------------")
print("")


i = 1
j = 1
contador = 0
nomes = []
nfs = []

while i <= quantidadeDevolucao:
    Nome = input("Digite o nome:")
    nomes.append(Nome)
    NF = input("Digite o Nº da Nota Fiscal:")
    print("")
    nfs.append(NF)
    print("----------------------------------")
    i = i + 1

time.sleep(4)

while j <= quantidadeDevolucao:
    pyautogui.write(nomes[contador])
    pyautogui.hotkey('tab')
    pyautogui.write(nfs[contador])
    pyautogui.hotkey('enter')
    contador = contador + 1
    j = j + 1    

