algoritmo "loko"
var
I: inteiro
N, Pesado: caractere
P, Mai: real
procedimento topo()
inicio
      limpatela
      escreval("-----------------------------------------")
      escreval(" D E T E C T O R  DE  P E S A D O")
      escreval("maior peso ate agora: ",Mai, "Kg")
      escreval("-----------------------------------------")
fimprocedimento
inicio
      topo()
      para i <- 1 ate 5 faca
           escreva("digite o nome: ")
           leia(N)
           escreva("digite o peso de ",N," : ")
           leia(P)
           se (P>Mai) entao
              Mai <- P
              Pesado <- N
           fimse
           topo()
      fimpara
      topo()
      escreval("A pessoa mais pesada foi ",Pesado," com ",Mai," quilos")
fimalgoritmo