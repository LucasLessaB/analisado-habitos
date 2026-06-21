while True:
    print('======== Analisador de Hábitos =======')
    print('[1]. Registrar sono (horas)')
    print('[2]. Registrar água (litros)')
    print('[3]. Registrar exercício  (minutos)')
    print('[0]. Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        sono = float(input('Quantas horas você dormiu? '))
        print(f'Sono registrado: {sono}h')

    elif opcao == '2':
        agua = float(input('Quantas litros de agua você bebeu?'))
        print(f'Água registrado: {agua}L')

    elif opcao == '3':
        exercicio = float(input('Quantos minutos de exercicio você fez?'))
        print(f'Exercicio registrado: {exercicio} minutos')

    elif opcao == '0':
        print('Até logo!')
        break

    else:
        print('Opção invalida!')
    print()