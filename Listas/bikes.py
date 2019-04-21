bikes = ["trek", "cannondale", "redline", "specialized"]

print(bikes)

print(bikes[0])

message = "My first bike was a " + bikes[2].title() + "."
print(message)


print()
print()


motos = ["honda", "yamaha", "suzuki"]
print(motos)

motos[0] = "ducatti"
print(motos)

print()
print()



# Acrescentando elementos em uma lista
# append() - acrescenta elementos no final da lista
motos.append("bmw")
print(motos)

print()
print()

# Inserindo elementos em uma lista
motos.insert(0, 'cb1000')
print(motos)


# Deletando elementos de uma lista
print(motos)
del motos[0]

print(motos)

print()
print()

# Metodo pop()
motos = ['honda', 'yamaha', 'suzuki']
print(motos)
popped_motos = motos.pop()
print(motos)
print(popped_motos)


print()
print()


motos = ['honda', 'yamaha', 'suzuki']
last_owned = motos.pop()
print('The last motorcycle i owned was a '+last_owned.title()+'.')

print()
print()

motos = ['honda', 'yamaha', 'suzuki']
first_owned = motos.pop(0)
print('The first motorcycle i owned was a '+first_owned.title()+'.')

print()
print()

# Removendo item de acordo com o valor
motos = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motos)

motos.remove('ducatti')
print(motos)


print()
print()


motos = ['honda', 'yamaha', 'suzuki', 'ducatti']
mais_caro = 'ducatti'

motos.remove(mais_caro)
print(motos)
print("\nA "+ mais_caro.title() + " is too expensive for me")


print()
print()


# Organizando uma lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

# Revertendo a ordem de organizacao
cars.sort(reverse=True)
print(cars)


print()
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))


print()
print()


# Lista em ordem inversa
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# Tamanho da lista
print(len(cars))