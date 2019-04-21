import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

#Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho dos rotulos das marcaçoes
plt.tick_params(axis='both', labelsize=14)

plt.show()

'''
plot() - cria o grafico
tittle() - cria titulo para o grafico / parametro fontsize" define o tamanho da letra"
xlabel() - titulo para o eixo x
ylabel() - titulo para o eixo y
tick_params() - estiliza as marcacoes nos eixos / parametro "axes" define a estilizacao ds marcacoes em ambos os eixos
show() - mostra o grafico
'''

