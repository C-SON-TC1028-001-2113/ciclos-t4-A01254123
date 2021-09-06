def main():
    numero1=int(input("Valor 1: "))
    numero2=int(input("Valor 2: "))
    if numero1>0 and numero2>0:
        if numero1!=numero2:   
            if numero1>numero2:
                for i in range(numero2,numero1+1):
                    if i%2==0:
                        print(i)
            elif numero1<numero2:
                for i in range(numero1,numero2+1):
                    if i%2==0:
                        print(i)
        else:
            print("No hay pares")
if __name__=='__main__':
    main()