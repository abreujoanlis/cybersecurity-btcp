def cifrado_cesar(texto, desplazamiento, modo):
    resultado = ""
    
    # Si el modo es descifrar, invertimos el desplazamiento
    if modo == 'descifrar':
        desplazamiento = -desplazamiento

    for caracter in texto:
        # Procesar letras mayúsculas
        if caracter.isupper():
            # Formula: (Posición en el abecedario + desplazamiento) % 26 + Código ASCII de 'A'
            nuevo_caracter = chr((ord(caracter) - 65 + desplazamiento) % 26 + 65)
            resultado += nuevo_caracter
        # Procesar letras minúsculas
        elif caracter.islower():
            # Formula: (Posición en el abecedario + desplazamiento) % 26 + Código ASCII de 'a'
            nuevo_caracter = chr((ord(caracter) - 97 + desplazamiento) % 26 + 97)
            resultado += nuevo_caracter
        else:
            # Si no es una letra (espacios, números, signos), se queda igual
            resultado += caracter
            
    return resultado

def menu():
    while True:
        print("\n--- CIFRADO CÉSAR ---")
        print("1. Cifrar un texto")
        print("2. Descifrar un texto")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '3':
            print("¡Hasta luego!")
            break
            
        if opcion in ['1', '2']:
            texto_usuario = input("\nIntroduce el texto: ")
            
            # Validación para asegurar que la clave sea un número entero
            while True:
                try:
                    clave = int(input("Introduce el número de desplazamiento (clave): "))
                    break
                except ValueError:
                    print("Por favor, introduce un número entero válido.")
            
            if opcion == '1':
                texto_final = cifrado_cesar(texto_usuario, clave, 'cifrar')
                print(f"\nTexto cifrado: {texto_final}")
            else:
                texto_final = cifrado_cesar(texto_usuario, clave, 'descifrar')
                print(f"\nTexto descifrado: {texto_final}")
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()