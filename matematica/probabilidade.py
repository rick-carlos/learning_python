# Calcula probabilidade simples
class Probabilidade:
    @staticmethod    # Como essa classe não vai armazenar valores, o método pode ser estático.
    def resultado():
        while True:  # O loop while é ativado pra repetir o código caso algum erro aconteça.
            try:     # Try é chamado pra lidar com os erros de exceção

                a = float(input("Qual a quantidade de números desejáveis?"))  # As entradas são convertidas pra float
                b = float(input("Qual a quantidade de números totais?"))

                if a < 0 or b <= 0:  # Checa se os valores são corretos pra conta funcionar
                    raise ValueError("Valores inválidos, tente novamente")
                    # 'raise ValueError' cria um alerta de exceção personalizado que encerrará o bloco do programa
                    # mas ele será reiniciado já que está dentro de um loop while.

                break  # Caso nenhum erro ocorra, o loop while será encerrado e a conta continuará

            except ValueError as e:  # Alerta de exceção pra caso letras sejam inseridas ao invés de números
                print(f'Erro: {e}, tente novamente')  # Isso forçará o reinicio do programa.

        resultado = round((a/b) * 100)  # É um conversor, vai arredondar números decimais e transformar pra inteiro
        print(f"A chance de acerto é de {resultado}%")

