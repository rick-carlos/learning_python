import matplotlib.pyplot as plt

# matplotlib é o módulo pra criar gráficos e planos cartesianos


a, b = plt.subplots()               # a é o espaço onde os gráficos serão desenhados, b representa o eixo da figura
b.plot([1,2,3,5],[1,4,3,5])   # criando 2 eixos no objeto b, o eixo x e y respectivamente
plt.show()                          # renderiza o gráfico




