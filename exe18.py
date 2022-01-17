#CÓDIGO QUE RECEBE O VALOR DO ANGULO E CALCULA SEU SENO, COSSENO E TANGENTE

import math

angulo = float(input('Digite o valor do ângulo: '))

seno = (math.sin(math.radians(angulo)))
cos = (math.cos(math.radians(angulo)))
tang = (math.tan(math.radians(angulo)))

print('O ângulo digitado foi {}.\nSeno = {}.\nCosseno = {}.\nTangente = {}.'.format(angulo,seno,cos,tang))
