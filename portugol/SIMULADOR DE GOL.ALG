algoritmo "Simulador de gol"
var
   gre, inter, med: inteiro
inicio
      escreval("---------------------------")
      escreva("Quantos gols Grêmio fez? ")
      leia (gre)
      escreva("Quantos gols Inter fez? ")
      leia (inter)
      escreval("---------------------------")
      med <- abs(gre - inter)
      escreval ("Diferencia ",med)
      escreva("STATUS: ")
      se (med >= 1) e (med <= 3) entao
         escreva("Partida Normal")
      senao
           se (med = 0) entao
              escreva("Empate")
           senao (med >= 5) entao
                 escreva("Goleada")
           fimse
      fimse
      escreval("")
      escreval("---------------------------")
fimalgoritmo