import json
import os

if os.path.exists("tarefas.json"):
    with open("tarefas.json", "r") as arquivo:
        lista_tarefas = json.load(arquivo)
    print("Tarefas anteriores carregadas com sucesso!")
else:
    lista_tarefas = []

def carregar_tarefas():
    while True:
        item = input("Digite um item: ")
        lista_tarefas.append(item)
        continuar = input("Deseja adicionar mais itens? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nItens adicionados:")
    for i, item in enumerate(lista_tarefas, start=1):
        print(f"{i}. {item}")

    return lista_tarefas

tasks = carregar_tarefas()

with open("tarefas.json", "w") as arquivo:
    json.dump(tasks, arquivo, indent=4, ensure_ascii=False)

print("\nTarefas salvas em 'tarefas.json'.")
