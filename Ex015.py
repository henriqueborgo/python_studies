'====Ex015===='

km=float(input('Quantos km você rodou com o carro? '))
d=int(input('Quantos dias vocês ficou com o carro? '))

ckm=0.15*km
cd=60*d
ct=ckm+cd

print('O aluguel deste carro irá custar R$ {:.2f} '.format(ct))