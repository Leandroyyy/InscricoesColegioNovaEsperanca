print("="*100)
print("Colégio Nova Esperança")
print("="*100)

nome_aluno = []
matricula = []
serie = []
quantidade_inscritos = []

cadastrado = True

list_sinais = []
list_emoji = []
list_hist = []
list_exp_art = []
list_leitura_dinamica = []
list_leitura_dramatica = []
list_corpo_fala = []
list_mundo = []
list_soletra = []
list_teatro = []

def menu():
        menu = int(input('''Menu de opções 
1 - Realizar cadastro
2 - Fazer inscrições 
3 - Listar inscrições
4 - Sair
->>> '''))
        return menu

def menu_sem_opcao1():
        menu = int(input(
        '''Menu de opções 
1 - INDISPONÍVEL 
2 - Fazer inscrições 
3 - Listar inscrições 
4 - Sair 
->>> '''))
        return menu

def cadastrar_aluno():
        rm = 1
        while(rm != 0):
                print("="*22)
                print("====  Novo Aluno  ====")
                print("="*22)
                rm = int(input("Digite o RM do aluno \n->>>  "))
                while(rm in matricula):
                        print("RM DUPLICADO!")
                        rm = int(input("Digite o RM do aluno \n->>>  "))
                        if(rm == 0):
                                break
                if(rm != 0):
                        matricula.append(rm)
                        nome = (input("Digite o nome do aluno \n->>> ").capitalize())
                        nome_aluno.append(nome)
                        serie_atual = int(input("Digite a série do aluno \n->>> "))
                        while(serie_atual <= 1 or serie_atual >= 6):
                                print("Só são permitidos alunos da 2ª à 5ª série")
                                serie_atual = int(input("Digite a série do aluno \n->>> "))
                        serie.append(serie_atual)
                        quantidade_inscritos.append(0)

