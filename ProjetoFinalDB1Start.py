# Programa CARTEIRA DE CLIENTES

'''Este programa tem como finalidade gerenciar dados de clientes de uma loja.
   Ele é capaz de:
   - Cadastrar dados;
   - Consultar dados cadastrados;
   - Excluir dados cadastrados;
   - Atualizar dados cadastrados;
   - Exibir lista de clientes cadastrados;'''

# Função que retorna dados do cliente
def Lista_de_Informacoes ():
    print(f'Nome completo do Cliente: {Cliente["Nome"]}')
    print(f'CPF do Cliente: {Cliente["CPF"]}')
    print(f'Endereço do Cliente: {Cliente["Endereco"]}')
    print(f'Telefone do Cliente: {Cliente["Tel"]}')
    print()


# Declaração da lista e dicionário utilizado
Dados_Cliente = []
Cliente = {}

# Menu de opções do usuário
while True:
    print()
    print('CARTEIRA DE CLIENTES - Loja D1B Acessórios')
    print('-' * 50)
    print('1 - Cadastrar Cliente')
    print('2 - Consultar Cliente')
    print('3 - Excluir Cliente')
    print('4 - Alterar Dados Cliente')
    print('5 - Listar Clientes')
    print('6 - Sair')
    print('-' * 50)

    # Início do tratamento da opção escolhida
    escolha = int(input('Escolha uma opção: '))
    print()

    match escolha:
        # Caso 1, recebe os dados informados pelo usuário e guarda-os em dicionários. Ao final, guarda-os em lista
        case 1:
            Nome_Cliente = str(input('Digite o nome do cliente: '))
            cpf_Cliente = int(input('Digite o CPF do cliente (somente números): '))
            Endereco_Cliente = str(input('Digite o endereço do cliente: '))
            Tel_Cliente = int(input('Digite o telefone do cliente (somente números): '))
            print()

            Cliente['Nome'] = Nome_Cliente
            Cliente['CPF'] = cpf_Cliente
            Cliente['Endereco'] = Endereco_Cliente
            Cliente['Tel'] = Tel_Cliente

            print('Os dados do cliente foram salvos com sucesso!')
            print()
            Dados_Cliente.append(Cliente.copy())
            print(Dados_Cliente)
            print(len(Dados_Cliente))
            Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
            print()

            if Continuar in 'Nn':
                break

        # Caso 2, consulta os dados cadastrados (por nome ou cpf)
        case 2:
            print('1 - Consultar pelo nome')
            print('2 - Consultar pelo CPF')
            print()

            opcao = int(input('Escolha uma opção: '))
            print()

            match opcao:

                case 1:

                    Consulta_Nome = str(input('Digite o nome completo do cliente: '))
                    print()

                    for i in range(0,len(Dados_Cliente)):  # P/ todas as posições da lista, faça comparação entre dic. e dado digitado

                        if Cliente['Nome'] == Consulta_Nome:
                           Dados_Retornados = Lista_de_Informacoes()

                        else:
                            print('ERRO! Cliente não encontrado.')
                            print()

                        Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                        print()

                        if Continuar in 'Nn':
                            break

                case 2:

                    Consulta_CPF = int(input('Digite o CPF completo do cliente (somente números): '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Consulta_CPF == Cliente['CPF']:
                            Dados_Retornados = Lista_de_Informacoes()

                        else:
                            print('ERRO! Cliente não encontrado.')
                            print()

                        Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                        print()

                        if Continuar in 'Nn':
                            break

        case 3:

            # Caso 3, exclui dados gravados (por nome ou CPF)
            print('1 - Excluir cliente pelo nome')
            print('2 - Excluir cliente pelo CPF')
            print()

            opcao = int(input('Escolha uma opção: '))
            print()

            match opcao:

                case 1:
                    Excluir_Nome = str(input('Digite o nome completo do cliente: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Excluir_Nome == Cliente['Nome']:
                            Dados_Cliente.pop(i)

                            print('Cliente excluído com sucesso!!')
                            print()
                            print(Dados_Cliente)
                            print()
                        else:
                            print('ERRO!! Estes dados não existem.')

                case 2:
                    Excluir_CPF = str(input('Digite o CPF completo do cliente: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Excluir_CPF == Cliente['CPF']:
                            del Cliente[i]
                            print('Cliente excluído com sucesso!!')
                            print()
                            print(Dados_Cliente)
                            print()
                        else:
                            print('ERRO!! Estes dados não existem.')

            Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
            print()
            if Continuar in 'Nn':
                break

        case 4:
            # Caso 4, altera dados já cadastrados
            print('1 - Alterar Nome')
            print('2 - Alterar CPF')
            print('3 - Alterar Endereço')
            print('4 - Alterar Telefone')

            opcao = int(input('Escolha uma opção: '))
            print()

            match opcao:

                case 1:
                    Alterar_Nome = int(input('Digite o CPF do cliente que deseja realizar alteração: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Alterar_Nome == Cliente['CPF']:
                            print('DADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()

                            Novo_Nome = str(input('Digite o NOVO nome do cliente: '))
                            print()
                            Cliente['Nome'] = Novo_Nome
                            print('DADOS ATUALIZADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()
                            Dados_Cliente[i]['Nome'] = Novo_Nome                                # joga novo nome no dici.


                        else:
                            print('ERRO!! Dados incorretos.')

                    Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                    print()
                    if Continuar in 'Nn':
                        break

                case 2:
                    Alterar_CPF = str(input('Digite o NOME do cliente que deseja realizar alteração: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Alterar_CPF == Cliente['Nome']:
                            print('DADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()

                            Novo_CPF = int(input('Digite o NOVO CPF do cliente: '))
                            print()
                            Cliente['CPF'] = Novo_CPF
                            print('DADOS ATUALIZADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()
                            Dados_Cliente[i]['CPF'] = Novo_CPF                                   # joga novo CPF no dici.

                        else:
                            print('ERRO!! Dados incorretos.')

                    Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                    print()
                    if Continuar in 'Nn':
                        break

                case 3:
                    Alterar_Endereco = int(input('Digite o CPF do cliente que deseja realizar alteração: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Alterar_Endereco == Cliente['CPF']:
                            print('DADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()

                            Novo_Endereco = str(input('Digite o NOVO ENDEREÇO do cliente: '))
                            print()
                            Cliente['Endereco'] = Novo_Endereco
                            print('DADOS ATUALIZADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()
                            Dados_Cliente[i]['Endereco'] = Novo_Endereco                        # joga novo Endereço no dici.
                        else:
                            print('ERRO!! Dados incorretos.')

                    Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                    print()
                    if Continuar in 'Nn':
                        break

                case 4:

                    Alterar_Telefone = int(input('Digite o CPF do cliente que deseja realizar alteração: '))
                    print()

                    for i in range(0, len(Dados_Cliente)):

                        if Alterar_Telefone == Cliente['CPF']:
                            print('DADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()

                            Novo_Telefone = str(input('Digite o NOVO TELEFONE do cliente: '))
                            print()
                            Cliente['Tel'] = Novo_Telefone
                            print('DADOS ATUALIZADOS DO CLIENTE: ')
                            print()
                            Dados_Retornados = Lista_de_Informacoes()
                            Dados_Cliente[i]['Telefone'] = Novo_Telefone                            # joga novo Telefone no dici.

                        else:
                             print('ERRO!! Dados incorretos.')

                    Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
                    print()
                    if Continuar in 'Nn':
                        break

        case 5:
            # Caso 5, retorna valores específicos dos dicionários
            for i in range(0, len(Dados_Cliente)):                                                   # P/ toda posicão. da lista...

                print(Dados_Cliente[i]['Nome'])  # Acessa a lista toda, no dic [i], campo nome

            print()
            Continuar = str(input('Deseja realizar outra operação? (S/N)?'))
            print()
            if Continuar in 'Nn':
                break

        # Encerra o programa
        case 6:
            print('')
            print('ATÉ MAIS!!')
            break