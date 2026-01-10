algoritmo "Primos"
var
   C, N, contdiv:inteiro
inicio
      C <- 1
      contdiv <- 0
      escreva("digite um numero: ")
      leia(N)
      repita
            se (N % C = 0) entao
               contdiv <- contdiv + 1
            fimse
            C <- C + 1
      ate (C > N)
      se (contdiv > 2) entao
         escreval(" O valor ",N," Não é primo!")
      senao
           escreval(" O valor ",N," é Primo!")
      fimse
fimalgoritmo