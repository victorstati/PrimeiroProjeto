
def describe_pet(animal_type, pet_name):
    """Exibe informacoes sobre um aninam de extimacao"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('dog', 'zeus')

describe_pet('cat', 'tama')

# Argumento nomeado
describe_pet(animal_type='fish', pet_name='bob')

