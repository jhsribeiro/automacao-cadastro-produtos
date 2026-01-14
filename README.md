# Automação de Cadastro de Produtos

Este projeto automatiza o processo de cadastro de mercadorias num sistema web, utilizando scripts para ler uma base de dados e preencher formulários automaticamente.

## Stack de Tecnologia
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-yellow?style=for-the-badge&logo=python&logoColor=white)](https://pyautogui.readthedocs.io/)
[![Time](https://img.shields.io/badge/Time-Library-blue?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/time.html)

* **Python**: Linguagem de programação principal.
* **PyAutoGUI**: Biblioteca para automação de interface gráfica, controlo de rato e teclado.
* **Pandas**: Utilizada para a leitura e manipulação da base de dados em formato CSV.
* **Time**: Módulo para gestão de pausas e sincronização entre as ações do script.

## Funcionalidades
* **Acesso e Login**: Abre o navegador (Microsoft Edge) e realiza o login automaticamente no sistema através de link e credenciais predefinidas.
* **Processamento de Dados**: Carrega as informações dos produtos a partir do ficheiro `produtos.csv`.
* **Cadastro em Lote**: Itera por todas as linhas da tabela, preenchendo campos como código, marca, tipo, categoria, preço unitário, custo e observações.
* **Navegação Inteligente**: Utiliza comandos de teclado (`tab`, `enter`) para alternar entre campos e `scroll` para navegar na interface.

## Estrutura de Ficheiros
* `main.py`: Script principal que contém o fluxo completo da automação.
* `auxiliar.py`: Ferramenta de apoio utilizada para identificar as coordenadas (x, y) do rato no ecrã.
* `produtos.csv`: Base de dados contendo a lista de produtos com as colunas: código, marca, tipo, categoria, preço, custo e obs.