# script for simples pra ler valores de uma lista

lista = [1,2,3,4,5,6]
nova_lista = []  # possível fazer listas vazias, essa é a lista onde será armazenada novos valores

 # for é usado pra percorrer cada item em uma lista
for item in lista:   # item é a variável que vai armazenar cada valor na lista
    nova_lista.append(item * 2)  # append é o comando usado pra adicionar itens a lista

print(lista)
print(nova_lista)

# existe uma forma mais simples de fazer isso que é atravez de list comprehension.

             #sintaxe: variavel = [(operação) for item in lista]
nova_lista2 = [valor * 2 for valor in nova_lista]  # eu não preciso ter que criar primeiro uma lista vazia
                                                   # e depois ter que dar append em um loop for.

print(nova_lista2)
