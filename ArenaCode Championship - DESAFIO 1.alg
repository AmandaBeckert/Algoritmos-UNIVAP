Algoritmo "ArenaCode Championship - Desafio 1"
//
//
// Descrição   : A proposta do desafio é criar um algoritmo que armazene os dados
// de uma competção incluindo informações das equipes, tabelas de pontuação, resultados
//utilizando de subrotinas e organização para resolver de maneira efeciente a comitiva
//da E sports championship
// Autor(a)    : Amanda Beckert Suzuki
// RA: 0261087
// Data atual  : 29/09/2026

const
//Seção de declaração das constantes
   MAX_EQUIPES = 10
   PONTOS_VITORIA = 3
   PONTOS_EMPATE = 1
   PONTOS_DERROTA = 0

tipo
//Seção de declaração do registro das equipes
   TEquipe = registro
      codigo: inteiro
      nome: caractere
      capitao: caractere
      vitorias: inteiro
      empates: inteiro
      derrotas: inteiro
      pontosMarcados: inteiro
      pontosSofridos: inteiro
      saldo: inteiro
      pontosCampeonato: inteiro
      indiceMatriz: inteiro
   fimregistro

var
//Seção de declaração das variáveis globais
   equipes: vetor[1..MAX_EQUIPES] de TEquipe
   confrontos: vetor[1..MAX_EQUIPES,1..MAX_EQUIPES] de inteiro
   totalEquipes, totalPartidas, opcao: inteiro
   calcularSaldo :inteiro

procedimento buscarEquipe(cod: inteiro; var indiceEncontrado: inteiro)
//procedimento que busca o código cadastrado da equipe para retornar sua posição

var
//Seção de declaração de variáveis locais do procedimento buscarEquipe
   i: inteiro
inicio
   indiceEncontrado <- 0
   para i de 1 ate totalEquipes faça
      se equipes[i].codigo = cod então
         indiceEncontrado <- i
         interrompa
      fimse
   fimpara
fimprocedimento

// Função: calcula e devolve o saldo de pontos de uma equipe.
funcao calcularSaldo(indiceEquipe: inteiro): inteiro
inicio
   calcularSaldo := equipes[indiceEquipe].pontosMarcados - equipes[indiceEquipe].pontosSofridos
fimfuncao

// Procedimento: atualiza o saldo usando a função calcularSaldo.
procedimento atualizarSaldo(indiceEquipe: inteiro)
inicio
equipes[indiceEquipe].saldo <- calcularSaldo(indiceEquipe)
fimprocedimento

// Procedimento: cadastra uma nova equipe e inicializa suas estatísticas.
procedimento cadastrarEquipe
var
cod, indiceEquipe: inteiro
nomeDigitado, capitaoDigitado: caractere

inicio
se totalEquipes >= MAX_EQUIPES então
escreval("Limite de equipes atingido.")
senão
escreva("Código numérico único: ")
leia(cod)
buscarEquipe(cod, indiceEquipe)

  enquanto (cod <= 0) ou (indiceEquipe <> 0) faça
     escreva("Código inválido ou duplicado. Digite outro: ")
     leia(cod)
     buscarEquipe(cod, indiceEquipe)
  fimenquanto

  escreva("Nome da equipe: ")
  leia(nomeDigitado)
  enquanto nomeDigitado = "" faça
     escreva("O nome não pode ficar vazio. Digite novamente: ")
     leia(nomeDigitado)
  fimenquanto

  escreva("Nome do capitão: ")
  leia(capitaoDigitado)
  enquanto capitaoDigitado = "" faça
     escreva("O nome não pode ficar vazio. Digite novamente: ")
     leia(capitaoDigitado)
  fimenquanto

  totalEquipes <- totalEquipes + 1
  indiceEquipe <- totalEquipes

  equipes[indiceEquipe].codigo <- cod
  equipes[indiceEquipe].nome <- nomeDigitado
  equipes[indiceEquipe].capitao <- capitaoDigitado
  equipes[indiceEquipe].vitorias <- 0
  equipes[indiceEquipe].empates <- 0
  equipes[indiceEquipe].derrotas <- 0
  equipes[indiceEquipe].pontosMarcados <- 0
  equipes[indiceEquipe].pontosSofridos <- 0
  equipes[indiceEquipe].saldo <- 0
  equipes[indiceEquipe].pontosCampeonato <- 0
  equipes[indiceEquipe].indiceMatriz <- indiceEquipe

  escreval("Equipe cadastrada com sucesso!")

fimse
fimprocedimento

procedimento listarEquipes
var
   i: inteiro
