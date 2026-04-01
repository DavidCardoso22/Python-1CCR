 # Logica E (and)
 # é a logica do login
 # email e a senha sejam true

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

# Logica OU (or)
# Sol no Dom Jogo Br   Churras no Dom.
# False       True     True

logica_ou = False or False or False
print(logica_ou)

negacao = not True
print(negacao)

if not verifica_login:
    print("acerta ai...")