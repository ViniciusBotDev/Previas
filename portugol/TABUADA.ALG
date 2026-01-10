algoritmo "tabuada"
var
   i,numero,tot,n1:inteiro
   resp:caractere
inicio
repita
      limpatela
      escreva("escreva um numero que deseja ver a tabuada: ")
      leia(numero)
      escreva(n1)                  "deseja repitir ver a tabuada até quando? ")
      leia(
      i <- 1
      repita
        numero <- numero * 1
        tot <- numero * i
        escreval(numero," x ",i," = ",tot)
        i <- i + 1
      ate(i > n1)
      escreva("deseja continuar? ")
      leia(resp)
ate(resp = "n")
fimalgoritmo