algoritmo "timer legal"
var
   contador, numb:inteiro
   resp,M:caractere
inicio
repita
      escreval("Qual tipo tu quer: Regressiva=R e Progressiva=P")
      leia(resp)
      se (resp = "P") entao
         escreva("Qual numero voçe quer iniciar: ")
         leia(contador)
         escreva("Qual numero deseja finalizar: ")
         leia(numb)
         contador <- contador
         repita
               contador <- contador + 1
               escreval(contador)
         ate contador = numb
      senao
           se (resp = "R") entao
           escreva("Qual numero voçe quer iniciar: ")
           leia (contador)
           escreva("Qual numero deseja finalizar: ")
           leia (numb)
           contador <- contador
           repita
                 contador <- contador - 1
                 escreval(contador)
           ate contador = numb
           fimse
      fimse
escreva("Deseja parar agora? [S/N] ")
leia(M)
ate M = "N"
fimalgoritmo