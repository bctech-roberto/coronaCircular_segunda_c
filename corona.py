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
    op = int(input("deseac continuar SI=1/NO=0: "))
    if(op==0):
        break
print("Vsitanos en www.bctech.com")
