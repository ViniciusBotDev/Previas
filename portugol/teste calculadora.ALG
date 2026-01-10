algoritmo "semnome"
var
   N,N2,tot,resp3:real
   resp,resp2:caractere

inicio
   repita
      limpatela
      escreval("====================================")
      escreval("    C A L C U L A D O R A    ")
      escreval("====================================")
      escreva(" Digite um numero: ")
      leia(N)
      escreva(" Digite outro numero: ")
      leia(N2)
      escreval("====================================")
      escreval("Digite a expressão que deseja utilizar: ")
      escreval("[1] Somar")
      escreval("[2] Subtração")
      escreval("[3] Multiplicaçao")
      escreval("[4] Divisão")
      leia(resp)
      escolha resp
      caso "1"
         tot <- N + N2
         escreval("A soma de ",N," e ",N2," é igual a: ",tot)
      caso "2"
         tot <- N - N2
         escreval("A subtração de ",N," e ",N2," é igual a: ",tot)
      caso "3"
         tot <- N * N2
         escreval("A multiplicação de ",N," e ",N2," é igual a: ",tot)
      caso "4"
         tot <- N / N2
         escreval("A divisão de ",N," e ",N2," é igual a: ",tot)
      fimescolha

      escreva("Quer sair? ")
      leia(resp2)
   ate (resp2 = "s")
fimalgoritmo