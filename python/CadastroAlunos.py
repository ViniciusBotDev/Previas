alunos = []

while True:
    nome = input("Nome: ")
    nota = float(input(f"Nota de {nome}: "))
    
    alunos.append({"Nome": nome, "Nota": nota})
    
    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar.lower() == 'n':
        break
print("\n----- RESULTADO FINAL -----")
for Aluno in alunos:
    if Aluno["Nota"] >= 6:
        status = "APROVADO"
    else:
        status = "REPROVADO"
    print(f"Aluno: {Aluno['Nome']} | Nota: {Aluno['Nota']} | Status: {status}") 
