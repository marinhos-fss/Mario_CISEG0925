def calcular_soma_key(key):
    soma = 0
    for char in key:
        soma += ord(char)
    return soma

def encriptografar(message, key):
    if not key:
        print("Erro: A chave não pode ser vazia.")
        return None
    
    soma_key = calcular_soma_key(key)
    codigos_encriptografados = []
    
    for char in message:
        valor_ascii = ord(char)
        valor_encriptografado = valor_ascii + soma_key
        
        if valor_ascii >= 32 and valor_ascii <= 126:
            intervalo = 126 - 32 + 1
            novo_valor = (valor_encriptografado - 32) % intervalo + 32
            codigos_encriptografados.append(novo_valor)
        else:
            codigos_encriptografados.append(valor_encriptografado)
            
    return codigos_encriptografados

def descriptografar(codigos, key):
    if not key:
        print("Erro: A chave não pode ser vazia.")
        return None
    
    soma_key = calcular_soma_key(key)
    mensagem_descriptografada = ""
    
    for codigo in codigos:
        valor_descriptografado = codigo - soma_key
        
        if 0 <= valor_descriptografado <= 255:
            mensagem_descriptografada += chr(valor_descriptografado)
        else:
            mensagem_descriptografada += '?'
            print(f"Aviso: Valor inválido {valor_descriptografado} encontrado na descriptografia. Caractere substituído por '?'.")
            
    return mensagem_descriptografada

def listar(codigos):
    print("Encrypted Codes:", codigos)

# Exemplo de uso
message = "Olá Mundo"
key = "key"

if key:
    encrypted_codes = encriptografar(message, key)
    if encrypted_codes is not None:
        listar(encrypted_codes)
    
        decrypted_message = descriptografar(encrypted_codes, key)
        if decrypted_message is not None:
            print("Decrypted Message:", decrypted_message)
else:
    print("Erro: A chave não pode ser vazia.")