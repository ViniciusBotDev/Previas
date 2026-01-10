algoritmo "timerinteligente"
var
    i, f, cont:real
inicio
      escreval("-------------------------")
      escreval("    Timer Inteligente    ")
      escreval("-------------------------")
      escreva("Qual numero começar? ")
      leia (i)
      escreva("Qual numero o fim? ")
      leia (f)
      se (f > i) entao
         cont <- i
         enquanto (cont <= f) faca
                  escreval(cont)
                  cont <- cont + 1
         fimenquanto
      senao
            cont <- i
            enquanto ( cont >= f) faca
                     escreval(cont)
                     cont <- cont - 1
            fimenquanto
      fimse
fimalgoritmo