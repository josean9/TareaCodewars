def anagrams(anagramas):
    resultado = {}
    for letra in anagramas:
        x = "".join(sorted(letra))
        if x in resultado:
            resultado[x].append(letra)
        else:
            resultado[x] = [letra]
    return print(list(resultado.values()))

lista = []
numagramas = int(input('palabras a agrupar en anagramas?'))
print('ultimo')
while len(lista)<=numagramas-1:
    global anagramas
    anagramas = lista.append(input(f' anagrama numero {int(numagramas)-len(lista)} '))
else:
    anagrams(lista)
anagrams(["hola", "aloh"])
    