def inscricoes():
        rm = int(input("Digite o RM do aluno \n->>>  "))
        while(rm not in matricula and rm != 0):
                print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")
                rm = int(input("Digite o RM do aluno \n->>> "))
        if(rm != 0):      
                serie_atual = serie[matricula.index(rm)]

                hist = "Criar e contar histórias (Vagas disponíveis: {})".format(10-len(list_hist))
                teatro = "Teatro: Luz, Câmera e Ação (Vagas disponíveis: {})".format(10-len(list_teatro))
                sinais = "A língua de sinais (Vagas disponíveis: {})".format(10-len(list_sinais))
                exp_art = "Expressão Artística (Vagas disponíveis: {})".format(10-len(list_exp_art))
                soletr = "Soletrando (Vagas disponíveis: {})".format(10-len(list_soletra))
                leit_dram = "Leitura dramática (Vagas disponíveis: {})".format(10-len(list_leitura_dramatica))
                corpo_fala = "O corpo Fala (Vagas disponíveis: {})".format(10-len(list_corpo_fala))
                mundo = "O mundo da imaginação (Vagas disponíveis: {})".format(10-len(list_mundo))
                leit_din = "Leitura dinâmica (Vagas disponíveis: {})".format(10-len(list_leitura_dinamica))
                emoji = "Criando e recriando com emojis (Vagas disponíveis: {})".format(10-len(list_emoji))

                if(len(list_hist) == 10):
                    hist = "==== INDISPONIVEL ===="
                if(len(list_teatro) == 10):
                    teatro = "==== INDISPONIVEL ===="
                if(len(list_sinais) == 10):
                    sinais = "==== INDISPONIVEL ===="
                if(len(list_exp_art) == 10):
                    exp_art = "==== INDISPONIVEL ===="
                if(len(list_soletra) == 10):
                    soletr = "==== INDISPONIVEL ===="
                if(len(list_leitura_dramatica) == 10):
                    leit_dram = "==== INDISPONIVEL ===="
                if(len(list_corpo_fala) == 10):
                    corpo_fala = "==== INDISPONIVEL ===="
                if(len(list_mundo) == 10):
                    mundo = "==== INDISPONIVEL ===="
                if(len(list_leitura_dinamica) == 10):
                    leit_din = "==== INDISPONIVEL ===="
                if(len(list_emoji) == 10):
                    emoji = "==== INDISPONIVEL ===="
    
                if(serie_atual == 2):
                        cadastrado = False
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, sinais, mundo, emoji))
                        seleciona = int(input("->>> "))

                        if(quantidade_inscritos[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in list_hist and len(list_hist) < 10):
                                        list_hist.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 2 and rm not in list_sinais and len(list_sinais) < 10):
                                        list_sinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 3 and rm not in list_mundo and len(list_mundo) < 10):
                                        list_mundo.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 4 and rm not in list_emoji and len(list_emoji) < 10):
                                        list_emoji.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrado):
                                        quantidade_inscritos[matricula.index(rm)] += 1
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
            
                if(serie_atual == 3):
                        cadastrado = False
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(hist, teatro, sinais,corpo_fala))
                        seleciona = int(input("->>> "))

                        if(quantidade_inscritos[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in list_hist and len(list_hist) < 10):
                                        list_hist.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 2 and rm not in list_teatro and len(list_teatro) < 10):
                                        list_teatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 3 and rm not in list_sinais and len(list_sinais) < 10):
                                        list_sinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 4 and rm not in list_corpo_fala and len(list_corpo_fala) < 10):
                                        list_corpo_fala.append(rm)
                                        print("ALUNO CADASTRO")
                                        cadastrado = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrado):
                                        quantidade_inscritos[matricula.index(rm)] += 1
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")

                if(serie_atual == 4):
                        cadastrado = False
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(teatro, sinais, exp_art, leit_dram))
                        seleciona = int(input("->>> "))

                        if(quantidade_inscritos[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in list_teatro and len(list_teatro) < 10):
                                        list_teatro.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 2 and rm not in list_sinais and len(list_sinais) < 10):
                                        list_sinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 3 and rm not in list_exp_art and len(list_exp_art) < 10):
                                        list_exp_art.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 4 and rm not in list_leitura_dramatica and len(list_leitura_dramatica) < 10):
                                        list_leitura_dramatica.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrado):
                                        quantidade_inscritos[matricula.index(rm)] += 1
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")
            
                if(serie_atual == 5):
                        cadastrado = False
                        print("Escolha um evento \n1 - {} \n2 - {} \n3 - {} \n4 - {}\n".format(sinais, exp_art, soletr, leit_din))
                        seleciona = int(input("->>> "))
                        if(quantidade_inscritos[matricula.index(rm)] < 3):
                                if(seleciona == 1 and rm not in list_sinais and len(list_sinais) < 10):
                                        list_sinais.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 2 and rm not in list_exp_art and len(list_exp_art) < 10):
                                        list_exp_art.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 3 and rm not in list_soletra and len(list_soletra) < 10):
                                        list_soletra.append(rm)
                                        print("ALUNO CADASTRADO")
                                        cadastrado = True
                                elif(seleciona == 4 and rm not in list_leitura_dinamica and len(list_leitura_dinamica) < 10):
                                        list_leitura_dinamica.append(rm)
                                        print("ALUNO CADASTRADO") 
                                        cadastrado = True
                                else:
                                        print("ALUNO JA FOI CADASTRADO")
                                if(cadastrado):
                                        quantidade_inscritos[matricula.index(rm)] += 1
                        else:
                                print("APENAS TRÊS INSCRIÇÕES POR ALUNO")

def ajustar_aluno(nome, rm, serie):
        inscricoes  = []
        aluno = ()
        if(rm in list_hist):
                inscricoes.append("Criar e contar histórias - 2ª. feira - Matutino")
        if(rm in list_teatro):
                inscricoes.append("Teatro: Luz, Câmera e Ação - 3ª. feira – Matutino")
        if(rm in list_sinais):
                inscricoes.append("A língua de sinais - 4ª. feira - Matutino")
        if(rm in list_exp_art):
                inscricoes.append("Expressão Artística - 5ª. feira - Matutino")
        if(rm in list_soletra):
                inscricoes.append("Soletrando - 6ª. feira - Matutino")
        if(rm in list_leitura_dramatica):
                inscricoes.append("Leitura dramática - 2ª. feira - Vespertino")
        if(rm in list_corpo_fala):
                inscricoes.append("O corpo fala - 3ª. feira - Vespertino")
        if(rm in list_mundo):
                inscricoes.append("O mundo da imaginação - 4ª. feira - Vespertino")
        if(rm in list_leitura_dinamica):
                inscricoes.append("Leitura dinâmica - 5ª. feira - Vespertino")
        if(rm in list_emoji):
                inscricoes.append("Criando e recriando com emojis - 6ª. feira - Vespertino")

        if(len(inscricoes) == 3):
                aluno = (rm, nome, serie, inscricoes[0], inscricoes[1], inscricoes[2])
        elif(len(inscricoes) == 2):
                aluno = (rm, nome, serie, inscricoes[0], inscricoes[1])
        elif(len(inscricoes) == 1):
                aluno = (rm, nome, serie, inscricoes[0])
        elif(len(inscricoes) == 0):
                aluno = (rm, nome, serie)


        if(len(aluno) == 6):
                x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
        elif(len(aluno) == 5):
                x = "RM: {} - {} - {}ª. série \nOficinas: \n{} \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4])
        elif(len(aluno) == 4):
                x = "RM: {} - {} - {}ª. série \nOficinas: \n{}\n".format(aluno[0], aluno[1], aluno[2], aluno[3])
        elif(len(aluno) == 3):
                x = "RM: {} - {} - {}ª. série \nO aluno não está cadastrado em nenhuma oficina\n".format(aluno[0], aluno[1], aluno[2])
        return x

