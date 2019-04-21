import pygal
from die import Die

# Cria um dado D6 e um dado D10

die_1 = Die()
die_2 = Die()

# Faz alguns lancamentos e armazena na lista de resultados
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequecy = results.count(value)
    frequencies.append(frequecy)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times"
hist.x_labels = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)

hist.render_to_file('different_dice.svg')