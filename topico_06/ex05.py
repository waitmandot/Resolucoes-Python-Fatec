# Pangrama, ou pantograma, (do grego, pan ou
# pantós = todos, + grama = letra) é uma frase 
# em que são usadas todas as letras do alfabeto 
# de determinada língua. A partir da definição, 
# crie um código python para definir se uma frase 
# é ou não um pangrama.
# https://pt.wikipedia.org/wiki/Pangrama

import string

alfabeto = string.ascii_lowercase

# Use como exemplo a frase:
frase = 'Jane quer LP, fax, CD, giz, TV e bom whisky'

diferenca_simetrica = set(alfabeto) - set(frase.lower())

if not diferenca_simetrica:
    print('A frase é um pantograma')
else:
    print('A frase não é um pantograma')