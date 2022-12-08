# Questão 2

while True:

    # Recebe os valores

    V1 = float(int(input('Digite o valor da tensão primária (RMS): ')))
    alfa = float(int(input('Digite o valor da relação de trasnformação (Alfa): ')))
    f = float(input('Digite o valor da frequência (Hz): '))
    C = float(input('Digite o valor da capacitância (µF): '))
    R = float(input('Digite o valor da resistência (Ω): '))

    # Entrega os valores para o retificador de meia onda

    v2p_meia = (V1 / alfa) ** 0.5
    Icc_meia = (v2p_meia - 0.7) / R
    vrpp_meia = Icc_meia / (f * (C * 10 ** -6))
    vcc_meia = v2p_meia - (vrpp_meia / 2)
    PIV_meia = 2 * v2p_meia
    vmin_meia = (v2p_meia - 0.7) - vrpp_meia

    # Meia onda

    print()
    print(f'Para o retificador de meia onda com filtro: Vcc = {vcc_meia:.2f}V, Vrpp = {vrpp_meia:.2f}V, '
          f'PIV = {PIV_meia:.2f}V e Vmin = {vmin_meia:.2f}V')
    if vrpp_meia > 0.1 * (v2p_meia - 0.7):
        C_novo_meia = Icc_meia / ((0.1 * (v2p_meia - 0.7)) * f * 10 ** -6)
        print(f'Vrpp não está adequado, logo, um novo capacitor de {C_novo_meia:.1f}µF deve ser colocado no lugar do '
              f'antigo.')
    else:
        print('Vrpp está adequado!')

    # Entrega os valores para o TAP central

    v2p_tap = ((V1 / alfa) / 2) ** 0.5
    Icc_tap = (v2p_tap - 0.7) / R
    vrpp_tap = Icc_tap / (2 * f * (C * 10 ** -6))
    vcc_tap = vrpp_tap / 2
    PIV_tap = v2p_tap
    vmin_tap = (v2p_tap - 0.7) - vrpp_tap

    # TAP central

    print()
    print(f'Para o retificador de meia onda com filtro: Vcc = {vcc_tap:.2f}V, Vrpp = {vrpp_tap:.2f}V, '
          f'PIV = {PIV_tap:.2f}V e Vmin = {vmin_tap:.2f}V')
    if vrpp_tap > 0.1 * (v2p_tap - 0.7):
        C_novo_tap = Icc_tap / ((0.1 * (v2p_tap - 0.7)) * 2 * f * 10 ** -6)
        print(f'Vrpp não está adequado, logo, um novo capacitor de {C_novo_tap:.1f}µF deve ser colocado no lugar do '
              f'antigo.')
    else:
        print('Vrpp está adequado!')

    # Entrega os valores para o Ponte

    v2p_ponte = ((V1 / alfa) / 2) ** 0.5
    Icc_ponte = (v2p_tap - 1.4) / R
    vrpp_ponte = Icc_tap / (2 * f * (C * 10 ** -6))
    vcc_ponte = vrpp_tap / 2
    PIV_ponte = 2 * v2p_tap
    vmin_ponte = (v2p_tap - 0.7) - vrpp_tap

    # Em ponte

    print()
    print(f'Para o retificador em ponte com filtro: Vcc = {vcc_ponte:.2f}V, Vrpp = {vrpp_ponte:.2f}V, '
          f'PIV = {PIV_ponte:.2f}V e Vmin = {vmin_ponte:.2f}V')
    if vrpp_ponte > 0.1 * (v2p_ponte - 0.7):
        C_novo_ponte = Icc_ponte / ((0.1 * (v2p_ponte - 0.7)) * 2 * f * 10 ** -6)
        print(f'Vrpp não está adequado, logo, um novo capacitor de {C_novo_ponte:.1f}µF deve ser colocado no lugar do '
              f'antigo.')
    else:
        print('Vrpp está adequado!')

    p = str(input('Quer repetir o processo? [S/N] '))

    if p not in 'Ss':
        break
