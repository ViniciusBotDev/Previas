algoritmo "dubom"
var
   R, D: real
   vzs, C: inteiro
inicio
      C <- 1
      escreva("Quantas conversoes deseja realizar? ")
      leia (vzs)
      enquanto ( C <= vzs) faca
               escreva("Qual o valor em R$ ")
               leia (R)
               D <- R/5.54
               escreval("O valor convertido em US$", D:5:2)
               C <- C + 1
      fimenquanto
fimalgoritmo