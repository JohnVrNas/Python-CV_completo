import time
hour = time.strftime('H.%M',time.localtime())
if hour >= '05:00' and hour <='12:00':
    print('Tenha um Bom Dia!')
elif hour>'12:00' and hour <='17:59':
    print('Tenha uma Boa Tarde !')
else:
    print('Tenha uma Boa Noite!')
