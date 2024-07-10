# passo 1 - entrar no sistema
# passo 2 - fazer login
# passo 3 - importar base de dados
# passo 4 - cadastrar produto
# passo 5 - repetir tarefa ate acabar

import pyautogui
import time
# pyautogui.click - clicar com o mause
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rolar a tela para cima e para baixo

pyautogui.PAUSE = 0.5

# passo 1 - entrar no sistema
# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1.5)
# pyautogui.press('tab')

# Passo 2 - fazer login
# pyautogui.click(x=568, y=445) pode usar a posiçao para clicar
pyautogui.press('tab')
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab')
pyautogui.write('minha senha')
# pyautogui.click(x=556, y=550) pode usar a posiçao para clicar 
pyautogui.press('tab')
pyautogui.press('enter')

# passo 3 - importar a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

print(tabela)

# Passo 4 cadastar o produto
# para cada linha da minha tabela:
for linha in tabela.index:
#codigo
    # pyautogui.press('tab')
    pyautogui.click(x=288, y=310)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    # marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(marca)
    # tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(tipo)
    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)
    # preço-unitario
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)
    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.press('tab')
    pyautogui.write(categoria)
    # obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':     
        pyautogui.write(obs)
    #clicar no botão de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
    #retornar a pagina para cima ou pode usar o scroll
    pyautogui.scroll(5000)
    # pyautogui.press('pgup')

# passo 5 - repetir para todas as linhas da tabela