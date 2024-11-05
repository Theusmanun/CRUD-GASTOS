import json
import os


arquivo = os.path.join(os.path.dirname(__file__), 'despesas.json')

def carregar_despesas():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=2)
    with open(arquivo,'r') as f:
        return json.load(f)
    
def adicionar_despesa(despesa,valor):
    