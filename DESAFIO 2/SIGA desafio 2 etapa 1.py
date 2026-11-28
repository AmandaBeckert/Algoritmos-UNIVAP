
# SIGA-PYTHON  - Desafio 2 Etapa 1
# Nome: Amanda Beckert Suzuki                 
# RA: 02610872
# O código busca subtituir e automatizar o registro de dados dos alunos feitos de maneira manual e ampliar suas
# funcionalidades, incorporando recursos de manipulação de dados, organização modular e algoritmos

# Lista principal: cada posição armazena os dados de um aluno.
estudantes = []

# Declaração da função: EXIBIR MENU
def exibir_menu():
    print("\n" + "=" * 42)
    print("          SIGA-PYTHON")
    print("    SISTEMA DE GESTÃO ACADÊMICA")
    print("=" * 42)
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Registrar notas")
    print("4 - Consultar desempenho individual")
    print("5 - Consultar resumo da turma")
    print("0 - Encerrar aplicação")
    print("=" * 42)


# Declaração da função: BUSCAR ESTUDANTE
def buscar_estudante(matricula):
    # Percorre a lista até encontrar a matrícula informada.
    for aluno in estudantes:
        if aluno["matricula"] == matricula:
            return aluno

    return None


# Declaração da função: CADASTRAR ESTUDANTE
def cadastrar_estudante():
    print("\n CADASTRO DE ESTUDANTE ")

    matricula = input("Informe a matrícula: ").strip()

    # Impede que uma matrícula seja utilizada mais de uma vez.
    if buscar_estudante(matricula) is not None:
        print("Ops! Já existe um estudante com essa matrícula!")
        return

    if matricula == "":
        print("O espaço da matrícula não pode ficar vazio")
        return

    nome = input("Nome completo: ").strip()

    while nome == "":
        print("O espaço do nome precisa ser preenchido")
        nome = input("Nome completo: ").strip()

    # Valida a idade para aceitar somente números inteiros positivos.
    while True:
        try:
            idade = int(input("Idade: "))

            if idade > 0:
                break
            else:
                print("A idade informada deve ser maior que zero")

        except ValueError:
            print("Digite uma idade utilizando números inteiros.")

    turma = input("Nome da turma: ").strip()

    while turma == "":
        print("O espaço da turma precisa ser informado")
        turma = input("Nome da turma: ").strip()

    # As três notas começam vazias e serão preenchidas posteriormente.
    novo_aluno = {
        "matricula": matricula,
        "nome": nome,
        "idade": idade,
        "turma": turma,
        "notas": [None, None, None]
    }

    estudantes.append(novo_aluno)
    #Envia o cadastro do aluno para o final da lista

    print(f"\nEstudante {nome} cadastrado com sucesso!")


# Declaração da função: LISTAR ESTUDANTES
def listar_estudantes():
    print("\n ESTUDANTES CADASTRADOS ")

    if len(estudantes) == 0:
        print("Ainda não existem estudantes cadastrados.")
        return

    # A lista é percorrida na mesma ordem dos cadastros.
    for aluno in estudantes:
        print("-" * 42)
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Turma: {aluno['turma']}")

    print("-" * 42)


# Declaração da função: CALCULAR MÉDIA
def calcular_media(notas):
    # Não calcula a média se alguma das três avaliações estiver vazia.
    if None in notas:
        return None

    return sum(notas) / 3


# Declaração da função: CLASSIFICAR SITUAÇÃO ACADÊMICA
def classificar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


