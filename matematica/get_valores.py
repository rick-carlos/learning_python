# Uma classe pra criar uma lista de valores inteiros

class LeitorDeValores():
    def __init__(self):
        self.valores = []

    def formatar_valores(self):  # Converter a string em inteiros
        while True:
            try:
                numeros = input("Digite os valores, se for mais de um, separado por espaço")
                self.valores = [int(valor) for valor in numeros.split()]
                # split() é usado pra separar os valores da string, o separador vai ser definido entre o (), como ('-')
                # se nada for definido, então o separador será o espaço.
                break
            except ValueError:
                print("Valores incorretos, tente novamente")

    def pegar_valores(self):
        return self.valores # pegar valores armazenados na lista self.valores que agora já estão formatados pra inteiros

    def limpar(self):  # usada pra limpar os valores da lista
        self.valores.clear()
