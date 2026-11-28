
# SIGA-PYTHON - Sistema Integrado de Gestão Acadêmica
# Desafio 2 - Etapa 2
# Nome: Amanda Beckert Suzuki
# RA: 02610872
# O código busca complementar a etapa 1, permitindo que haja a alteração de dados previamente informados
# pelo usuário no código.


# Lista principal: cada posição armazena os dados de um aluno.
estudantes = []


# Declaração da função: EXIBIR MENU
def exibir_menu():
    print("\n" + "=" * 46)
    print("                 SIGA-PYTHON")
    print("          SISTEMA DE GESTÃO ACADÊMICA")
    print("=" * 46)
    print("1  - Cadastrar estudante")
    print("2  - Listar estudantes")
    print("3  - Registrar notas")
    print("4  - Consultar desempenho individual")
    print("5  - Consultar resumo da turma")
    print("6  - Alterar cadastro")
    print("7  - Excluir estudante")
    print("8  - Visualizar matriz de notas")
    print("9  - Consultar análise estatística")
    print("10 - Consultar ranking acadêmico")
    print("11 - Realizar busca recursiva")
    print("12 - Consultar média por recursividade")
    print("13 - Gerar relatório consolidado")
    print("0  - Encerrar aplicação")
    print("=" * 46)


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

    if matricula == "":
        print("O espaço da matrícula não pode ficar vazio")
        return

    # Impede que uma matrícula seja utilizada mais de uma vez.
    if buscar_estudante(matricula) is not None:
        print("Ops! Já existe um estudante com essa matrícula!")
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
            print("Digite uma idade utilizando números inteiros")

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
    # Envia o cadastro do aluno para o final da lista.

    print(f"\nEstudante {nome} cadastrado com sucesso!")


# Declaração da função: LISTAR ESTUDANTES
def listar_estudantes():
    print("\n ESTUDANTES CADASTRADOS ")

    if len(estudantes) == 0:
        print("Ainda não existem estudantes cadastrados")
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
        confirmacao = input("Deseja atualizar as três notas? (Sim/Não): ").strip().upper()

        if confirmacao != "Sim":
            print("Atualização cancelada")
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

    print(f"Média Final: {media:.2f}")
    print(f"Situação: {situacao}")
    print("=" * 42)


# Declaração da função: RESUMO GERAL DA TURMA
def resumo_turma():
    print("\n RESUMO GERAL DA TURMA ")

    turma_consultada = input("Informe o nome da turma: ").strip()

    if turma_consultada == "":
        print("É necessário informar uma turma!")
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
        print(f"Média geral: {media_geral:.2f}")
    else:
        print("Média geral: Não disponível")

    print("=" * 42)

# Declaração da função: ALTERAR CADASTRO
def alterar_cadastro():
    print("\n ALTERAÇÃO DE CADASTRO ")

    matricula = input("Informe a matrícula do estudante: ").strip()
    aluno = buscar_estudante(matricula)

    if aluno is None:
        print("Não foi encontrado nenhum estudante com essa matrícula")
        return

    print(f"\nCadastro localizado: {aluno['nome']}")
    print("A matrícula será mantida como identificador do estudante")

    novo_nome = input("Novo nome completo: ").strip()

    while novo_nome == "":
        print("O nome não pode ficar vazio")
        novo_nome = input("Novo nome completo: ").strip()

    # A idade é validada antes de atualizar o cadastro.
    while True:
        try:
            nova_idade = int(input("Nova idade: "))

            if nova_idade > 0:
                break
            else:
                print("A idade deve ser maior que zero")
        except ValueError:
            print("Digite uma idade utilizando números inteiros")

    nova_turma = input("Nova turma: ").strip()

    while nova_turma == "":
        print("A turma precisa ser informada")
        nova_turma = input("Nova turma: ").strip()

    # Somente os campos permitidos pelo enunciado são alterados.
    aluno["nome"] = novo_nome
    aluno["idade"] = nova_idade
    aluno["turma"] = nova_turma

    print("\nCadastro atualizado com sucesso!")


