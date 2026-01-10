algoritmo "APROVAMENTO de filha da puta"
var
   nome:caractere
   notaum, notadois, notatres, media: real
inicio
      escreval("----------------------------------------------------")
      escreval("                    ESCOLA DE BOI                   ")
      escreval("----------------------------------------------------")
      escreva("   Qual seu nome: ")
        leia (nome)
      escreva("   Primeira Nota: ")
        leia (notaum)
      escreva("   Segunda Nota: ")
       leia (notadois)
      escreva("   Terceira Nota: ")
        leia(notatres)
      media <- (notaum + notadois + notatres) / 3
      escreval("----------------------------------------------------")
      escreval("   Sua Média é: ",media:4:2)
      se (media >= 6) e (media <= 6.9) entao
         escreval("   APROVEITAMENTO: D")
      senao
          se (media = 5) entao
             escreval("   APROVEITAMENTO: E")
          senao
               se (media <= 4) entao
                  escreval("   APROVEITAMENTO: F")
               senao
                    se (media >= 7) e (media <= 7.9) entao
                       escreval("   APROVEITAMENTO: C")
                    senao
                         se (media >= 8) e (media <= 8.9) entao
                            escreval("   APROVEITAMENTO: B")
                         senao
                              se (media >= 9) entao
                                 escreval("   APROVEITAMENTO: A")
                              fimse
                         fimse
                    fimse
               fimse
          fimse
      fimse
      
se (media >= 6) entao
   escreval("   Parabéns voçe foi APROVADO! ",nome)
senao
     se (media < 6) entao
        escreval("   Voçe NÃO ficou na média e não foi aprovado. ",nome)
     fimse
fimse
      escreval("----------------------------------------------------")
      
fimalgoritmo