import subprocess
import re
import os
import platform
from datetime import datetime

def obtener_nombres_perfiles():
    try:
        # Ejecutamos el comando y decodificamos con 'cp850' que es el estándar de la consola en Windows español
        salida = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode(errors="ignore", encoding="cp850")
        
        # Buscamos cualquier línea que tenga ":" y capturamos lo que sigue. 
        # Esto funciona en inglés (All User Profile : ...) y en español (Perfil de todos los usuarios : ...)
        perfiles = re.findall(r".*?:\s(.*)\r", salida)
        
        # Filtramos posibles líneas vacías o encabezados del comando
        return [p.strip() for p in perfiles if p.strip() != ""]
    except Exception as e:
        print(f"Error al obtener perfiles: {e}")
        return []

def extraer_datos_perfil(nombre):
    try:
        info_clave = subprocess.run(["netsh", "wlan", "show", "profile", nombre, "key=clear"], capture_output=True).stdout.decode(errors="ignore", encoding="cp850")
        
        # Buscamos la línea que contiene el contenido de la clave basándonos en la estructura, no en el idioma
        # En español suele ser "Contenido de la clave"
        lineas = info_clave.split('\n')
        busqueda_clave = None
        
        for linea in lineas:
            # Buscamos la línea que indica el contenido de la contraseña (Key Content / Contenido de la clave)
            if "Contenido de la clave" in linea or "Key Content" in linea:
                busqueda_clave = linea.split(":")[1].strip()
                break
        
        return {
            "nombre_red": nombre,
            "contrasena": busqueda_clave if busqueda_clave else "Abierta o No encontrada"
        }
    except Exception:
        return None

def guardar_en_txt(lista):
    try:
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usuario = os.getlogin()
        equipo = platform.node()
        nombre_archivo = f"redes_wifi_{equipo}.txt"
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"REPORTE DE REDES WIFI\n")
            archivo.write(f"Fecha: {ahora}\n")
            archivo.write(f"Equipo: {equipo}\n")
            archivo.write(f"Usuario: {usuario}\n")
            archivo.write("-" * 50 + "\n")
            
            lineas = map(lambda p: f"Red: {p['nombre_red']:25} | Contraseña: {p['contrasena']}\n", lista)
            archivo.writelines(lineas)
            
        print(f"Archivo '{nombre_archivo}' generado con éxito.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

nombres = obtener_nombres_perfiles()
# Filtramos nombres genéricos que netsh a veces devuelve como encabezados
nombres_limpios = [n for n in nombres if "Perfil" not in n and "Profile" not in n and "---" not in n]

lista_wifi = list(filter(None, map(extraer_datos_perfil, nombres_limpios)))

if lista_wifi:
    guardar_en_txt(lista_wifi)
    [print(f"Red: {p['nombre_red']:25} | Contraseña: {p['contrasena']}") for p in lista_wifi]
else:
    print("No se encontraron redes. Verifica si el sistema tiene perfiles WiFi guardados.")