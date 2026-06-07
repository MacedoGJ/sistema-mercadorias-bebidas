# Sistema de Mercadorias de Bebidas

lista_bebidas = []

def adicionar_bebida():
    nome = input("Nome da bebida: ")
    categoria = input("Categoria (ex: cerveja, refrigerante): ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade inicial: "))
    fornecedor = input("Fornecedor: ")

    lista_bebidas.append({
        "produto": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
        "fornecedor": fornecedor
    })
    print(f"{nome} adicionada com sucesso!\n")

def listar_bebidas():
    print("\n--- ESTOQUE DE BEBIDAS ---")
    if not lista_bebidas:
        print("Nenhuma bebida cadastrada.")
    else:
        for i, bebida in enumerate(lista_bebidas, start=1):
            print(f"{i} - {bebida['produto']} | Categoria: {bebida['categoria']} | "
                  f"Preço: R${bebida['preco']} | Estoque: {bebida['quantidade']} | "
                  f"Fornecedor: {bebida['fornecedor']}")
    print()

def movimentar_bebida():
    listar_bebidas()
    if not lista_bebidas:
        return
    escolha = int(input("Escolha a bebida pelo número: "))
    tipo = input("Entrada ou Saída? ").lower()
    qtd = int(input("Quantidade: "))

    if tipo == "entrada":
        lista_bebidas[escolha-1]["quantidade"] += qtd
    elif tipo == "saida":
        if lista_bebidas[escolha-1]["quantidade"] >= qtd:
            lista_bebidas[escolha-1]["quantidade"] -= qtd
        else:
            print("Estoque insuficiente!")
    print("Movimentação registrada com sucesso!\n")

def relatorio_estoque():
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    for bebida in lista_bebidas:
        status = "⚠️ Estoque baixo" if bebida["quantidade"] < 10 else "OK"
        print(f"{bebida['produto']} | Estoque: {bebida['quantidade']} | {status}")
    print()

# Menu principal
while True:
    print("""
1 - Adicionar Bebida
2 - Listar Bebidas
3 - Movimentar Estoque
4 - Relatório de Estoque
5 - Sair
    """)
    escolha = int(input("Digite: "))

    if escolha == 1:
        adicionar_bebida()
    elif escolha == 2:
        listar_bebidas()
    elif escolha == 3:
        movimentar_bebida()
    elif escolha == 4:
        relatorio_estoque()
    elif escolha == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!\n")
