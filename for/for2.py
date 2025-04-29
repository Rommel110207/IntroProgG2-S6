#Leer un numero Ingresado por el usuario
#Mostrar la letra a por cada numero del 1 al numero
#Ingresado por el usuario ejemplo, numero: 3
#a
#aa
#aaa


def mostrar_letras(numero):
    for i in range(1,numero+1):
        print(f"a"*i)
        
def main():
    numero = int(input("Ingrese un numero: "))
    mostrar_letras(numero)
    
    
main()      