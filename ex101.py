
import os
os.system('cls')

    
def voto(nasc):
    from datetime import datetime
    ano = datetime.now().year
    global idade
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} ano: VOTO NEGADO'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} ano: VOTO OBRIGATÓRIO'
    elif idade > 65:
        return f'Com {idade} ano: VOTO OPCIONAL'




nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
