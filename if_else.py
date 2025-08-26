

velocidade = input('Qual sua velocidade media? ')
velocidade = int(velocidade)

if velocidade > 110:
    print('Acima da Velocidade Permitida')
    print('Reduza a Velocidade')

elif velocidade <60:
    print('Favor dirigir acima de 80 km/hr')

else:
    print('Velocidade Permitida')