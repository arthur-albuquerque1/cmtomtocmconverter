def conversor():
        exit = False
        while not exit:
            print("Seja Bem vindo ao nosso conversor de centímetros para metros, e vice-versa")
            print("1. Metros para centímetros")
            print("2. Centímetros para metros")
            print("3. Metros para milímetros")

            opt = int(input("Selecione a opção desejada: "))
            if 0 <= opt > 3:
                 print("Opção inválida, tente novamente")

            elif opt == 1:
                meters = float(input("Digite o valor em metros: ")) * 100
                print(f'{meters} centímetros')
                
            elif opt == 2:
                centimeters = float(input("Digite o valor em centímetros: ")) / 100
                print(f'{centimeters} metros')
            elif opt == 3:
                meters = float(input("Digite o valor em metros: ")) * 1000
                print(f'{meters} milímetros')

            opt_message = int(input('Se deseja fazer outra operação digite 1, se deseja sair digite 2: ')) 

            def exit():
                 global exit
                 exit = True
                 print("Até a próxima!")

            if opt_message == 2:
                 exit()
            elif 0 <= opt_message > 2:
                 print("Opção inválida, tente novamente")
            elif opt_message == 1:
                conversor()
            elif opt_message == 2:
                exit()



conversor()
