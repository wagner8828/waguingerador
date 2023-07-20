

import random
import string

def gerar_email(tamanho=2):
    caracteres = string.ascii_letters + string.digits
    email = ''.join(random.choice(caracteres) for _ in range(tamanho)) + "@outlook.com"
    return email

# Examplo de uso:
email_gerado = gerar_email()
print("E-mail gerado:", email_gerado)