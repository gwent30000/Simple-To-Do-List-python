import os
import sys
import json

lista_tarefas = []

def carregar_tarefas():
    while True:
        itens = input("Digite um item: ")
        lista_tarefas.append(itens)
        continuar = input("Deseja adicionar mais itens? (s/n): ").lower()
        if continuar.lower() != 's':
            break

        print("\nItens adicionados:")
        for i, item in enumerate(lista_tarefas, start=1):
            print(f"{i}. {item}")

tasks = carregar_tarefas()
print(tasks)