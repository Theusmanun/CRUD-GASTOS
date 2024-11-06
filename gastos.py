import json
import os
from time import sleep
class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

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
    print("💲 DESPESA ADICIONADA COM SUCESSO!💲")

def listar_despesa():
    despesas = carregar_despesas()

    if despesas:
        total = 0
        print("=" *50)
        print("LISTA DE DESPESAS:")
        print("-" *50)
        for despesa in despesas:
            print("*" *50)
            print(f"DESPESA: {despesa['gasto']}, VALOR: R${despesa['valor']}")
            print("*" *50)
            print("=" *50)
            total += float(despesa['valor'])
            
           
    else:
        print("💲DESPESA NÃO ENCONTRADA!💲")
    
    print(f"\n💲 TOTAL DE DESPESAS: R$ {total:.2f}")
        
def atualizar_despesa(gasto_antigo, novo_gasto, novo_valor):
    despesas = carregar_despesas()

    for despesa in despesas:
        if despesa ['gasto'] == gasto_antigo:
            despesa['gasto'] = novo_gasto
            despesa['valor'] = novo_valor
    with open(arquivo,'w') as f:
        json.dump(despesas, f, indent=4,ensure_ascii=False)
    print("💲DESPESA ATUALIZADA COM SUCESSO!💲")

def excluir_despesa(gasto):
    despesas = carregar_despesas()
    for despesa in despesas:
        if despesa['gasto']== gasto:
            despesas.remove(despesa)
    with open(arquivo, 'w') as f:
        json.dump(despesa, f, indent=4, ensure_ascii=False)
    print("💲DESPESA EXCLUIDA COM SUCESSO!💲")

def buscar_despesa(gasto):
    despesas = carregar_despesas()

    encontrado = False

    for despesa in despesas:
        if despesa['gasto'] == gasto:
            print(F"Despesa: {despesa['gasto']}, Valor: {despesa['valor']}")
            encontrado = True
    if not encontrado:
        print("💲DESPESA NÃO ENCONTRADA.💲")

def linha_horizontal(cor):
    return cor + "=" * 50 + cor ['RESET']

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO ECOFIN <<<---- ")
    print("          1 - DESPESAS ")
    print("          2 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)

def exibir_menu():

    print("\nMENU:")
    print("1. ADICIONAR DESPESA")
    print("2. LISTAR DESPESAS")
    print("3. ATUALIZAR DESPESAS")
    print("4. EXCLUIR DESPESAS")
    print("5. LISTAR UMA DESPESA")
    print("6. VOLTAR AO MENU ANTERIOR")



def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO!"))

        match (opcao_inicial):
            
            case 1:
                while True:
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME DA DESPESA:\n>>>")
                        idade = input(" DIGITE O VALOR:\n>>>")
                        adicionar_despesa(nome, idade)
                    elif opcao == "2":
                        listar_despesa()
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME DA DESPESA A SER ATUALIZADA:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_idade = input("DIGITE O NOVO VALOR:\n>>>")
                        atualizar_despesa(nome_antigo, novo_nome, nova_idade)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DA DESPESA A SER EXCLUÍDA:\n>>>")
                        excluir_despesa(nome)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME DA DESPESA:\n>>>")
                        buscar_despesa(nome)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()