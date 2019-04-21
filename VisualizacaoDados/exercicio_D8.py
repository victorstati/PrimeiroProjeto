import  pygal
from die import Die

die_1 = Die()
die_2 = Die()

# Lancar dados e armazenar na lista
resultados = []

for jogadas in range(1000):
    resultado = die_1.roll() + die_2.roll()
    resultados.append(resultado)

# Analisar os resultados
frequencias = []

resultado_maximo = die_1.num_sides + die_2.num_sides

for valor in range(2, resultado_maximo+1):
    frequencia = resultados.count(valor)
    frequencias.append(frequencia)


# Visualizar resultados

hist = pygal.Bar()

hist.title = "Resultados de dois dados D8 em 1000 jogadas"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Resultado"
hist.y_title = "Frequencia dos Resultados"

hist.add('D8 + D8', frequencias)
hist.render_to_file('exercicio_D8.svg')