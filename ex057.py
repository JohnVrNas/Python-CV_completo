per = ''
print('Peças de roupas íntimas na seção ao lado')
while per != 'M' and per != 'F':
    print('[M] = Masculino \n[F] = Feminino')
    per = str(input('Qual das opções você deseja? ')).strip().upper()
    if per != 'F' and per != 'M':
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE...')
if per == 'F':
    print('Ok! Irei te acompanhar até a seção feminina')
else:
    print('Ok! Irei te acompanhar até a seção masculina')
