salario = float(input("Informe o salário:"))


if salario <=2000:
        print ("Programador junior")
elif salario > 2000 and salario <=6000:
        print ("Programador pleno ")
elif salario >6000 and salario <=15000:
        print ("Programador Senior")
else:
        print ("Gerente de projetos")