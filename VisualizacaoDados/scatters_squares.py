import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

#Define o titulo do grafico e nomeia os eixos
plt.title("Squares Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho do rotulo das marcacoes
plt.tick_params(axis='both', which='major', labelsize=14)

#Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()

'''
scatter(x, y) - plota um unico ponto de acordo com as cordenadas de x e y

axis() especifica o valor de cada eixo / exige 4 valores:
    - valores minimos e maximos para eixo x e eixo y
    
savefig() - salva o grafico automaticamente
    - 1 arg: nome do arquivo que sera salvo no mesmo diretorio que scatter_squares.py
    -2 arg: remove espacos em branco extras do grafico
'''