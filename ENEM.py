math = float(input('\033[1;31mDigite sua nota em Matemática:\033[m '))
hum = float(input('\033[1;37mDigite sua nota em Humanas:\033[m '))
cod = float(input('\033[1;35mDigite sua nota em Linguagens e Códigos:\033[m '))
bio = float(input('\033[1;32mDigite sua nota em Biológicas:\033[m '))
red = float(input('\033[7;97mDigite sua nota da Redação:\033[m '))
med = (math+hum+cod+bio+red)/5
import time
import emoji
time.sleep(1.5)
print('Calculando a média...')
time.sleep(1.5)
if med >= 680:
    print(f'Sua média no ENEM foi {med:.1f}\033[1;32m\033[m') 
    print(emoji.emojize('Sua nota foi excelente! Meus parabéns!:clapping_hands:'))
else:
    print('Sua média no ENEM foi \033[1;31m{}\033[m'.format(med))
    print(emoji.emojize("""Sua média foi um pouco baixa :crying_cat:. 
Mas no ano que vem tenho certeza que você vai se sair melhor!!"""))













