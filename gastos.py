import json
import os


arquivo = os.path.join(os.path.dirname(__file__), 'despesas.json')

def carregar_despesas():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo,'r') as f:
        return json.load(f)
    
def adicionar_despesa(gasto,valor):
    despesas = carregar_despesas()

    despesas.append({'gasto': gasto, 'valor': valor})

    with open(arquivo,'w') as f:
        json.dump(despesas, f,indent=4, ensure_ascii=False)
    print("💲 DESPESA ADICIONADA COM SUCESSO!")

def listar_despesa():
    despesas = carregar_despesas()

    if despesas:
        print("=" *50)
        print("LISTA DE DESPESAS:")
        print("-" *50)
        for despesa in despesas:
            print("*" *50)
            print(f"DESPESA: {despesa['gasto']}, VALOR: {despesa['valor']}")
            print("*" *50)
            print("=" *50)
    else:
        print("💲Despesa não reconhecida!")
        