# Declaração da função: REGISTRAR OU ATUALIZAR NOTAS
def registrar_notas():
    print("\n REGISTRO DE NOTAS ")

    matricula = input("Informe a matrícula do estudante: ").strip()
    aluno = buscar_estudante(matricula)

    if aluno is None:
        print("Não foi encontrado nenhum estudante com essa matrícula")
        return

    # Caso já existam notas, o usuário precisa autorizar a alteração.
    if aluno["notas"] != [None, None, None]:
        print(f"\nO estudante {aluno['nome']} já possui notas registradas")
        confirmacao = input("Deseja atualizar as três notas? ").strip().upper()

        if confirmacao != "S":
            print("Atualização cancelada.")
            return

    novas_notas = []

    # Solicita as três avaliações e valida cada valor.
    for i in range(3):
        while True:
            try:
                valor = input(f"Digite a nota {i + 1}: ").replace(",", ".")
                nota = float(valor)

                if 0 <= nota <= 10:
                    novas_notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10")

            except ValueError:
                print("Erro no registro, favor informar um valor numérico")

    # As notas só são alteradas depois que as três forem válidas.
    aluno["notas"] = novas_notas

    print("\nNotas registradas com sucesso!")
    print(f"Média atual: {calcular_media(aluno['notas']):.1f}")


# Declaração da função: CONSULTAR DESEMPENHO INDIVIDUAL
def consultar_desempenho():
    print("\n DESEMPENHO INDIVIDUAL ")

    matricula = input("Informe a matrícula do estudante: ").strip()
    aluno = buscar_estudante(matricula)

    if aluno is None:
        print("Matrícula não encontrada")
        return

    media = calcular_media(aluno["notas"])

    if media is None:
        print("O estudante ainda não possui as três notas registradas")
        return

    situacao = classificar_situacao(media)

    print("\n" + "=" * 42)
    print("          DESEMPENHO ACADÊMICO")
    print("=" * 42)
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Estudante: {aluno['nome']}")
    print(f"Turma: {aluno['turma']}")

    for i in range(3):
        print(f"Nota {i + 1}: {aluno['notas'][i]:.1f}")

    print(f"Média Final: {media:.1f}")
    print(f"Situação: {situacao}")
    print("=" * 42)


# Declaração da função: RESUMO GERAL DA TURMA
def resumo_turma():
    print("\n RESUMO GERAL DA TURMA ")

    turma_consultada = input("Informe o nome da turma: ").strip()

    if turma_consultada == "":
        print("É necessário informar uma turma")
        return

    total = 0
    completas = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    soma_medias = 0

    # Analisa somente os estudantes pertencentes à turma informada.
    for aluno in estudantes:

        if aluno["turma"].lower() == turma_consultada.lower():
            total += 1

            media = calcular_media(aluno["notas"])

            # Alunos sem as três notas contam no total, mas não nos resultados.
            if media is not None:
                completas += 1
                soma_medias += media

                situacao = classificar_situacao(media)

                if situacao == "Aprovado":
                    aprovados += 1

                elif situacao == "Recuperação":
                    recuperacao += 1

                else:
                    reprovados += 1

    if total == 0:
        print("Não existem estudantes cadastrados nessa turma")
        return

    print("\n" + "=" * 42)
    print(f"       RESUMO DA TURMA: {turma_consultada}")
    print("=" * 42)
    print(f"Total de estudantes: {total}")
    print(f"Avaliações completas: {completas}")
    print(f"Aprovados: {aprovados}")
    print(f"Em recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")

    # Evita divisão por zero quando ninguém possui notas completas.
    if completas > 0:
        media_geral = soma_medias / completas
        print(f"Média geral: {media_geral:.1f}")
    else:
        print("Média geral: Não disponível ")

    print("=" * 42)


# Corpo do código principal
def principal():

    while True:
        exibir_menu()

        opcao = input("Informe a opção desejada: ").strip()

        # O match direciona o usuário para a operação escolhida.
        match opcao:

            case "1":
                cadastrar_estudante()

            case "2":
                listar_estudantes()

            case "3":
                registrar_notas()

            case "4":
                consultar_desempenho()

            case "5":
                resumo_turma()

            case "0":
                print("\nAplicação encerrada. Até a próxima!")
                break

            case _:
                print("\nOpção inválida! Escolha uma opção disponível.")


# Inicia o sistema.
principal()