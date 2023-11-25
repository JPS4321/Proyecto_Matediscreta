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

#Alfabeto
alfabeto_dict = {}
letra = 'a'
valor = 0

#Crear el alfabeto
for i in range(26):
    alfabeto_dict[letra] = valor
    letra = chr(ord(letra) + 1)  # Incrementa la letra
    valor += 1

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

#Funcion para verificar si es Primo
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

# Funcion para cambiar letras a numeros
def letra_a_numero(letra):
    return alfabeto_dict[letra]

#Encriptador
def encripter():
    doubleprime = False
    maxcomdiv = False
    p = 0
    q = 0
    print(" \n***ENCRIPTADOR*** \n")
    #Mensaje
    mensaje = input("Ingrese el mensaje a encriptar:")
    mensaje = mensaje.replace(" ", "").lower()
    sizemen = (len(mensaje))%2
    if (sizemen == 1):
        mensaje = ''.join([mensaje, "h"])
    
    lista_mensaje = [caracter for caracter in mensaje]
    lista_numeros = []
    
    for caracter in lista_mensaje:
        if caracter in alfabeto_dict:
            lista_numeros.append(str(letra_a_numero(caracter)))
            
    lista_bloques = []
         
    for i in range(0, len(lista_numeros), 2):
        bloque = ""
        if (len(lista_numeros[i+1]) < 2):
            lista_numeros[i+1] = "0" + lista_numeros[i+1]
        bloque = lista_numeros[i] + lista_numeros[i+1]
        lista_bloques.append(bloque)
        
    lista_bloques_num = []
    
    for bloque in lista_bloques:
        lista_bloques_num.append(int(bloque))
        
    # p & q 
    print("\nIngrese 2 números primos para la llave pública")
    while doubleprime == False:
        p = int(input("Ingrese el primer número primo:"))
        q = int(input("Ingrese el segundo número primo:"))
        if (es_primo(p) == True & es_primo(q) == True):
            print("\n*NÚMEROS APROBADOS*\n")
            doubleprime = True
        else:
            if (es_primo(p) == True and es_primo(q) == False):
                print( "\n-" + str(q) + " no es primo. Vuelva a Intentarlo-\n")
            elif (es_primo(q) == True and es_primo(p) == False):
                print("\n-" + str(p) + " no es primo. Vuelva a Intentarlo-\n")
            else:
                print("\n-Ambos no son primos. Vuelva a Intentarlo-\n")
    # n & phi
    n = p*q   
    phi = (p-1)*(q-1) 
    # e 
    print("\nIngrese un número positivo que tenga como MCD '1' con este número: " + str(phi))
    while maxcomdiv == False:
        e = int(input(""))
        mcd = math.gcd(phi,int(e))
        if(mcd != 1):
            print("El número ingresado no tiene 1 como MCD con " + str(phi) +". Vuelva a Intentarlo\n")
        else:
            print("\n*NÚMERO APROBADO*\n")
            maxcomdiv = True
            
    lista_mensaje_prefinal = []
    #Encriptacion
    for bloque in lista_bloques_num:
        bloque = bloque**e
        bloque = bloque % n
        lista_mensaje_prefinal.append(int(bloque))

    lista_mensaje_final = []
    
    for bloque in lista_mensaje_prefinal:
        valor = str(bloque)
        if (len(valor) < 4):
            valor = "0" + valor
        lista_mensaje_final.append(valor)
    
    print("Mensaje Encriptrado")
    for bloque in lista_mensaje_final:
        print(bloque + " ", end='')
    
    print("\n")
    
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