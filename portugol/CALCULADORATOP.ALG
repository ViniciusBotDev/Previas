algoritmo "calculadoratop"
var
   n1, n2, tot:real
   resp,dic:caractere
inicio
      repita
      limpatela
      escreva("Digite um numero: ")
      leia (n1)
      escreva("digite outro numero: ")
      leia (n2)
      escreva("agora digite qual operaçao quer usar: ")
      leia (dic)
           escolha dic
                  caso "+"
                  tot <- n1 + n2
                  caso "-"
                  tot <- n1 - n2
                  caso "*"
                  tot <- n1 * n2
                  caso "/"
                  tot <- n1 / n2
                  outrocaso
                  escreval ("operacao invalida")
           fimescolha
      escreval(" O resultado do seu calculo é ",tot," Escreva [S/N] se deseja continuar")
      leia(resp)
      ate(resp = "n")
fimalgoritmo