# Declaração da função: EXCLUIR ESTUDANTE
def excluir_estudante():
    print("\n EXCLUSÃO DE ESTUDANTE ")

    matricula = input("Informe a matrícula do estudante: ").strip()
    aluno = buscar_estudante(matricula)

    if aluno is None:
        print("Não foi encontrado nenhum estudante com essa matrícula")
        return

    print(f"\nEstudante: {aluno['nome']}")
    confirmacao = input("Confirma a exclusão? (Sim/Não): ").strip().upper()

    if confirmacao == "Sim":
        # A remoção do cadastro também elimina suas notas associadas.
        estudantes.remove(aluno)
        print("Estudante excluído com sucesso!")
    else:
        print("Exclusão cancelada")


# Declaração da função: CONSTRUIR E EXIBIR MATRIZ
def construir_matriz_notas():
    # Cada linha contém as três notas de um estudante avaliado.
    matriz = []
    matriculas = []

    for aluno in estudantes:
        if calcular_media(aluno["notas"]) is not None:
            matriz.append(aluno["notas"].copy())
            matriculas.append(aluno["matricula"])

    return matriz, matriculas


def visualizar_matriz():
    print("\n MATRIZ DE NOTAS ")

    matriz, matriculas = construir_matriz_notas()

    if len(matriz) == 0:
        print("Não existem estudantes com avaliações completas")
        return

    print("\nMatrícula       Nota 1     Nota 2     Nota 3")
    print("-" * 52)

    # A lista auxiliar mantém a identificação de cada linha da matriz.
    for i in range(len(matriz)):
        print(f"{matriculas[i]:<15}", end="")

        for j in range(3):
            print(f"{matriz[i][j]:>11.2f}", end="")

        print()

    print("-" * 52)

    # Percorre as colunas para calcular os indicadores de cada avaliação.
    for coluna in range(3):
        soma = 0
        notas_coluna = []

        for linha in range(len(matriz)):
            nota = matriz[linha][coluna]
            soma += nota
            notas_coluna.append(nota)

        media_coluna = soma / len(matriz)
        maior_nota = max(notas_coluna)
        menor_nota = min(notas_coluna)

        print(f"\nAvaliação {coluna + 1}:")
        print(f"Média: {media_coluna:.2f}")
        print(f"Maior nota: {maior_nota:.2f}")
        print(f"Menor nota: {menor_nota:.2f}")


# Declaração da função: ANÁLISE ESTATÍSTICA
def consultar_estatisticas():
    print("\n ANÁLISE ESTATÍSTICA ")

    medias = []

    # Apenas estudantes com as três notas entram nos indicadores.
    for aluno in estudantes:
        media = calcular_media(aluno["notas"])

        if media is not None:
            medias.append(media)

    quantidade = len(medias)

    if quantidade == 0:
        print("Não há estudantes avaliados para gerar os indicadores")
        return

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for media in medias:
        situacao = classificar_situacao(media)

        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    media_geral = sum(medias) / quantidade
    maior_media = max(medias)
    menor_media = min(medias)

    taxa_aprovacao = (aprovados / quantidade) * 100
    taxa_recuperacao = (recuperacao / quantidade) * 100
    taxa_reprovacao = (reprovados / quantidade) * 100
    desvio_extremos = maior_media - menor_media

    print("\n" + "=" * 46)
    print("           INDICADORES ACADÊMICOS")
    print("=" * 46)
    print(f"Estudantes avaliados: {quantidade}")
    print(f"Média geral: {media_geral:.2f}")
    print(f"Maior média: {maior_media:.2f}")
    print(f"Menor média: {menor_media:.2f}")
    print(f"Taxa de aprovação: {taxa_aprovacao:.2f}%")
    print(f"Taxa de recuperação: {taxa_recuperacao:.2f}%")
    print(f"Taxa de reprovação: {taxa_reprovacao:.2f}%")
    print(f"Desvio entre extremos: {desvio_extremos:.2f}")
    print("=" * 46)


