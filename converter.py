def conversor():
        exit = False
        while not exit:
            print("Seja Bem vindo ao nosso conversor de centímetros para metros, e vice-versa")
            print("1. Metros para Centímetros")
            print("2. Centímetros para Metros")

            opt = int(input("Selecione a opção desejada: "))
            if 0 <= opt > 2:
                 print("Opção inválida, tente novamente")

            if opt == 1:
                meters = float(input("Digite o valor em metros: ")) * 100
                text_result1 = " centímetros"
                print(f"{meters}{text_result1}")
                
            if opt == 2:
                centimeters = float(input("Digite o valor em centímetros: ")) / 100
                text_result2 = " metros"
                print(f"{centimeters}{text_result2}")

            opt_message = int(input('Se deseja fazer outra operação digite 1, se deseja sair digite 2: ')) 
            if opt_message == 2:
                 exit = True
            elif 0 <= opt_message > 2:
                 print("Opção inválida, tente novamente")
            
            if opt_message == 1:
                conversor()
            if opt_message == 2:
                exit = True
                print("Até a próxima!")



conversor()