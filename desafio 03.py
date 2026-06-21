from datetime import date
import json
import os

arquivo = "dados.json"

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    return []

def salvar_dados(registros):
    with open(arquivo, "w") as f:
        json.dump(registros, f , indent = 4)

registros = carregar_dados()

while True:
    print('======== Analisador de Hábitos =======')
    print('[1]. Registrar sono (horas)')
    print('[2]. Registrar água (litros)')
    print('[3]. Registrar exercício  (minutos)')
    print('[0]. Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        sono = float(input('Quantas horas você dormiu? '))
        registro = {
            "data": str(date.today()),
            "tipo": "sono",
            "valor": sono,
            "unidade": "horas"
        }
        registros.append(registro)
        salvar_dados(registros)
        print(f'Sono registrado: {sono}h')

    elif opcao == '2':
        agua = float(input('Quantas litros de agua você bebeu?'))
        registro = {
            "data": str(date.today()),
            "tipo": "agua",
            "valor": agua,
            "unidade": "litros"
        }
        registros.append(registro)
        salvar_dados(registros)
        print(f'Água registrado: {agua}L')

    elif opcao == '3':
        exercicio = float(input('Quantos minutos de exercicio você fez?'))
        registro = {
            "data":str(date.today()),
            "tipo": "exercicio",
            "valor": exercicio,
            "unidade": "minutos"
        }
        registros.append(registro)
        salvar_dados(registros)
        print(f'Exercicio registrado: {exercicio} minutos')

    elif opcao == '0':
        print(registros)
        print('Até logo!')
        break

    else:
        print('Opção invalida!')
    print()