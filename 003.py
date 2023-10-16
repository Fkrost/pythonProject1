import json

try:
    with open("dados.json", "r") as arquivo:
        empresas = json.load(arquivo)
except FileNotFoundError:
    # Se o arquivo não existir, inicie com uma lista vazia de empresas
    empresas = []
try:
    with open("dados_cliente.json", "r") as arquivo:
        clientes = json.load(arquivo)
except FileNotFoundError:
    clientes = []

while True:
    print("Seja bem vindo ao MarketConnect!\nVocê é:\n(1)Empresa;\n(2)Cliente;")
    opcao = input("Opção selecionada: ")
    if opcao == "1":
        print("(1)Cadastrar\n(2)Login")
        opcao = int(input("opção selecionada: "))
        if opcao == 1:
            name_empresa = input("Nome da empresa: ")
            email_empresa = input("Digite o email: ")
            senha_empresa = input("Digite uma senha: ")
            senha_confirma = input("Confirme a senha: ")
            if senha_confirma == senha_empresa:
                empresa = {
                    "nome": name_empresa,
                    "email": email_empresa,
                    "senha": senha_empresa,
                    "itens": [],
                }

                empresas.append(empresa)
                print("Empresa Cadastrada!!")
                with open("dados.json", "w") as arquivo:
                    json.dump(empresas, arquivo)
            else:
                print("Lamento,mas senhas diferem!!")
        if opcao == 2:
            print("Digite o email da empresa")
            email = input("Email: ")
            senha = input("Senha: ")

            empresa = next(
                (p for p in empresas if p["email"] == email and p["senha"] == senha),
                None,
            )

            if empresa is not None:
                while True:
                    print(f'Seja bem-vindo\nLoja:{empresa["nome"].capitalize()}')
                    print(
                        "Deseja navegar em: \n(1)Produtos;\n(2)Departamentos;\n(3)Sair"
                    )
                    opcao = int(input("Opção selecionada: "))
                    if opcao == 1:
                        print("Deseja:\n(1)Adicionar produto;\n(2)Localizar produto;\n(3)Remover produto;\n(4)Alterar "
                              "produto;\n(5)Voltar")
                        opcao = int(input("Opção selecionada: "))
                        if opcao == 1:
                            name = input("Nome do Produto: ")
                            value = float(input("Valor do Produto: "))
                            unit = int(input("Quantas unidades desse produto: "))
                            department = input(
                                "Esse produto ira pertencer a qual departamento? "
                            )
                            novo_departamento = {
                                "name": name,
                                "valor": value,
                                "quantidade": unit,
                                "avaliações": "",
                            }
                            if department not in empresa:
                                empresa[department] = []

                            empresa[department].append(novo_departamento)
                            with open("dados.json", "w") as arquivo:
                                json.dump(empresas, arquivo)

                            item = {
                                "name": name,
                                "valor": value,
                                "quantidade": unit,
                            }
                            empresa["itens"].append(item)
                            print("Empresa Cadastrada!!")
                            with open("dados.json", "w") as arquivo:
                                json.dump(empresas, arquivo)
                            print("Item Adicionado!")
                            print(empresas)

                        if opcao == 2:

                            def buscar_item(nome_produto):
                                itens_encontrados: list[str] = []

                                for item in empresa["itens"]:
                                    if nome_produto.lower() in item["name"].lower():
                                        itens_encontrados.append(item)

                                return itens_encontrados


                            print("Qual nome do item que deseja localizar?")
                            name = input("Produto: ")
                            itens_encontrados = buscar_item(name)
                            if not itens_encontrados:
                                print("Item não localizado!")
                            else:
                                print("Produtos localizados:")
                                for item in itens_encontrados:
                                    print(
                                        f'Nome: {item["name"].capitalize()}\n'
                                        f'Valor: {item["valor"]}\n'
                                        f'Estoque: {item["quantidade"]}\n'
                                    )

                        if opcao == 3:
                            def buscar_item(nome_produto):
                                itens_encontrados = []

                                for item in empresa["itens"]:
                                    if nome_produto.lower() in item["name"].lower():
                                        itens_encontrados.append(item)

                                return itens_encontrados


                            print("Qual item deseja remover?")
                            name = input("Produto: ")
                            itens_encontrados = buscar_item(name)
                            if not itens_encontrados:
                                print("Item não localizado")

                            else:
                                for item in itens_encontrados:
                                    print(f'Produto localizado: {item["name"].capitalize()}')
                                print()
                                print("Cofirma remoção?\n(1)Sim;\n(2)Não;")
                                opcao = int(input("Confirma?"))
                                if opcao == 1:
                                    for item in itens_encontrados:
                                        empresa["itens"].remove(item)
                                    print("Item Removido!")
                                    with open("dados.json", "w") as arquivo:
                                        json.dump(empresas, arquivo)

                                if opcao == 2:
                                    print("Remoção Cancelada!!")

                        if opcao == 4:
                            def buscar_item(nome_produto):
                                itens_encontrados = []

                                for item in empresa["itens"]:
                                    if nome_produto.lower() in item["name"].lower():
                                        itens_encontrados.append(item)

                                return itens_encontrados


                            def atualizar_quantidade(nome, nova_quantidade):
                                for departamento in empresa.values():
                                    for item in departamento:
                                        if item["name"].lower() == nome.lower():
                                            item["quantidade"] = nova_quantidade



                            print("Qual produto deseja alterar?")
                            name = input("Produto:")
                            itens_encontrados = buscar_item(name)
                            if not itens_encontrados:
                                print("Produto não localizado")
                            else:
                                print("Produtos localizados:")
                                for item in itens_encontrados:
                                    print(item["name"].capitalize())
                                print(
                                    "Deseja alterar:\n(1)Nome;\n(2)Valor;\n(3)Estoque:\n(4)Voltar"
                                )
                                opcao = int(input("Opção selecionada:"))
                                if opcao == 1:
                                    print("Deseja alterar por?")
                                    newName = input("Novo nome: ")
                                    print(f"Confirma novo nome?\n(1)Sim;\n(2)Não;")
                                    opcao_confirmacao = int(input("Confirma? "))
                                    if opcao_confirmacao == 1:
                                        for item in itens_encontrados:  # Adicionado loop para alterar todos os itens encontrados
                                            item["name"] = newName
                                        print("Nome do produto alterado!")
                                        # Atualizar também nos departamentos
                                        atualizar_quantidade(name, newName)

                                    if opcao_confirmacao == 2:
                                        print("Alteração cancelada")

                                if opcao == 2:
                                    print("Deseja alterar por?")
                                    newValor = float(input("Novo Valor :"))
                                    print(f"Confirma novo valor?\n(1)Sim;\n(2)Não;")
                                    opcao_confirmacao = int(input("Confirma?"))
                                    if opcao_confirmacao == 1:
                                        for item in itens_encontrados:  # Adicionado loop para alterar todos os itens encontrados
                                            item["valor"] = newValor
                                        with open("dados.json", "w") as arquivo:
                                            json.dump(empresas, arquivo)
                                        print("Valor do produto alterado")
                                        # Atualizar também nos departamentos
                                        atualizar_quantidade(name, newValor)
                                    if opcao_confirmacao == 2:
                                        print("Alteração cancelada")

                                if opcao == 3:
                                    print("Deseja alterar por?")
                                    newEstoque = input("Novo estoque: ")
                                    print(f"Confirma novo estoque?\n(1)Sim;\n(2)Não;")
                                    opcao_confirmacao = int(input("Confirma? "))
                                    if opcao_confirmacao == 1:
                                        for item in itens_encontrados:  # Adicionado loop para alterar todos os itens encontrados
                                            item["quantidade"] = newEstoque
                                        with open("dados.json", "w") as arquivo:
                                            json.dump(empresas, arquivo)
                                        print("Estoque do produto alterado")

                                        # Atualizar também nos departamentos
                                        atualizar_quantidade(name, newEstoque)

                                    if opcao_confirmacao == 2:
                                        print("Alteração cancelada")

                                elif opcao == 4:
                                    print()
                        if opcao == 5:
                            print()


                    elif opcao == 2:
                        print(
                            "Deseja:\n(1)Adicionar departamento;\n(2)Remover departamento\n(3)Ver departamentos disponiveis\n(4)Voltar"
                        )
                        opcao = int(input("Opção selecionada "))
                        if opcao == 1:
                            print("Digite o nome do departamento")
                            new_namedp = input("Novo departamento:")
                            print("Confirma novo departamento?\n(1)Sim;\n(2)não")
                            opcao_confirmacao = input("Confirma?")

                            if opcao_confirmacao == 1:
                                namedp = {}
                                namedp[""] = ""
                            empresa[new_namedp] = []
                            with open("dados.json", "w") as arquivo:
                                json.dump(empresas, arquivo)
                            print("Departamento adicionado!")

                            if opcao_confirmacao == 2:
                                print("Operação cancelada")
                        if opcao == 2:
                            print("Qual departamento deseja remover?")
                            departamento_remover = input("Departamento:")
                            if departamento_remover in empresa:
                                empresa.pop(departamento_remover)
                                with open("dados.json", "w") as arquivo:
                                    json.dump(empresa, arquivo)
                                print(
                                    f"O departamento {departamento_remover} foi removido"
                                )

                            else:
                                print(
                                    f"O departamento {departamento_remover} não foi encontrado"
                                )
                        if opcao == 3:
                            def buscar_departamento(nome_parcial):
                                dep_encontrados = []

                                for departamento, itens in empresa.items():
                                    if nome_parcial.lower() in departamento.lower():
                                        dep_encontrados.extend(itens)

                                return dep_encontrados


                            valor_pra_excluir = ["nome", "email", "senha", "itens"]
                            print("Esses são todos os departamentos:")
                            for chave in empresa:
                                if chave not in valor_pra_excluir:
                                    print(f"{chave}")

                            print("\nDeseja visualizar os produtos de algum destes departamentos?")
                            departamento_pesquisar = input("Digite o nome do departamento ou 'n' para voltar: ")

                            dep_encontrados = buscar_departamento(departamento_pesquisar)
                            if not dep_encontrados:
                                print("Nenhum departamento encontrado")
                            if departamento_pesquisar == "n":
                                print("")
                            else:
                                for item in dep_encontrados:
                                    print(f'Nome: {item["name"]}\nValor: {item["valor"]}\nUnit: {item["quantidade"]}')

                        if opcao == 4:
                            print()
                    elif opcao == 3:
                        break
            else:
                print("email ou senha invalidos")

    if opcao == "2":
        print("(1)Cadastrar\n(2)login")
        opcao = int(input("Opção selecionada: "))
        if opcao == 1:
            name_cliente = input("Digite seu nome: ")
            email_cliente = input("Digite o email: ")
            senha_cliente = input("Digite uma senha: ")
            senha_confirmacliente = input("Confirme a senha: ")

            if senha_confirmacliente == senha_cliente:
                cliente = {
                    "nome": name_cliente,
                    "email": email_cliente,
                    "senha": senha_cliente,
                    "carrinho": [],
                    "pedidos": []
                }
                clientes.append(cliente)
                print("Cliente Cadastrado!!")

                # Salvar todos os clientes no arquivo dados_cliente.json
                with open("dados_cliente.json", "w") as arquivo:
                    json.dump(clientes, arquivo)

            else:
                print("Lamento, mas as senhas diferem!!")

        if opcao == 2:
            print("Digite seu Email")
            email = input("Email: ")
            print("Digite a senha: ")
            senha = input("Senha: ")
            cliente_encontrado = next((p for p in clientes if p['email'] == email and p['senha'] == senha), None)
            if cliente_encontrado is None:
                print("Email ou senha inválidos!")
            else:
                print(f'Seja bem-vindo!!\nCliente: {cliente_encontrado["nome"]}')
                print(
                    "Deseja ver:\n(1)Ver empresar parceiras;\n(2)Ver carrinho\n(3)Acessar perfil\n(4)Sair"
                )
                opcao = int(input("Opção selecionada"))
                if opcao == 1:
                    for empresa in empresas:
                        print(empresa["nome"])
                    print("Deseja acessar alguma dessas empresa?\n(1)Sim;\n(2)Não;")
                    opcao = int(input("Opção selecionada"))
                    if opcao == 1:
                        print("Qual?")
                        acessar_empresa = input("Empresa:")

                        empresa_encontrada = next(
                            (
                                empresa
                                for empresa in empresas
                                if empresa["nome"] == acessar_empresa
                            ),
                            None,
                        )

                        if empresa_encontrada is not None:
                            print(
                                "Deseja:\n(1)Pequisar produto\n(2)Ver departamento\n"
                            )
                            opcao = int(input("Opção selecionada:"))
                        if opcao == 1:
                            def buscar_item(nome_produto):
                                itens_encontrados = []

                                for item in empresa_encontrada["itens"]:
                                    if nome_produto.lower() in item["name"].lower():
                                        itens_encontrados.append(item)

                                return itens_encontrados


                            nome = input("Digite o nome do produto")
                            itens_encontrados = buscar_item(nome)

                            if not itens_encontrados:
                                print("Produto não localizado")
                            else:
                                print("Produtos localizados:")
                                for item in itens_encontrados:
                                    print(f'Nome: {item["name"]}\n'
                                          f'Valor:{item["valor"]}'
                                          )
                                    if item["quantidade"] == 0:
                                        print("Produto indisponivel")
                                    else:
                                        print(f'Estoque: {item["quantidade"]}')
                            print("Deseja adicionar algum desses itens no carrinho?")
                            produto_adicionar = input("Digite o produto ou 'n': ")
                            itens_encontrados = buscar_item(produto_adicionar)
                            if not itens_encontrados:
                                print("Produto não encontrado")
                            else:
                                print("Deseja quantas unidade desse produto?")
                                quantidade_desejada = int(input("Informe quantidade: "))
                                for item in itens_encontrados:
                                    if quantidade_desejada > item["quantidade"]:
                                        print("Infelizmente n temos tantos produtos")
                                    else:
                                        item_carrinho = {
                                            "name": item["name"],
                                            "valor": item["valor"],
                                            "quantidade": quantidade_desejada
                                        }
                                        nova_quantidade = item["quantidade"] - quantidade_desejada
                                        item["quantidade"] = nova_quantidade
                                        cliente_encontrado['carrinho'].append(item_carrinho)
                                        print("Produto adicionado ao carrinho!")
                                        with open("dados.json", "w") as arquivo:
                                            json.dump(empresas, arquivo)
                                        with open("dados_cliente.json", "w") as arquivo:
                                            json.dump(clientes, arquivo)
                            if produto_adicionar == "n":
                                print("")
                        if opcao == 2:
                            def buscar_departamento(nome_parcial):
                                dep_encontrados = []

                                for departamento, itens in empresa_encontrada.items():
                                    if nome_parcial.lower() in departamento.lower():
                                        dep_encontrados.extend(itens)

                                return dep_encontrados


                            valor_pra_excluir = ["nome", "email", "senha", "itens"]
                            print("Esses são todos os departamentos:")
                            for chave in empresa_encontrada:
                                if chave not in valor_pra_excluir:
                                    print(f"{chave}")

                            print("\nDeseja visualizar os produtos de algum destes departamentos?")
                            departamento_pesquisar = input("Digite o nome do departamento ou 'n' para voltar: ")

                            dep_encontrados = buscar_departamento(departamento_pesquisar)
                            if not dep_encontrados:
                                print("Nenhum departamento encontrado")
                            if departamento_pesquisar == "n":
                                print("")
                            else:
                                for item in dep_encontrados:
                                    print(f'Nome: {item["name"]}\nValor: {item["valor"]}\nUnit: {item["quantidade"]}')
