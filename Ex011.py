'====Ex011===='

c=float(input('Digite o comprimento da parede (em m): '))
l=float(input('Digite a largura da parede (em m): '))

a=c*l
r=2
t=a/r

print('A área da parede é {} m²'.format(a))
print('Para pintar são necessários {} litros de tinta'.format(t))