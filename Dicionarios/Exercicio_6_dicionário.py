# O dicionário de vendas fornecido
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

#Os valores individualmente
total_vendas = vendas.get('Janeiro', 0) + vendas.get('Fevereiro', 0) + vendas.get('Março', 0)

# Imprime o resultado
print(f"O total de vendas do trimestre é: {total_vendas}")