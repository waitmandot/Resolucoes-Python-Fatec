# Escreva um programa que cadastre o estado civil 
# de uma pessoa, entretanto, o programa deve continuar
# perguntando enquanto o valor informado for diferente 
# de "solteiro" ou "casado".

while True:
    estado_civil = input('solteiro\ncasado\nDigite seu estado civil: ')
    estado_civil.lower()
    if estado_civil == 'solteiro' or estado_civil == 'casado':
        break