inicio
   se totalEquipes = 0 então
      escreval("Nenhuma equipe cadastrada.")
   senão
      escreval("--- EQUIPES CADASTRADAS ---")
      para i de 1 ate totalEquipes faça
         escreval("Codigo: ", equipes[i].codigo)
         escreval("Equipe: ", equipes[i].nome)
         escreval("Capitao: ", equipes[i].capitao)
         escreval("------------------------------")
      fimpara
   fimse
fimprocedimento

procedimento mostrarEquipe(indiceEquipe: inteiro)
inicio
   escreval("Código: ", equipes[indiceEquipe].codigo)
   escreval("Equipe: ", equipes[indiceEquipe].nome)
   escreval("Capitão: ", equipes[indiceEquipe].capitao)
   escreval("Vitórias: ", equipes[indiceEquipe].vitorias)
   escreval("Empates: ", equipes[indiceEquipe].empates)
   escreval("Derrotas: ", equipes[indiceEquipe].derrotas)
   escreval("Pontos marcados: ", equipes[indiceEquipe].pontosMarcados)
   escreval("Pontos sofridos: ", equipes[indiceEquipe].pontosSofridos)
   escreval("Saldo: ", equipes[indiceEquipe].saldo)
   escreval("Pontos no campeonato: ", equipes[indiceEquipe].pontosCampeonato)
fimprocedimento

procedimento consultarEquipe
var
   cod, indiceEquipe: inteiro
inicio
   escreva("Informe o código da equipe: ")
   leia(cod)
   buscarEquipe(cod, indiceEquipe)
   se indiceEquipe = 0 entao
      escreval("Equipe não localizada.")
   senao
      mostrarEquipe(indiceEquipe)
   fimse
fimprocedimento

procedimento registrarPartida
var
   cod1, cod2, pos1, pos2, pm1, pm2, m1, m2: inteiro
inicio
   se totalEquipes < 2 então
      escreval("Cadastre pelo menos duas equipes antes de registrar partidas.")
   senao
      escreva("Código da primeira equipe: ")
      leia(cod1)
      buscarEquipe(cod1, pos1)
      enquanto pos1 = 0 faça
         escreva("Equipe nao encontrada. Informe outro codigo: ")
         leia(cod1)
         buscarEquipe(cod1, pos1)
      fimenquanto

      escreva("Código da segunda equipe: ")
      leia(cod2)
      buscarEquipe(cod2, pos2)
      enquanto (pos2 = 0) ou (pos2 = pos1) faça
         se pos2 = pos1 então
            escreva("Uma equipe nao pode jogar contra ela mesma. Informe outro código: ")
         senao
            escreva("Equipe não encontrada. Informe outro código: ")
         fimse
         leia(cod2)
         buscarEquipe(cod2, pos2)
      fimenquanto

      m1 <- equipes[pos1].indiceMatriz
      m2 <- equipes[pos2].indiceMatriz
      enquanto confrontos[m1,m2] <> 0 faca
         escreval("Esse confronto ja foi registrado. Escolha outra equipe para a segunda vaga.")
         escreva("Codigo da segunda equipe: ")
         leia(cod2)
         buscarEquipe(cod2, pos2)
         enquanto (pos2 = 0) ou (pos2 = pos1) faca
            escreva("Código inválido ou igual ao da primeira equipe. Tente novamente: ")
            leia(cod2)
            buscarEquipe(cod2, pos2)
         fimenquanto
         m2 <- equipes[pos2].indiceMatriz
      fimenquanto

      escreva("Pontos da primeira equipe (zero ou mais): ")
      leia(pm1)
      enquanto pm1 < 0 faca
         escreva("A pontuação nao pode ser negativa. Digite novamente: ")
         leia(pm1)
      fimenquanto
      escreva("Pontos da segunda equipe (zero ou mais): ")
      leia(pm2)
      enquanto pm2 < 0 faca
         escreva("A pontuacao nao pode ser negativa. Digite novamente: ")
         leia(pm2)
      fimenquanto

      equipes[pos1].pontosMarcados <- equipes[pos1].pontosMarcados + pm1
      equipes[pos1].pontosSofridos <- equipes[pos1].pontosSofridos + pm2
      equipes[pos2].pontosMarcados <- equipes[pos2].pontosMarcados + pm2
      equipes[pos2].pontosSofridos <- equipes[pos2].pontosSofridos + pm1

      se pm1 > pm2 entao
         equipes[pos1].vitorias <- equipes[pos1].vitorias + 1
         equipes[pos2].derrotas <- equipes[pos2].derrotas + 1
         equipes[pos1].pontosCampeonato <- equipes[pos1].pontosCampeonato + PONTOS_VITORIA
         equipes[pos2].pontosCampeonato <- equipes[pos2].pontosCampeonato + PONTOS_DERROTA
         confrontos[m1,m2] <- 1
         confrontos[m2,m1] <- 2
      senão
         se pm2 > pm1 entao
            equipes[pos2].vitorias <- equipes[pos2].vitorias + 1
            equipes[pos1].derrotas <- equipes[pos1].derrotas + 1
            equipes[pos2].pontosCampeonato <- equipes[pos2].pontosCampeonato + PONTOS_VITORIA
            equipes[pos1].pontosCampeonato <- equipes[pos1].pontosCampeonato + PONTOS_DERROTA
            confrontos[m1,m2] <- 2
            confrontos[m2,m1] <- 1
         senão
            equipes[pos1].empates <- equipes[pos1].empates + 1
            equipes[pos2].empates <- equipes[pos2].empates + 1
            equipes[pos1].pontosCampeonato <- equipes[pos1].pontosCampeonato + PONTOS_EMPATE
            equipes[pos2].pontosCampeonato <- equipes[pos2].pontosCampeonato + PONTOS_EMPATE
            confrontos[m1,m2] <- 3
            confrontos[m2,m1] <- 3
         fimse
      fimse

      atualizarSaldo(pos1)
      atualizarSaldo(pos2)
      totalPartidas <- totalPartidas + 1
      escreval("Resultado registrado com sucesso.")
   fimse
