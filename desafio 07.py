from datetime import date , timedelta
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

def calcular_streak(registros , tipo):
    datas = sorted(set(
        r["data"] for r in registros if r["tipo"] == tipo
    ))
    if not datas:
        print(f"Nenhum registro de {tipo} encontrado")
        return
    streak = 1
    maior_streak = 1

    for i in range(1,len(datas)):
        data_anterior = date.fromisoformat(datas[i-1])
        data_atual = date.fromisoformat(datas[i])

        if data_atual - data_anterior == timedelta(days = 1):
            streak += 1
            maior_streak = max(maior_streak, streak)
        else:
            streak = 1

    print(f"\n Streak de {tipo}:")
    print(f"   Sequência atual: {streak} dia(s)")
    print(f"   Maior sequÊncia: {maior_streak} dia(s)")

def exportar_relatorio(registros):
    with open ("relatorio.txt" , "w" , encoding = "utf-8") as f:
        f.write("===== RELATORIO GERAL =====\n\n")
        for r in registros:
            f.write(f'{r['data']} | {r['tipo']} | {r["valor"]} | {r["unidade"]}\n')
        f.write("====== ESTATISTICAS =====\n")
        for tipo in ["sono", "agua" , "exercicio"]:
            valores = [r["valor"] for r in registros if r["tipo"] == tipo]
            if valores:
                f.write(f"\n{tipo.upper()}\n")
                f.write(f"   Media: {statistics.mean(valores):.1f}\n")
                f.write(f"   Máximo: {max(valores)}\n")
                f.write(f"   Minimo: {min(valores)}\n")
    print("Relatorio exportado para relatorio.txt!")

registros = carregar_dados()

while True:
    print('======== Analisador de Hábitos =======')
    print('[1]. Registrar sono (horas)')
    print('[2]. Registrar água (litros)')
    print('[3]. Registrar exercício  (minutos)')
    print('[4]. Ver estatisticas')
    print('[5]. Ver relatorio do dia')
    print('[6]. Ver sequência de dias')
    print('[7]. Exportar relatorio')
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

    elif opcao == '6':
        print("\n Escolha um Hábito:")
        print("[1] Sono [2] Água [3] Exercício")
        escolha = input("Escolha uma opção:")
        if escolha == '1':
            calcular_streak(registros, "sono")
        elif escolha == '2':
            calcular_streak(registros, "agua")
        elif escolha == '3':
            calcular_streak(registros, "exercicio")

    elif opcao == '7':
        exportar_relatorio(registros)

    elif opcao == '0':
        print('Até logo!')
        break

    else:
        print('Opção invalida!')
    print()