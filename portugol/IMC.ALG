algoritmo "IMC"
var
     M, A, IMC: real
inicio
      Escreva("Sua Altura: ")
      leia (A)
      escreva("Seu Massa (KG): ")
      leia (M)
      IMC <- M / (A ^ 2)
      escreval("IMC: ", IMC:5:2)
      se (IMC < 17) entao
         escreval("Muito abaixo do Peso")
      senao
           se (IMC >= 17) e (IMC < 18.5) entao
              escreval("Abaixo do Peso")
           senao
                se (IMC >= 18.5) e (IMC < 25) entao
                   escreval("Peso Ideal")
                senao
                     se (IMC >= 25) e (IMC < 30) entao
                        escreval("Sobrepeso")
                     senao
                          se (IMC >= 30) e (IMC < 35) entao
                             escreval("Obesidade")
                          senao
                               se (IMC >= 35) e (IMC <40) entao
                                  escreval("Obesidade Severa")
                               senao
                                    escreval("Obesidade Morbida")
                               fimse
                          fimse
                     fimse
                fimse
           fimse
      fimse
fimalgoritmo