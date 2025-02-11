import numpy as np
import matematica.get_valores as matgetvalor

# Fórmula é a soma dos elementos dividido pela quantidade de elementos

numeros = matgetvalor.LeitorDeValores()  # Criando uma instância de classe numeros
numeros.formatar_valores()               # Input e conversão dos números
elementos = numeros.pegar_valores()      # pegar a lista

media = np.mean(elementos)  # mean é uma função do numpy que faz a média aritmética automaticamente dos elementos
print(int(media))           # conversão pra inteiro e print do resultado.









