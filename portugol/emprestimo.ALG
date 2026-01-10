algoritmo "Vou trabalhar no banco"
var
   tantos, empre, par, vpar: real
inicio
      escreva ("Quanto voçe deseja pegar de emprestimo? R$")
      leia (tantos)
       empre <- (tantos*20)/100
      empre <- (tantos+empre)
       escreva ("Quantas parecelar? ")
       leia (par)
       vpar <- (empre/par)
       escreval ("")
       escreval ("Então voçe vai pagar",par, " parcelas de R$",vpar )
       escreva ("E o valor total com juros ficará R$",empre)
fimalgoritmo