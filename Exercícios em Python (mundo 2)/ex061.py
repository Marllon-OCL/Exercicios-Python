print('Gerador de PA')
n = int(input('digite o primeiro termo: '))
r = int(input('digite o valor da razão: '))
an = n
c = 1
print(f'os 10 primeiros termos dessa PA são: ', end= '')
while c <= 10:
    print(f'{an}', end= ' ')
    an += r
    c += 1
    