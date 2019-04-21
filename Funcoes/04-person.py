# Devolvendo um dicionario

def build_person(f_name, l_name, age=''):
    """Devolve um dicionario com as informacoes de uma pessoa"""

    person = {'first': f_name, 'last': l_name}

    if age:
        person['age'] = age
    return person

musician = build_person('alan', 'walker')
print(musician)

musician = build_person('alan', 'walker', 33)
print(musician)