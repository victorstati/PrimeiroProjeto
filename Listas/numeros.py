# Funcao range() gera numeros, porem o ultimo numero nao eh incluso

for value in range(1, 6):
    print(value)


print()
print()


numbers = list(range(1, 6))
print(numbers)


print()
print()


print('Pulando numeros de 2 em 2')
even_numbers = list(range(2, 11, 2))
print(even_numbers)


print()
print()

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)


print()
print()


print("Estatistica simples")

digits = [1,2,3,4,5,6,7,8,9,0]
print("Minimo")
print(min(digits))

print("Maximo")
print(max(digits))

print("Soma")
print(sum(digits))


print()
print()


print("List comprehensions")
squares = [value**2 for value in range(1,11)]
print(squares)