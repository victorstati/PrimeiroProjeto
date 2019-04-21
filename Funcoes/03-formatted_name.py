def get_formatted_name(f_name, l_name, middle_name = ''):
    """Devolve um nome completo formatado de forma elegante """

    if middle_name:
        full_name = f_name + ' ' + middle_name + ' ' + l_name
        return full_name.title()
    else:
        full_name = f_name + ' ' + l_name
        return full_name.title()

musician = get_formatted_name('Alan', 'Walker')
print(musician)

musician = get_formatted_name('jimmi', 'hendrix', 'lee')
print(musician)