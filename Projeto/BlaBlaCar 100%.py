usuarios = [{
    'nome': "Rafael",
    'email': "rafa@gmail.com",
    'senha': "123",
    'carteira': 25
}]
caronas = [{
    'motorista': "Rafael",
    'emailMot': "rafa@gmail.com",
    'origem': "Cajazeiras",
    'destino': "Sousa",
    'data': "13/05/2026",
    'hora': "15:00",
    'vagas': 3,
    'valor': 10.00,
    'passageiros': ["Allan"]
}]

login = False
emailLog = ""
nomeLog = ""
saldo = 0

while True:
    while login == False:
        print("-" * 30)
        print("Bem-vindo ao BlablaCar!")
        print("-" * 30)
        opcao = input("\nEscolha uma das opções:\n\n"
                "1- Cadastro \n"
                "2- Login \n"
                "0- Sair \n\n"
                "Opção: ")
        
        if opcao == "0":
            break

        elif opcao == "1":
            print("\nPara Cadastro de usuario, siga o passo a passo.")
            nome = input("\nDigite seu nome: ").capitalize()
            
            emailV = False
            while emailV == False:
                email = input("\nDigite seu email: ").lower()

                if "@" in email and email.endswith(".com"):
                    for ema in usuarios:
                        if not ema.get('email') == email:
                            emailV = True
                        else:
                            print("\nEsse email já existe! Tente novamente.\n")
                else:
                    print("\nDigite um email correto. Certifique que contem '@' e termine com '.com'\n")
            
            senha = input("\nDigite sua senha: ")
            while len(senha) < 8:
                print("Insira uma senha no minimo com 8 caracters")
                senha = input("\nDigite uma senha: ")
            
            print("\nCadastro feito com sucesso\n")
            usuarios.append({'nome': nome, 'email': email, 'senha': senha, 'carteira': 10})

        elif opcao == "2":
            print("\nPara login de usuario: ")
            
            emailV = False
            while emailV == False:
                email = input("\nDigite seu email: ").lower()
                if "@" in email and email.endswith(".com"):
                    emailV = True
                else:
                    print("\nDigite um email correto. Certifique que contem '@' e termine com '.com'\n")

            senha = input("\nDigite sua senha: ")
            for log in usuarios:
                if log.get('email') == email and log.get('senha') == senha:
                    login = True
                    emailLog = email
                    nomeLog = log.get('nome')
                    print("\nLogin feito com sucesso!\n")

            if login == False:
                print("\nInsira um usuario existente!")
        
        else:
            print("\nDigite uma opção valída! Tente novamente.")
    
    if opcao == "0":
        break

    while login == True:
        print("#" * 30)
        print("Menu de Usuario!")
        print("#" * 30)
        for din in usuarios:
            if din.get('email') == emailLog:
                saldo = din['carteira']

        print(f"\nSeu saldo é de: R$ {saldo:.2f}\n")
        opcao = input("Escolha uma das opções abaixo: \n\n"
                    "1- Cadastro de Carona\n"
                    "2- Listar Caronas Disponiveis\n"
                    "3- Busca de Carona por Destino\n"
                    "4- Reservar Carona\n"
                    "5- Cancelar Reserva\n"
                    "6- Remover Carona\n"
                    "7- Ver detalhes de uma Carona\n"
                    "8- Caronas Cadastradas\n"
                    "9- BlablaPay\n"
                    "0- Logout\n"
                    "O que deseja fazer? ")
        
        if opcao == "0":
            login = False
            emailLog = ""
            nomeLog = ""
            saldo = 0
        
        elif opcao == "1":
            print("\nPara cadastrar uma Carona, informe: ")
            
            for mot in usuarios:
                if mot.get('email') == emailLog:
                    motorista = mot.get('nome')

            origem = input("\nDe onde está partindo? ").capitalize()
            destino = input("\nPara onde quer ir? ").capitalize()

            valido = False
            data = input("\nEm qual dia, mês e ano (dd/mm/aaaa)? ")
            while valido == False:
                dia = int(data[0:2])
                mes = int(data[3:5])
                ano = int(data[6:10])
                
                if ano >= 2025:
                    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                        if dia >=1 and dia <=31:
                            valido = True
                    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                        if dia >=1 and dia <=30:
                            valido = True
                    elif mes == 2:
                        if dia >=1 and dia <=29:
                            valido = True
                else:
                    print("\nDigite uma data válida!\n")
                    data = input("\nEm qual dia, mês e ano (dd/mm/aaaa)? ")
            
            validoH = False
            hora = input("\nQual horario de partida? ")
            while validoH == False:
                h = int(hora[0:2])
                m = int(hora[3:5])
                if h <= 23 and h >= 0:
                    if m <= 60 and m >= 0:
                        validoH = True
                else:
                    print("\nDigite um hora valida!\n")
                    hora = input("\nQual horario de partida? ")
            
            vagas = int(input("\nQuantas vagas estão disponíveis? ")) 
            valor = float(input("\nQuanto quer cobrar por passageiro? "))
            caronas.append({
                'motorista': motorista,
                'emailMot': emailLog,
                'origem': origem,
                'destino': destino,
                'data': data,
                'hora': hora,
                'vagas': vagas,
                'valor': valor,
                'passageiros': []
            })
            print("\nCarona cadastrada com sucesso!\n")

        elif opcao == "2":
            for carona in caronas:
                print("-" * 20)
                print("Motorista: ", carona['motorista'])
                print("Email do Motorista: ", carona['emailMot'])
                print("Origem: ", carona['origem'])
                print("Destino: ", carona['destino'])
                print("Data: ", carona['data'])
                print("Horario: ", carona['hora'])
                print("Vagas: ", carona['vagas'])
                print("Valor por vaga: ", carona['valor'])
                print("-" * 20)
        
        elif opcao == "3":
            print("Busca de Carona por Destino")
            origemBusca = input("\nDe onde está saindo? ").capitalize()
            destinoBusca = input("\nPara onde está indo? ").capitalize()
            busc = False

            for busca in caronas:
                if busca.get('origem') == origemBusca and busca.get('destino') == destinoBusca:
                    busc = True
                    print("-" * 20)
                    print("Motorista: ", busca['motorista'])
                    print("Email do Motorista: ", busca['emailMot'])
                    print("Origem: ", busca['origem'])
                    print("Destino: ", busca['destino'])
                    print("Data: ", busca['data'])
                    print("Horario: ", busca['hora'])
                    print("Vagas: ", busca['vagas'])
                    print("Valor por vaga: ", busca['valor'])
                    print("-" * 20)
            if busc == False:
                print("\nNão há caronas para este destino. Tente novamente\n")
        
        elif opcao == "4":
            print("\nPara reservar uma carona, informe: ")

            emailV = False
            while emailV == False:
                emailCarona = input("\nDigite o email do Motorista: ").lower()
                if "@" in emailCarona and emailCarona.endswith(".com"):
                    emailV = True
                else:
                    print("\nDigite um email correto. Certifique que contem '@' e termine com '.com'")

            if emailCarona != emailLog:
                reserva = False
                valido = False
                dataCarona = input("\nEm qual dia, mês e ano (dd/mm/aaaa)? ")
                while valido == False:
                    dia = int(dataCarona[0:2])
                    mes = int(dataCarona[3:5])
                    ano = int(dataCarona[6:10])
                    if ano >= 2025:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            if dia >=1 and dia <=31:
                                valido = True
                        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                            if dia >=1 and dia <=30:
                                valido = True
                        elif mes == 2:
                            if dia >=1 and dia <=29:
                                valido = True
                    else:
                        print("\nDigite uma data válida!\n")
                        dataCarona = input("\nEm qual dia, mês e ano (dd/mm/aaaa)? ")
                validoH = False
                horaCarona = input("\nQual horario de partida? ")
                while validoH == False:
                    h = int(horaCarona[0:2])
                    m = int(horaCarona[3:5])
                    if h <= 23 and h >= 0:
                        if m <= 60 and m >= 0:
                            validoH = True
                    else:
                        print("\nDigite um hora valida!\n")
                        horaCarona = input("\nQual horario de partida? ")

                for c in caronas:
                    if c.get('emailMot') == emailCarona and c.get('data') == dataCarona and c.get('hora') == horaCarona:
                        if c['vagas'] > 0:
                            if c.get('valor') <= saldo:
                                reserva = True
                                saldo -= c['valor']
                                c['passageiros'].append(nomeLog)
                                c['vagas'] -= 1
                                for d in usuarios:
                                    if emailLog == d.get('email'):
                                        d['carteira'] -= c['valor']
                                print("\nReserva realizada!\n")
                                break
                if reserva == False:
                    print("\nDigite uma carona disponivel! Tente novamente.")
                        
            else:
                print("\nVocê não pode reservar sua propria carona! Tente novamente.")

        elif opcao == "5":
            reserva = False
            for r in caronas:
                if nomeLog in r['passageiros']:
                    reserva = True
                    print("\nPara cancelar uma carona, informe:\n")
                    
                    valido = False
                    data = input("\nDigite a data da sua carona reservada: ")
                    while valido == False:
                        dia = int(data[0:2])
                        mes = int(data[3:5])
                        ano = int(data[6:10])
                        
                        if ano >= 2025:
                            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                                if dia >=1 and dia <=31:
                                    valido = True
                            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                                if dia >=1 and dia <=30:
                                    valido = True
                            elif mes == 2:
                                if dia >=1 and dia <=29:
                                    valido = True
                        else:
                            print("\nDigite uma data válida!\n")
                            data = input("\nDigite a data da sua carona reservada: ")
                    
                    validoH = False
                    hora = input("\nDigite o horario da sua carona reservada: ")
                    while validoH == False:
                        h = int(hora[0:2])
                        m = int(hora[3:5])
                        if h <= 23 and h >= 0:
                            if m <= 60 and m >= 0:
                                validoH = True
                        else:
                            print("\nDigite um hora valida!\n")
                            hora = input("\nDigite o horario da sua carona reservada: ")

                    if r.get('data') == data and r.get('hora') == hora:
                        r['passageiros'].remove(nomeLog)
                        r['vagas'] += 1
                        valorVaga = r['valor']
                        for d in usuarios:
                            if emailLog == d.get('email'):
                                d['carteira'] += valorVaga
                        print("\nReserva cancelada com sucesso!\n")
                        break
                    else:
                        print("\nDigite uma reserva válida.\n")
                        break

            if reserva == False:
                print("\nVocê não possui reservas.\n")

        elif opcao == "6":
            reserva = False
            for r in caronas:
                if emailLog == r.get('emailMot'):
                    reserva = True
                    print("\nPara remover uma carona, informe: ")
                    valido = False
                    data = input("\nDigite a data da sua carona reservada: ")
                    while valido == False:
                        dia = int(data[0:2])
                        mes = int(data[3:5])
                        ano = int(data[6:10])
                        
                        if ano >= 2025:
                            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                                if dia >=1 and dia <=31:
                                    valido = True
                            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                                if dia >=1 and dia <=30:
                                    valido = True
                            elif mes == 2:
                                if dia >=1 and dia <=29:
                                    valido = True
                        else:
                            print("\nDigite uma data válida!\n")
                            data = input("\nDigite a data da sua carona reservada: ")
                    
                    validoH = False
                    hora = input("\nDigite o horario da sua carona reservada: ")
                    while validoH == False:
                        h = int(hora[0:2])
                        m = int(hora[3:5])
                        if h <= 23 and h >= 0:
                            if m <= 60 and m >= 0:
                                validoH = True
                        else:
                            print("\nDigite um hora valida!\n")
                            hora = input("\nDigite o horario da sua carona reservada: ")

                    for c, valor in enumerate(caronas):
                        if valor['emailMot'] == emailLog and valor['data'] == data and valor['hora'] == hora:
                            del caronas[c]
                            print("\nCarona deletada!\n")
                            break
                        else:
                            print("\nDigite uma carona valída! Tente novamente.\n")
            if reserva == False:
                print("\nVocê não possui caronas cadastradas.\n")
                        
        elif opcao == "7":
            print("\nPara ver os detalhes de uma carona especifica, digite:\n")
            busc = False
            email = input("\nDigite o email do Motorista: ").lower()
            valido = False
            data = input("\nDigite a data da carona: ")
            while valido == False:
                dia = int(data[0:2])
                mes = int(data[3:5])
                ano = int(data[6:10])
                    
                if ano >= 2025:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            if dia >=1 and dia <=31:
                                valido = True
                        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                            if dia >=1 and dia <=30:
                                valido = True
                        elif mes == 2:
                            if dia >=1 and dia <=29:
                                valido = True
                else:
                    print("\nDigite uma data válida!\n")
                    data = input("\nDigite a data da carona: ")
                    
                validoH = False
                hora = input("\nDigite o horario da carona: ")
                while validoH == False:
                    h = int(hora[0:2])
                    m = int(hora[3:5])
                    if h <= 23 and h >= 0:
                        if m <= 60 and m >= 0:
                            validoH = True
                    else:
                        print("\nDigite um hora valida!\n")
                        hora = input("\nDigite o horario da carona: ")
            print("\n")
            for busca in caronas:
                if busca.get('emailMot') == email and busca.get('data') == data and busca.get('hora') == hora:
                    print(f"Detalhe da carona: {busca['data']}, {busca['hora']}")
                    busc = True
                    print("-" * 20)
                    print("Motorista: ", busca['motorista'])
                    print("Email do Motorista: ", busca['emailMot'])
                    print("Origem: ", busca['origem'])
                    print("Destino: ", busca['destino'])
                    print("Data: ", busca['data'])
                    print("Horario: ", busca['hora'])
                    print("Vagas: ", busca['vagas'])
                    print("Valor por vaga: ", busca['valor'])
                    print("Passageiros: ")
                    for p in busca['passageiros']:
                        print(p)
                    print("-" * 20)
            if busc == False:
                print("\nDigite uma carona valída! Tente novamente.\n")

        elif opcao == "8":
            busc = False
            for usua in usuarios:
                if usua.get('email') == emailLog:
                    print(f"Caronas do usuario: {usua['nome']}")
                    for busca in caronas:
                        if busca.get('motorista') == nomeLog:
                            busc = True
                            print("-" * 20)
                            print("Motorista: ", busca['motorista'])
                            print("Email do Motorista: ", busca['emailMot'])
                            print("Origem: ", busca['origem'])
                            print("Destino: ", busca['destino'])
                            print("Data: ", busca['data'])
                            print("Horario: ", busca['hora'])
                            print("Vagas: ", busca['vagas'])
                            print("Valor por vaga: ", busca['valor'])
                            print("-" * 20)
                    if busc == False:
                        print("\nVocê não cadastrou nenhuma carona!\n")

        elif opcao == "9":
            dinheV = False
            
            while dinheV == False:
                print("\nEste é o seu BlablaPay")
                dinheiro = float(input("Digite o valor que deseja depositar (Max. por deposito: R$100): "))
                if dinheiro >= 5 and dinheiro <= 100:
                    saldo += dinheiro
                    dinheV = True
                    for d in usuarios:
                        if emailLog == d.get('email'):
                            d['carteira'] += dinheiro
                    print("\nTransação feita com sucesso!\n")
                else:
                    print("\nDigite um valor entre 5 e 100! Tente novamente.")
    #Fim