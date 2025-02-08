#código em construção


class Probabilidade:
    def __init__(self):
        self.A = None
        self.B = None

    def resultado(self):
        try:

            self.A = input("Qual a quantidade de números desejáveis?")
            self.B = map(int(input("Qual a quantidade de números totais?")))

            if self.B == 0:
                print("Erro, não é possível dividir por 0, tente novamente")
                self.B = input("Qual a quantidade de números totais?")
            else:
                break




