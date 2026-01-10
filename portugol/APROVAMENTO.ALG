algoritmo "APROVAMENTO"
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
      leia(notadois)
      escreva("   Terceira Nota: ")
      leia(notatres)
      media <- (notaum + notadois + notatres) / 3
      escreval("----------------------------------------------------")
      escreval("   Sua Média é: ",media:4:2)
      se (media >= 6) entao
         escreval("   Parebéns voçe alcançou a Média! E foi APROVADO!")
      senao
          se (media >= 4) e (media <= 6) entao
             escreval("Voçe não atingiu a média, Mas está de RECUPERÇÃO.")
          senao
           escreval("   Voçe NÃO alcançou a Média. E NÃO foi aprovado.")
          fimse
      fimse
      escreval("----------------------------------------------------")
      
fimalgoritmo