#Leer dos numeros e imprimir los numeros entre ellos
def mostrar_numeros(numero1=0, numero2=0):
    if numero1 < numero2:
        for i in range(numero1, numero2+1):
            print(i)
    else:
        for i in range(numero2, numero1+1):
            print(i, end=" ")
            
def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    mostrar_numeros(numero1, numero2)
main()                
            