import string
import random


def password_generator(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(len):
        password += random.choice(characters)

    return password


len = int(input("Ingrese la longitud de la contraseña: "))
new_password = password_generator(len)

print(f"PASSWORD: {new_password}")
