from time import sleep
import emoji
print('A contagem para a virada do ano vai começar!!')
sleep(2)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print(emoji.emojize('\033[31m:fireworks: FELIZ ANO NOVO!!:fireworks:\033[m'))