def lista_nomes(nome):
        cadastro = []
        for i in range(len(nome)):
                list = (nome_aluno[i], matricula[i], serie[i])
                cadastro.append(list)  

        cadastro_ordenado = sorted(cadastro)
        return cadastro_ordenado

def listar_oficinas():
        oficina1 = ("A língua de sinais - 4ª. feira - Matutino", list_sinais)
        oficina2 = ("Criando e recriando com emojis - 6ª. feira - Vespertino", list_emoji)
        oficina3 = ("Criar e contar histórias - 2ª. feira - Matutino", list_hist)
        oficina4 = ("Expressão Artística - 5ª. feira - Matutino", list_exp_art)
        oficina5 = ("Leitura dinâmica - 5ª. feira - Vespertino", list_leitura_dinamica)
        oficina6 = ("Leitura dramática - 2ª. feira - Vespertino",list_leitura_dramatica)
        oficina7 = ("O corpo fala - 3ª. feira - Vespertino", list_corpo_fala)
        oficina8 = ("O mundo da imaginação - 4ª. feira - Vespertino", list_mundo)
        oficina9 = ("Soletrando - 6ª. feira - Matutino", list_soletra)
        oficina10 = ("Teatro: Luz, Câmera e Ação - 3ª. feira – Matutino", list_teatro)
        
        oficinas = [oficina1, oficina2, oficina3, oficina4, oficina5, oficina6, oficina7, oficina8, oficina9, oficina10]

        return oficinas 

def oficinas(oficinas):
        for i in range(len(oficinas)):
                atual = oficinas[i]
                print(atual[0])
                alunos = atual[1]
                cont_alunos = 0
                for i in range(len(alunos)):
                        rm = alunos[cont_alunos]
                        nome_atual = nome_aluno[cont_alunos]
                        serie_atual = serie[cont_alunos]
                        print("RM: {} - {} - {}ª. série".format(rm, nome_atual, serie_atual))
                        cont_alunos += 1
                if(len(alunos) > 1):
                        print("\nTotal: {} alunos".format(len(alunos)))
                elif(len(alunos) == 1):
                        print("\nTotal: {} aluno".format(len(alunos)))
                else:
                        print("Nenhum aluno cadastrado")
                print("\n"+"-"*60+"\n")

while True:
        if(cadastrado):
                menu = menu()
        else:
                menu = menu_sem_opcao1()

        if(menu == 1 and cadastrado == False):
                print("="*44)

                print("====  OS CADASTROS JÁ FORAM REALIZADOS  ====")

                print("="*44)
        elif(menu == 1 and cadastrado == True):
                cadastrar_aluno()
                cadastrado = False

        elif(menu == 2):
                inscricoes()

        elif(menu == 3):
                print("Listar inscrições \n1 - Listar por aluno (ordem alfabética de nome) \n2 - Listar por oficina (ordem alfabética) \n3 - Sair")
                opcao = int(input("->>> "))
                while(opcao < 1 or opcao > 3):
                        opcao = int(input("Opção inválida, digite novamente. \n->>> "))
                if(opcao == 1):
                       print("\n***** Alunos inscritos – Ordem: Alfabética (nome) *****\n")
                       print("Oficinas: \n")
                       lista = lista_nomes(nome_aluno)
                       for i in range(len(lista)):
                                tupla = lista[i]
                                print(ajustar_aluno(tupla[0], tupla[1], tupla[2]))                         
                if(opcao == 2):
                        print("***** Alunos inscritos – Ordem: Alfabética (Oficinas) *****\n")
                        print("Oficinas: \n")
                        oficinas(listar_oficinas())
                if(opcao == 3):
                        continue
             
        elif(menu == 4):
                break