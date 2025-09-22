palavra = str(input("Introduza uma palavra: "))

print(f"A palavra introduzida foi: {palavra}")

palavra_ordenada = ""

for letra in sorted(palavra):
    palavra_ordenada += letra
    
print(f"A palavra ordenada alfabeticamente é: {palavra_ordenada}")