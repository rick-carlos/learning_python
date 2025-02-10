
#um simples script pra ler o conteúdo de um arquivo de texto no mesmo diretório.

try:
    with open("arquivo.txt", 'r') as texto: #with permitir abrir arquivos sem se preocupar em fecha-los.
        conteudo = texto.read()             # pra não precisar ter que digitar texto.read()
        print("conteúdo do arquivo \n")
        print(conteudo)
except FileNotFoundError:                   #isso é um tratamento de erro, se não ouver arquivo a ser lido, este bloco será executado.
    print("Arquivo não existente")

finally:
    print("fim da operação")                #finnaly é o bloco final a ser executado e finaliza o contexto do try:


#A vantagem do try é que o programa não trava quando um erro aparece