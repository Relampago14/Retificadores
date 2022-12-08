# Questão 1

while True:

    # Recebe os valores e o tipo de retificador

    Icc = float(input('Digite o valor de Icc (mA): '))
    C = float(input('Digite o valor da capacitância (µF): '))
    f = float(input('Digite o valor da frequência (Hz): '))
    while True:
        tipo = str(input('O retificador é de meia onda ou de onda completa? ')).upper()
        tipo = tipo.replace(' ', '')
        if tipo in 'MEIAONDA':
            vrpp = (Icc * 10 ** -3) / (f * (C * 10 ** -6))
            print(f'A tensão de Ripple no retificador de meia onda é {vrpp:.2f}V')
        elif tipo in 'ONDACOMPLETA':
            while True:
                config = str(input('Ele é um retificador de TAP central ou em ponte? ')).upper()
                config = config.replace(' ', '')
                if config in 'TAPCENTRALCENTER':
                    vrpp = (Icc * 10 ** -3) / ((2 * f) * (C * 10 ** -6))
                    print(f'A tensão de Ripple no retificador de onda completa com derivação no TAP central é {vrpp:.2f}V')
                    break
                elif config in 'EMPONTE':
                    vrpp = (Icc * 10 ** -3) / ((2 * f) * (C * 10 ** -6))
                    print(f'A tensão de Ripple no retificador de onda completa em ponte é {vrpp:.2f}V')
                    break
                else:
                    print('Por favor, digite se ele é TAP CENTRAL/CENTER TAP ou se ele é EM PONTE/PONTE.')
            break
        else:
            print('Por favor, digite se ele é MEIA ONDA ou ONDA COMPLETA.')

    p = str(input('Quer continuar? [S/N] '))

    if p not in 'Ss':
        break
