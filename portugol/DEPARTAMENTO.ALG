algoritmo "DEPARTAMENTO"
var
   ano, nasc, idade: inteiro
   nome: caractere
inicio
      escreval("-----------------------------------------------")
      escreval("              Departasmento de transito        ")
      escreval("-----------------------------------------------")
      escreva("   Escreva seu nome: ")
      leia (nome)
      Escreva("   Ano atual (yyyy): ")
      leia (ano)
      escreva("   Ano de Nascimento: ")
      leia (nasc)
      idade <- ano - nasc
      escreva("")
      escreval("-----------------------------------------------")
      escreval("                    STATUS                     ")
      escreval("-----------------------------------------------")
      escreval("   IDADE: ",idade)
      se (idade >= 18) entao
         escreval("   Voçe estás apto a tirar sua habilitação.")
      senao
           escreval("   Voçe NÃO está apto a tirar sua habilitação.")
      fimse
      escreval("-----------------------------------------------")
fimalgoritmo