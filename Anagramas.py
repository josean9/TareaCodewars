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
numagramas = int(input('cuantas palabras quieres agrupar en anagramas?'))
print('empezamos con el ultimo')
while len(lista)<=numagramas-1:
    global anagramas
    anagramas = lista.append(input(f'dime el anagrama numero {int(numagramas)-len(lista)} '))
else:
    anagrams(lista)
anagrams(["hola", "aloh"])
    
