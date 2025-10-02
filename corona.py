while(True):
    print("Hecho por RObertito BC")
    print("=====================")
    print("Cornoa cicular")
    print("======================")
    radio_mayor = float(input("radio mayor: "))
    radio_menor = float(input("radio menor: "))
    area = 3.14*(radio_mayor**2 - radio_menor**2)
    peri = 2*3.14*(radio_mayor + radio_menor)
    print()
    print("resultaos")
    print("Area ; ",area.__round__(2))
    print("Peru : ",peri.__round__(2))
    print()
    while(True):
        try:
            op = int(input("deseac continuar SI=1/NO=0: "))
            if(op==0 or op==1):
                break
            else:
                print("solo ingresa 1 o 0")
        except:
            print("no letras")
    if(op==0):
        break
print("Ud a teminado el sistem")
print("Vsitanos en www.bctech.com")
