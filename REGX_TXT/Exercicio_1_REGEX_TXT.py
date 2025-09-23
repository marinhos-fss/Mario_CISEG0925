#Exercicio 1: Ler o ficheiro dados.txt 
x = r"C:\DEV\Mario_Santos_CISEG0925\Mario_CISEG0925\REGX_TXT\dados.txt"

conteudo = ""

with open(x, 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print(conteudo)