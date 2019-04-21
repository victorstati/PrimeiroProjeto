from random import choice

# Define a classe do passeio aleatorio

class RandomWalk():

    # Inicializa os atributos de um passeio

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Todos os passeios comecam em (0, 0)

        self.x_values = [0]
        self.y_values = [0]


    # Calcula todos os pontos do passeio

    def fill_walk(self):

        # Continua dando passos ate que o passeio alcance o tamanho desejado

        while len(self.x_values) < self.num_points:

            # Decide a direcao a ser seguida e distancia a ser percorrida nessa direcao

            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeita movimentos que nao vao a lugar nenhum

            if x_step == 0 and y_step == 0:
                continue

            # Calcula os proximos valores de x e y

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



'''
fill_walk() - preencher passeios com pontos e determinar a direcao de cada passo
'''