from datetime import datetime, timedelta

agendamentos = []

def inicio():
    print("\n")
    print("--------CABELELEILA LEILA SALÕES DE BELEZA--------")
    print("---SELECIONE SEU PERFIL:---")
    print("1. Sou cliente")
    print("2. Sou funcionário")
    print("--------------------------------------------------")
    print("\n")
    selecionar_perfil()

def selecionar_perfil():
    global perfilSelecionado

    perfilSelecionado = input("Insira o número correspondente ao seu perfil: ")

    if perfilSelecionado == '1':
        print("\nBem-vindo(a), cliente!")
        realizar_login_usuario()
    elif perfilSelecionado == '2':
        print("\nBem-vindo(a), colaborador!")
        realizar_login_Funcionario()
        menu_funcionario()
    else:
        print("\nPerfil inválido! Por favor, escolha entre 1 para cliente e 2 para funcionário.")
        selecionar_perfil()

def realizar_login_usuario():
    global loginUsuario

    print("\nLembre-se que seu login é seu primeiro nome + 4 últimos dígitos do celular. (Exemplo: leila4693)")

    loginUsuario = input("Insira seu login: ")

    while loginUsuario != 'leila4693':
        print("\nUsuário incorreto! Lembre-se que seu login é seu primeiro nome + 4 últimos dígitos do celular. (Exemplo: leila4693)")
        print("Caso não consiga logar, entre em contato com o salão.")
        loginUsuario = input("Insira seu login: ")

    print("\nLogin realizado com sucesso!\n")
    menu_cliente()
    
def realizar_login_Funcionario():

    global loginFuncionario

    print("\nLembre-se que seu login é seu primeiro nome + 4 últimos dígitos do celular. (Exemplo: leilaleilinha1234)")

    loginFuncionario = input("Insira seu login: ")

    while loginFuncionario != 'leilaleilinha1234':
        print("\nUsuário incorreto! Lembre-se que seu login é seu primeiro nome + 4 últimos dígitos do celular. (Exemplo: leilaleilinha1234)")
        print("Caso não consiga logar, entre em contato com o salão.")
        loginFuncionario = input("Insira seu login: ")

def menu_funcionario():
    while True:
        print("Menu Funcionário: \n") 
        opcoes = ["1 - Alterar Agendamento", "2 - Listar Agendamentos", "3 - Acompanhamento Semanal", "4 - Sair"]
        for opcao in opcoes:
            print(opcao)
        print("\n")    
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            alterar_agendamento_funcionario()
        elif escolha == "2":
            gerir_agendamentos()
        elif escolha == "3": 
            acompanhamento_semanal()
        elif escolha == "4":
            print("\n Cabeleila Leila agradece a preferência!.")
            break
        else:
            print("\nOpção inválida.\n")

def gerir_agendamentos():
    print(agendamentos)
    
    
def alterar_agendamento_funcionario():
    global agendamentos

    print("\nReagendar agendamento:")
    
    if not agendamentos:
        print("Não há agendamentos registrados.")
        return

    print("Agendamentos disponíveis para reagendamento:")
    for i, agendamento in enumerate(agendamentos, 1):
        horario = agendamento.get('horario', 'Horário não informado')
        print(f"{i}. Nome do cliente: {agendamento['nome_cliente']}, Serviços: {', '.join(agendamento['servicos'])}, Data: {agendamento['data']}, Horário: {horario}")

    agendamento_escolhido = None
    while agendamento_escolhido is None:
        escolha = input("Escolha o número do agendamento que deseja reagendar (ou digite 0 para cancelar): ")

        if escolha == '0':
            print("Cancelando reagendamento.")
            return

        opcao = int(escolha)
        if 1 <= opcao <= len(agendamentos):
            agendamento_escolhido = agendamentos[opcao - 1]
        else:
            print("Opção inválida.")

    data_agendamento_str = agendamento_escolhido['data']
    data_agendamento = datetime.strptime(data_agendamento_str, '%d/%m/%Y')
    data_atual = datetime.now()
    diferenca_dias = (data_agendamento - data_atual).days

    if diferenca_dias < 2:
        print("Não é possível reagendar este agendamento. O prazo máximo é de 2 dias antes do atendimento.")
        return

    nova_data = input("Insira a nova data (dd/mm/aaaa): ")
    novo_horario = input("Insira o novo horário (hh:mm): ")

    agendamento_escolhido['data'] = nova_data
    agendamento_escolhido['horario'] = novo_horario

    print("Agendamento reagendado com sucesso!")