fimprocedimento

// Compara duas equipes por pontos, vitorias, saldo e pontos marcados.
// O resultado e devolvido por parametro para evitar chamadas de funcao.
procedimento verificarOrdem(indiceA, indiceB: inteiro; var resultado: logico)
inicio
   resultado <- falso
   se equipes[indiceA].pontosCampeonato > equipes[indiceB].pontosCampeonato então
      resultado <- verdadeiro
   senão
      se equipes[indiceA].pontosCampeonato = equipes[indiceB].pontosCampeonato então
         se equipes[indiceA].vitorias > equipes[indiceB].vitorias então
            resultado <- verdadeiro
         senão
            se equipes[indiceA].vitorias = equipes[indiceB].vitorias então
               se equipes[indiceA].saldo > equipes[indiceB].saldo então
                  resultado <- verdadeiro
               senão
                  se (equipes[indiceA].saldo = equipes[indiceB].saldo) e (equipes[indiceA].pontosMarcados > equipes[indiceB].pontosMarcados) entao
                     resultado <- verdadeiro
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse
fimprocedimento

procedimento ordenarClassificacao
var
   i, j: inteiro
   auxiliar: TEquipe
   deveTrocar: logico
inicio
   // Bubble Sort: troca as equipes quando a seguinte deve ficar antes da atual.
   para i de 1 até totalEquipes - 1 faça
      para j de 1 até totalEquipes - i faça
         verificarOrdem(j+1, j, deveTrocar)
         se deveTrocar então
            auxiliar <- equipes[j]
            equipes[j] <- equipes[j+1]
            equipes[j+1] <- auxiliar
         fimse
      fimpara
   fimpara
fimprocedimento

procedimento exibirClassificacao
var
   i: inteiro
inicio
   se totalEquipes = 0 então
      escreval("Nao há equipes para classificar.")
   senão
      ordenarClassificacao
      escreval("--- CLASSIFICACAO GERAL ---")
      escreval("Pos. Equipe | P | V | E | D | PM | PS | SG")
      para i de 1 ate totalEquipes faça
         escreval(i, ". ", equipes[i].nome)
         escreval("   Pontos: ", equipes[i].pontosCampeonato, " | Vitorias: ", equipes[i].vitorias)
         escreval("   Empates: ", equipes[i].empates, " | Derrotas: ", equipes[i].derrotas)
         escreval("   Marcados: ", equipes[i].pontosMarcados, " | Sofridos: ", equipes[i].pontosSofridos)
         escreval("   Saldo: ", equipes[i].saldo)
         escreval("------------------------------")
      fimpara
   fimse
fimprocedimento

procedimento exibirEstatisticas
var
   i, totalVitorias, totalEmpates, maiorVitoria, maiorPontos, maiorSaldo, maiorMarcados: inteiro
   somaPontos: inteiro
