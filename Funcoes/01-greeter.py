# Exibe uma saudacao simples

def greet_user():
    print("Hello!")


greet_user()


def greet_user(username):
    print("Hello ,"+username.title()+ "!")


greet_user('Jesse')