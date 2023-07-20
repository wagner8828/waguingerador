import sys
import traceback

def excepthook(exc_type, exc_value, exc_traceback):
    print("Ocorreu um erro:")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    input("Pressione Enter para sair...")

sys.excepthook = excepthook

import random
import string

def gerar_email(tamanho=2):
    caracteres = string.ascii_letters + string.digits
    email = ''.join(random.choice(caracteres) for _ in range(tamanho)) + "@outlook.com"
    return email

# Examplo de uso:
email_gerado = gerar_email()
print("E-mail gerado:", email_gerado)



import sys
import traceback
import time

def excepthook(exc_type, exc_value, exc_traceback):
    print("Ocorreu um erro:")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    (5)  # Adiciona um atraso de 5 segundos antes de sair
    (1)    # Encerra o programa com um código de erro (1)

sys.excepthook = excepthook

import random
import string

def gerar_email(tamanho=2):
    caracteres = string.ascii_letters + string.digits
    email = ''.join(random.choice(caracteres) for _ in range(tamanho)) + "@outlook.com"
    return email

# Exemplo de uso:
email_gerado = gerar_email()
print("E-mail gerado:", email_gerado)

# Remova a linha de input("Pressione Enter para sair...")

import sys
import traceback

def excepthook(exc_type, exc_value, exc_traceback):
    print("Ocorreu um erro:")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    with open("gerador_waguin_error.log", "w") as f:
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)

sys.excepthook = excepthook

import random
import string

def gerar_email(tamanho=2):
    caracteres = string.ascii_letters + string.digits
    email = ''.join(random.choice(caracteres) for _ in range(tamanho)) + "@outlook.com"
    return email

# Exemplo de uso:
email_gerado = gerar_email()
print("E-mail gerado:", email_gerado)

# Pausa para permitir que você veja a saída antes de fechar a janela
input("Pressione Enter para sair...")