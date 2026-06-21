from datetime import date
import json
import os
import statistics

arquivo = "dados.json"

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    return []

def salvar_dados(registros):
    with open(arquivo, "w") as f:
        json.dump(registros, f , indent = 4)

def barra_progresso(valor, meta , tamanho = 20):
    preenchido = int((valor/meta) * tamanho)
    preenchido = min(preenchido, tamanho)
    barra = "█" * preenchido + "░" * (tamanho - preenchido)
    percentual = min(int((valor/meta) * 100),100)
    return f"[{barra}] {percentual}%"

def exibir_relatorio(registros):
    print("\n ========= RELATÓRIO DO DIA ==========")
    hoje = str(date.today())
    registros_hoje = [r for r in registros if r ["data"] == hoje]

    if not registros_hoje:
        print("Nenhum registro para hoje ainda.")
        return
    metas = {"sono": 8 , "agua": 2.5 , "exercicio": 30}

    for tipo, meta in metas.items():
        valores = [r["valor"] for r in registros_hoje if r["tipo"] == tipo]
        if valores:
            total = sum(valores)
            print(f"{tipo.upper()}")
            print(f" Valor:{total}")
            print(f" Meta: {meta}")
            print(f" {barra_progresso(total,meta)}")
        else:
            print(f"{tipo.upper()}")
            print(f" Sem registro hoje.")

def calcular_estatistica(registros , tipo):
    valores = [r["valor"] for r in registros if r["tipo"] == tipo]
    if not valores:
        print(f"Nenhum registro de {tipo} encontrado")
        return
    print(f"\n Estatísticas de {tipo}:")
    print(f"  Total de registros {len(valores)}")
    print(f"  Média dos registros {statistics.mean(valores)}")
    print(f"  Maior registro {max(valores)}")
    print(f"  Menor registro {min(valores)}")

registros = carregar_dados()

while True:
    print('======== Analisador de Hábitos =======')
    print('[1]. Registrar sono (horas)')
    print('[2]. Registrar água (litros)')
    print('[3]. Registrar exercício  (minutos)')
    print('[4]. Ver estatisticas')
    print('[5]. Ver relatorio do dia')
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

    elif opcao == '4':
        print("\n Escolha um hábito:")
        print("[1] Sono  [2] Água  [3] Exercício")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            calcular_estatistica(registros, "sono")
        elif escolha == "2":
            calcular_estatistica(registros, "agua")
        elif escolha == "3":
            calcular_estatistica(registros, "exercicio")

    elif opcao == '5':
        exibir_relatorio(registros)

    elif opcao == '0':
        print('Até logo!')
        break

    else:
        print('Opção invalida!')
    print()