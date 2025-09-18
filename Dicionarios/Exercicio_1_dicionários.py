#Dicion]ario principal para armanezar os dados dos alunos
Alunos = {"nome_Aluno" : "x", "idade_Aluno" : "y", "curso_Aluno" : "z"}

#Lista de cursos permitidos para validação
cursos_validos = ["Engenharia", "Medicina", "Direito", "Ciência da Computação"]

#Loop para grantir a escolh certa dos cursos permitidos
while True:
    print(f"\nCursos disponíveis: ")
    for curso in cursos_validos:
        print(f"{cursos_validos}")
        Student_curso= input(str("Introduza o curso: "))
    if Student_curso in cursos_validos:
     break  # Sai do loop
    else:
         print("Curso inválido. Por favor, escolha um dos cursos da lista.")

#Outros dados dos alunos
    Student_name = input(str("Insira um nome do aluno: "))
    Student_age= input(str("Introduzida a idade do aluno: "))

#Atualiza o dicionário
    Alunos.update({"nome_Aluno" : Student_name , "idade_Aluno" : Student_age , "curso_Aluno" : Student_curso })

    for key in sorted(Alunos.keys()):
     print(f"{key}: {Alunos[key]}")