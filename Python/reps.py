notas =[]

for x in range(5) :
    codido_aluno = input ("RA: ")
    nota = float(input("nota:"))
    resultado = [codido_aluno, nota]
    notas.append(resultado)

print( "quantidade de notas", len (notas))    

for n in notas:
    codido_aluno = n[0]
    nota = n[1]
    print("O RA", codido_aluno, "tirou a nota:", nota)