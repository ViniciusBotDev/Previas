algoritmo "Fatorial"
var
   C, N, F:inteiro
   R: caractere
inicio
repita
      escreva("Digite um numero:")
      leia (N)
      C <- N
      F <- 1
      repita
            F <- F * C
            C <- c - 1
      ate (C < 1)
      escreval("o valor fatorial de ",N," é igual a ",F)
      escreva("deseja continuar? [S/N]")
      leia (R)
ate (R = "n")
fimalgoritmo