# Declaração da função: RANKING ACADÊMICO
def consultar_ranking():
    print("\n RANKING DE DESEMPENHO ")

    avaliados = []

    for aluno in estudantes:
        media = calcular_media(aluno["notas"])

        if media is not None:
            avaliados.append(aluno)

    if len(avaliados) == 0:
        print("Não existem estudantes avaliados para montar o ranking")
        return

    # A ordenação é feita em uma nova lista, sem alterar os cadastros.
    # Primeiro considera a maior média; em caso de empate, o nome.
    ranking = sorted(
        avaliados,
        key=lambda aluno: (-calcular_media(aluno["notas"]), aluno["nome"].lower())
    )

    print("\n" + "=" * 65)
    print("                    RANKING ACADÊMICO")
    print("=" * 65)
    print(f"{'Pos.':<7}{'Matrícula':<15}{'Nome':<23}{'Média':<10}{'Situação'}")
    print("-" * 65)

    for posicao, aluno in enumerate(ranking, start=1):
        media = calcular_media(aluno["notas"])
        situacao = classificar_situacao(media)

        print(f"{posicao:<7}{aluno['matricula']:<15}"
              f"{aluno['nome']:<23}{media:<10.2f}{situacao}")

    print("=" * 65)


# Declaração da função: BUSCA RECURSIVA
def buscar_estudante_recursivo(lista, matricula, indice=0):
    # Caso-base: o índice chegou ao final da lista.
    if indice >= len(lista):
        return None

    # Caso encontre a matrícula, devolve o cadastro correspondente.
    if lista[indice]["matricula"] == matricula:
        return lista[indice]

    # Continua a busca na próxima posição da lista.
    return buscar_estudante_recursivo(lista, matricula, indice + 1)


def realizar_busca_recursiva():
    print("\n BUSCA RECURSIVA ")

    matricula = input("Informe a matrícula que deseja localizar: ").strip()

    resultado_recursivo = buscar_estudante_recursivo(estudantes, matricula)
    resultado_comum = buscar_estudante(matricula)

    if resultado_recursivo is None:
        print("A busca recursiva não encontrou essa matrícula")
    else:
        print("\nEstudante localizado pela busca recursiva:")
        print(f"Matrícula: {resultado_recursivo['matricula']}")
        print(f"Nome: {resultado_recursivo['nome']}")
        print(f"Idade: {resultado_recursivo['idade']}")
        print(f"Turma: {resultado_recursivo['turma']}")

    # Compara o resultado da busca recursiva com a busca convencional.
    if resultado_recursivo == resultado_comum:
        print("\nComparação: as duas buscas retornaram o mesmo resultado")
    else:
        print("\nComparação: os resultados das buscas foram diferentes")


# Declaração da função: SOMA RECURSIVA DAS MÉDIAS
def somar_medias_recursivo(medias):
    # Caso-base: uma lista vazia não possui valores para somar.
    if len(medias) == 0:
        return 0

    # Soma o primeiro elemento ao resultado da chamada seguinte.
    return medias[0] + somar_medias_recursivo(medias[1:])


def consultar_media_recursiva():
    print("\n MÉDIA GERAL POR RECURSIVIDADE ")

    medias = []

    for aluno in estudantes:
        media = calcular_media(aluno["notas"])

        if media is not None:
            medias.append(media)

    if len(medias) == 0:
        print("Não existem médias disponíveis para realizar o cálculo")
        return

    soma = somar_medias_recursivo(medias)
    media_geral = soma / len(medias)

    print(f"Quantidade de estudantes avaliados: {len(medias)}")
    print(f"Soma das médias: {soma:.2f}")
    print(f"Média geral calculada por recursividade: {media_geral:.2f}")


