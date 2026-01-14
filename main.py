import pyautogui
import time

pyautogui.PAUSE = 0.5 # tempo de espera entre as ações
link = 'http://10.0.70.29:3000/'
email = 'joao@gmail.com'

# 1. entrar no sistema da empresa
# abrir o navegador 
pyautogui.press('win')
pyautogui.write('microsoft edge') 
pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 't') # abrir uma nova aba
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(2) # esperar a página carregar

# 2. Fazer o login
pyautogui.click(x=2789, y=513) # clicar no campo de email
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write('joao@1234')
pyautogui.press('tab') # ir para o botão de login
pyautogui.press('enter')
time.sleep(5) # esperar a página carregar

# 3. Abrir a base de dados. 
import pandas as pd

tabela = pd.read_csv('produtos.csv')


# 4. Cadastrar um produto.
# para cada linha da tabela
for linha in tabela.index: 
# clicar no 1° campo do formulário 
    pyautogui.click(x=2467, y=361)

# codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

# marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

# tipo 
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

# categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

# preço
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

# custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

# observação
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs): # verificar se a observação não está vazia (NaN)
        pyautogui.write(obs)
    pyautogui.press('tab') # ir para o botão de salvar
    
    # salvar o produto
    pyautogui.press('enter') 

# 6. Repetir o passo 4 até acabar a lista de produtos    
    time.sleep(0.5) # esperar o sistema processar o cadastro
    pyautogui.scroll(5000) # voltar para o topo da página para cadastrar o próximo produto

# Fim do programa