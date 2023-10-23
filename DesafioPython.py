
registros_alunos = []


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    id_aluno = input("Digite o ID do aluno: ")
    notas = input("Digite as notas separadas por espaço: ")
    notas = [float(nota) for nota in notas.split()]
    registro = {'Nome': nome, 'ID': id_aluno, 'Notas': notas}
    registros_alunos.append(registro)
    print("Registro adicionado com sucesso!\n")


def exibir_registros():
    for estudante in registros_alunos:
        print(f"Nome: {estudante['Nome']}, ID: {estudante['ID']}, Notas: {estudante['Notas']}")


def buscar_por_id():
    id_procurado = input("Digite o ID do estudante que deseja buscar: ")
    for estudante in registros_alunos:
        if estudante['ID'] == id_procurado:
            print(f"Registro encontrado:\nNome: {estudante['Nome']}, ID: {estudante['ID']}, Notas: {estudante['Notas']}")
            break
    else:
        print("ID não encontrado.\n")


def calcular_media_notas():
    if len(registros_alunos) == 0:
        print("Não há estudantes registrados.")
        return
    total_notas = sum(sum(estudante['Notas']) for estudante in registros_alunos)
    media = total_notas / sum(len(estudante['Notas']) for estudante in registros_alunos)
    print(f"Média de notas de todos os estudantes: {media:.2f}\n")

def excluir_estudante():
    id_excluir = input("Digite o ID do estudante que deseja excluir: ")
    for estudante in registros_alunos:
        if estudante['ID'] == id_excluir:
            registros_alunos.remove(estudante)
            print(f"Estudante com ID {id_excluir} foi excluído com sucesso.\n")
            return
    print(f"Estudante com ID {id_excluir} não encontrado.\n")

   
    
def salvar_registros_em_arquivo():

    with open('registros_estudantes.txt', 'w') as arquivo:
        for estudante in registros_alunos:
            linha = f"{estudante['Nome']},{estudante['ID']},{','.join(map(str, estudante['Notas']))}\n"
            arquivo.write(linha)
    print("Registros de estudantes foram salvos no arquivo.\n")


def carregar_registros_de_arquivo():
    try:
        with open('registros_estudantes.txt', 'r') as arquivo:
            registros_alunos.clear()  
            for linha in arquivo:
                partes = linha.strip().split(',')
                nome = partes[0]
                id_aluno = partes[1]
                notas = [float(nota) for nota in partes[2:]]
                registro = {'Nome': nome, 'ID': id_aluno, 'Notas': notas}
                registros_alunos.append(registro)
        print("Registros de estudantes foram carregados do arquivo.\n")
    except FileNotFoundError:
        print("O arquivo de registros de estudantes não foi encontrado.\n")



while True:
    print("Escolha uma opção:")
    print("1. Adicionar registro de estudante")
    print("2. Exibir registros de estudantes")
    print("3. Procurar estudante por ID")
    print("4. Calcular média de notas de todos os estudantes")
    print("5. Salvar registros em um arquivo de texto")
    print("6. Carregar registros de um arquivo de texto")
    print("7. Excluir estudante por ID")
    print("8. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        exibir_registros()
    elif opcao == '3':
        buscar_por_id()
    elif opcao == '4':
        calcular_media_notas()
    elif opcao == '5':
        salvar_registros_em_arquivo()
    elif opcao == '6':
        carregar_registros_de_arquivo()
    elif opcao == '7':
        excluir_estudante()
    elif opcao == '8':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