inicio
   se totalEquipes = 0 então
      escreval("Cadastre equipes para consultar as estatisticas.")
   senao
      totalVitorias <- 0
      totalEmpates <- 0
      somaPontos <- 0
      maiorVitoria <- 1
      maiorPontos <- 1
      maiorSaldo <- 1
      maiorMarcados <- 1

      para i de 1 ate totalEquipes faça
         totalVitorias <- totalVitorias + equipes[i].vitorias
         totalEmpates <- totalEmpates + equipes[i]. empates
         somaPontos <- somaPontos + equipes[i].pontosMarcados
         se equipes[i].vitorias > equipes[maiorVitoria].vitorias então
            maiorVitoria <- i
         fimse
         se equipes[i].pontosCampeonato > equipes[maiorPontos].pontosCampeonato então
            maiorPontos <- i
         fimse
         se equipes[i].saldo > equipes[maiorSaldo].saldo então
            maiorSaldo <- i
         fimse
         se equipes[i].pontosMarcados > equipes[maiorMarcados].pontosMarcados então
            maiorMarcados <- i
         fimse
      fimpara

      escreval("Equipes cadastradas: ", totalEquipes)
      escreval("Partidas realizadas: ", totalPartidas)
      escreval("Vitorias registradas: ", totalVitorias)
      escreval("Empates registrados: ", totalEmpates)
      se totalPartidas > 0 então
         escreval("Média de pontos marcados por partida: ", somaPontos / totalPartidas)
      senao
         escreval("Média de pontos marcados por partida: ainda não há partidas.")
      fimse
      escreval("Mais vitórias: ", equipes[maiorVitoria].nome, " (", equipes[maiorVitoria].vitorias, ")")
      escreval("Maior pontuação no campeonato: ", equipes[maiorPontos].nome, " (", equipes[maiorPontos].pontosCampeonato, ")")
      escreval("Maior saldo: ", equipes[maiorSaldo].nome, " (", equipes[maiorSaldo].saldo, ")")
      escreval("Mais pontos marcados: ", equipes[maiorMarcados].nome, " (", equipes[maiorMarcados].pontosMarcados, ")")
   fimse
fimprocedimento

procedimento consultarConfrontos
var
   cod1, cod2, pos1, pos2, resultado: inteiro
inicio
   escreva("Codigo da primeira equipe: ")
   leia(cod1)
   buscarEquipe(cod1, pos1)
   escreva("Codigo da segunda equipe: ")
   leia(cod2)
   buscarEquipe(cod2, pos2)

   se (pos1 = 0) ou (pos2 = 0) então
      escreval("Uma ou ambas as equipes não foram encontradas.")
   senão
      se pos1 = pos2 então
         escreval("Uma equipe nao pode ser consultada contra ela mesma.")
      senão
         resultado <- confrontos[equipes[pos1].indiceMatriz, equipes[pos2].indiceMatriz]
         se resultado = 0 então
            escreval("Ainda não há resultado registrado para esse confronto.")
         senão
            se resultado = 1 então
               escreval("Vitoria de ", equipes[pos1].nome)
            senão
               se resultado = 2 então
                  escreval("Vitoria de ", equipes[pos2].nome)
               senão
                  escreval("O confronto terminou empatado.")
               fimse
            fimse
         fimse
      fimse
   fimse
fimprocedimento

procedimento contagemRegressiva(n: inteiro)
inicio
   se n <= 0 então
      escreval("CAMPEONATO INICIADO!")
   senão
      escreva(n, "... ")
      contagemRegressiva(n - 1)
   fimse
fimprocedimento

procedimento recursoRecursivo
var
   inicioContagem: inteiro
inicio
   escreva("Número inicial da contagem (entre 1 e 10): ")
   leia(inicioContagem)
   enquanto (inicioContagem < 1) ou (inicioContagem > 10) faça
      escreva("Valor inválido. Digite um numero de 1 a 10: ")
      leia(inicioContagem)
   fimenquanto
   contagemRegressiva(inicioContagem)
fimprocedimento

inicio
   totalEquipes <- 0
   totalPartidas <- 0
   para opcao de 1 ate MAX_EQUIPES faça
      para totalPartidas de 1 ate MAX_EQUIPES faça
         confrontos[opcao,totalPartidas] <- 0
      fimpara
   fimpara
   totalPartidas <- 0

   repita
      escreval("")
      escreval("===== ARENACODE CHAMPIONSHIP =====")
      escreval("1. Cadastrar equipe")
      escreval("2. Listar equipes")
      escreval("3. Registrar resultado de partida")
      escreval("4. Consultar equipe")
      escreval("5. Exibir classificacao geral")
      escreval("6. Exibir estatisticas do campeonato")
      escreval("7. Consultar confrontos")
      escreval("8. Executar recurso recursivo")
      escreval("9. Encerrar sistema")
      escreva("Escolha uma opcao: ")
      leia(opcao)

      escolha opcao
         caso 1
            cadastrarEquipe
         caso 2
            listarEquipes
         caso 3
            registrarPartida
         caso 4
            consultarEquipe
         caso 5
            exibirClassificacao
         caso 6
            exibirEstatisticas
         caso 7
            consultarConfrontos
         caso 8
            recursoRecursivo
         caso 9
            escreval("Sistema encerrado.")
         outrocaso
            escreval("Opcao invalida. Escolha um numero de 1 a 9.")
      fimescolha
   ate opcao = 9
fimalgoritmo