def menu_cliente():
    while True:
        print("Menu: \n") 
        opcoes = ["1 - Agendamento", "2 - Reagendamento", "3 - Visualizar agendamentos", "4 - Histórico de agendamento", "5 - Sair"]
        for opcao in opcoes:
            print(opcao)
        print("\n")    
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            agendar_servico_cliente()
        elif escolha == "2":
            reagendar_servico_cliente()
        elif escolha == "3": 
            visualizar_agendamentos()
        elif escolha == "4":
            historico_agendamentos()
        elif escolha == "5":
            print("\nCabeleila Leila agradece a preferência!.")
            break
        else:
            print("\nOpção inválida. Escolha novamente.\n")

def agendar_servico_cliente():
    global agendamentos

    print("\nAgendar serviço:")
    
    nome_cliente = input("Insira seu nome: ")
    servicos = ["Corte de Cabelo", "Manicure", "Pedicure", "Cílios", "Maquiagem"]
    
    print("\nEscolha o(s) serviço(s) que deseja agendar (separados por vírgula):")
    for i, servico in enumerate(servicos, 1):
        print(f"{i}. {servico}")
    
    servicos_escolhidos = input("Serviços: ").split(',')

    for i in range(len(servicos_escolhidos)):
        servicos_escolhidos[i] = servicos[int(servicos_escolhidos[i]) - 1]

    data_agendamento = input("Insira a data do agendamento (dd/mm/aaaa): ")
    hora_agendamento = input("Insira a hora do agendamento hh:mm: ")
    
    
    novo_agendamento = {
        'nome_cliente': nome_cliente,
        'servicos': servicos_escolhidos,
        'data': data_agendamento
    }
    
    agendamentos.append(novo_agendamento)
    
    print("\nAgendamento realizado com sucesso!\n")

def reagendar_servico_cliente():
    global agendamentos

    print("\nReagendar serviço:")

    if not agendamentos:
        print("Você ainda não possui nenhum agendamento.")
        return

    print("Seus agendamentos:")
    for i, agendamento in enumerate(agendamentos, 1):
        print(f"{i}. Nome do cliente: {agendamento['nome_cliente']}, Serviços: {', '.join(agendamento['servicos'])}, Data: {agendamento['data']}")

    agendamento_escolhido = None
    while agendamento_escolhido is None:
        escolha = input("Escolha o número do agendamento que deseja reagendar (ou digite 0 para cancelar): ")

        if escolha == '0':
            print("Cancelando reagendamento.")
            return

        opcao = int(escolha)
        if 1 <= opcao <= len(agendamentos):
            agendamento_escolhido = agendamentos[opcao - 1]
        else:
            print("Opção inválida. Por favor, escolha um agendamento válido.")

    nova_data = input("Insira a nova data (dd/mm/aaaa): ")
    novo_horario = input("Insira o novo horário (hh:mm): ")

    agendamento_escolhido['data'] = nova_data
    agendamento_escolhido['horario'] = novo_horario

    print("Agendamento reagendado com sucesso!")

def visualizar_agendamentos():
    print(f"\nAgendamentos de {loginUsuario}\n")
    for agendamento in agendamentos:
        horario = agendamento.get('horario', 'Horário não informado')
        print(f"Nome do cliente: {agendamento['nome_cliente']}, Serviços: {', '.join(agendamento['servicos'])}, Data: {agendamento['data']}, Horário: {horario}")

def historico_agendamentos():
    global agendamentos

    print("\nHistórico de agendamentos:")

    if not agendamentos:
        print("Você ainda não possui nenhum agendamento.")
        return

    for i, agendamento in enumerate(agendamentos, 1):
        horario = agendamento.get('horario', 'Horário não informado')
        print(f"Nome do cliente: {agendamento['nome_cliente']}, Serviços: {', '.join(agendamento['servicos'])}, Data: {agendamento['data']}, Horário: {horario}")

def acompanhamento_semanal():
    print(f"DESEMPENHO SEMANAL: ")
    print(f"Número de agendamentos: {len(agendamentos)}")
    


inicio()
