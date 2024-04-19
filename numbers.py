with open('numbers.txt', 'r') as arquivo: 
     conteudo = arquivo.read() 
print(conteudo)


numeros = conteudo.split(',')


for numero in numeros: 
    print(numero.strip())