# Declaração da função: RELATÓRIO CONSOLIDADO
def gerar_relatorio_consolidado():
    print("\n RELATÓRIO CONSOLIDADO DA INSTITUIÇÃO ")

    total_estudantes = len(estudantes)
    avaliados = []
    pendentes = 0
    turmas = []

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    # Reúne os dados gerais e identifica as turmas cadastradas.
    for aluno in estudantes:
        if aluno["turma"] not in turmas:
            turmas.append(aluno["turma"])

        media = calcular_media(aluno["notas"])

        if media is None:
            pendentes += 1
        else:
            avaliados.append(aluno)
            situacao = classificar_situacao(media)

            if situacao == "Aprovado":
                aprovados += 1
            elif situacao == "Recuperação":
                recuperacao += 1
            else:
                reprovados += 1

    print("\n" + "=" * 54)
    print("             RELATÓRIO DA INSTITUIÇÃO")
    print("=" * 54)
    print(f"Quantidade de turmas cadastradas: {len(turmas)}")
    print(f"Quantidade total de estudantes: {total_estudantes}")
    print(f"Estudantes com avaliações completas: {len(avaliados)}")
    print(f"Estudantes com avaliações pendentes: {pendentes}")
    print(f"Estudantes aprovados: {aprovados}")
    print(f"Estudantes em recuperação: {recuperacao}")
    print(f"Estudantes reprovados: {reprovados}")

    if len(avaliados) == 0:
        print("\nMédia geral da instituição: Não disponível")
        print("Não há estudantes avaliados para identificar maior ou menor média")
        print("Não há turmas avaliadas para comparar o desempenho")
        print("=" * 54)
        return

    # Calcula a média geral considerando somente estudantes avaliados.
    medias = [calcular_media(aluno["notas"]) for aluno in avaliados]
    media_instituicao = sum(medias) / len(medias)

    # Ordena uma cópia para aplicar o desempate alfabético.
    avaliados_ordenados = sorted(
        avaliados,
        key=lambda aluno: (-calcular_media(aluno["notas"]), aluno["nome"].lower())
    )

    melhor_aluno = avaliados_ordenados[0]
    pior_aluno = avaliados_ordenados[-1]

    print(f"\nMédia geral da instituição: {media_instituicao:.2f}")
    print(f"Maior média: {melhor_aluno['nome']} "
          f"({calcular_media(melhor_aluno['notas']):.2f})")
    print(f"Menor média: {pior_aluno['nome']} "
          f"({calcular_media(pior_aluno['notas']):.2f})")

    # Calcula a média de cada turma que possui estudantes avaliados.
    medias_turmas = []

    for turma in turmas:
        soma_turma = 0
        quantidade_turma = 0

        for aluno in avaliados:
            if aluno["turma"] == turma:
                soma_turma += calcular_media(aluno["notas"])
                quantidade_turma += 1

        if quantidade_turma > 0:
            media_turma = soma_turma / quantidade_turma
            medias_turmas.append((turma, media_turma))

    # Maior média; em caso de empate, nome da turma em ordem alfabética.
    medias_turmas.sort(key=lambda item: (-item[1], item[0].lower()))

    turma_destaque = medias_turmas[0]

    print(f"Turma com maior média geral: {turma_destaque[0]} "
          f"({turma_destaque[1]:.2f})")
    print("=" * 54)


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

            case "6":
                alterar_cadastro()

            case "7":
                excluir_estudante()

            case "8":
                visualizar_matriz()

            case "9":
                consultar_estatisticas()

            case "10":
                consultar_ranking()

            case "11":
                realizar_busca_recursiva()

            case "12":
                consultar_media_recursiva()

            case "13":
                gerar_relatorio_consolidado()

            case "0":
                print("\nAplicação encerrada. Até a próxima!")
                break

            case _:
                print("\nOpção inválida! Escolha uma opção disponível")


# Inicia o sistema
principal()
