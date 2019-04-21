# Busca os 3 primeiros jogadores

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print()
print()

# Busca a partir do 2 jogador ate o 4 jogador
print(players[1:4])


print()
print()


# 4 primeiros jogadores
print(players[:4])


print()
print()

# Busca a partir do 3 jogador
print(players[2:])


print()
print("-----------------------------------------------------------------------------------------")

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first 3 players on my team:")
for player in players[:3]:
    print(player.title())