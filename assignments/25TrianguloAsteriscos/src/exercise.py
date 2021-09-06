def main():
    #escribe tu código abajo de esta línea
    altura=int(input("Enter triangle height: "))
    for i in range(1,altura+1):
        print((altura-i)*" "+"*"*i)
if __name__=='__main__':
    main()