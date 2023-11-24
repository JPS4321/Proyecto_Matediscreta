#-------------------------------------------------------------
# Proyecto Matemática Discreta
# Encriptador y Desencriptador RSA
# Diego Duarte 22075
# Juan Pablo Solis 22102
# Fecha de creación: 6/11/2023
# Última modificación: 
# Versión: 1
# -----------------------------------------------------------
import math

#Funcion que maneja logica de decriptacion
def Decriptador(cipher_blocks, n, d):
    decrypted_blocks = [pow(c, d, n) for c in cipher_blocks]
    decrypted_message = ''.join(chr((block // 100) + ord('A')) + chr((block % 100) + ord('A')) for block in decrypted_blocks)
    return decrypted_message
#Funcion para obtener el inverso modlar
def inverso_modular(a, m):
    g, x, y = algoritmo_Euclides(a, m)
    if g != 1:
        raise Exception('Inverso modular no existe para %d mod %d' % (a, m))
    else:
        return x % m
#Funcionl la cual realiza el algoritmo de euclide
def algoritmo_Euclides(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = algoritmo_Euclides(b % a, a)
        return gcd, y - (b // a) * x, x
#Funcion para obtener el valor de phi
def encontrar_phi(n):
    p, q = encontrar_factores(n)
    return (p - 1) * (q - 1)
#Funcion para obtener los factores de n
def encontrar_factores(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    raise Exception('Factores no encontrados para n=%d. Asegúrese de que n sea el producto de dos números primos.' % n)


#Primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False

    return True

#Encriptador
def encripter():
    doubleprime = False
    print(" \n ENCRIPTADOR \n")
    mensaje = input("Ingrese el mensaje a encriptar:")
    print("Ahora debe de ingresar 2 números primos")
    while doubleprime == False:
        p = int(input("Ingrese el primer número primo:"))
        q = int(input("Ingrese el primer número primo:"))
        if (es_primo(p) == True & es_primo(q) == True):
            print("Son Primos")
            doubleprime = True
        else:
            print("Ambos no son primos")
        
    e = input("")

#Desencriptador
def deencripter():
    try:
        input_cifrado = input("Ingrese el mensaje cifrado (números separados por espacios): ")
        Bloques_cifrado = [int(block) for block in input_cifrado.split()]
        n = int(input("Ingrese n: "))
        e = int(input("Ingrese e: "))
        phi = encontrar_phi(n)
        d = inverso_modular(e, phi)
        Mensaje = Decriptador(Bloques_cifrado, n, d)
        print(f"Mensaje Desencriptado: {Mensaje}")
        print(f"Clave Privada d: {d}")
    except ValueError:
        print("Error: Entrada no válida. Asegúrese de ingresar números enteros.")
    except Exception as ex:
        print(f"Error: {ex}")



    



#Menu Principal 
continuar = True
print("***Bienvenido al Encriptador y Desencriptador RSA*** \n")
while continuar:
    des = int(input("   ¿Qué desea hacer?  \n 1 Encriptar \n 2 Desencriptar \n 3 SALIR \n"))
    if (des == 1):
        encripter()
    elif (des == 2):
        deencripter()
    elif (des == 3):
        print("Gracias por usar el Encriptador y Desencriptador RSA")
    else:
        print("Eliga una opción válida")