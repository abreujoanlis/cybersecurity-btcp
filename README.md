Utilidad 

Verificar si tienes conexión a internet
	•	El comando ping 8.8.8.8 (servidor de Google) sirve como prueba directa.
	•	Si responde → tienes internet
	•	Si no responde → problema de red (router, ISP, cable, etc.)


Obtener tu configuración de red
	•	ipconfig muestra:
	•	Dirección IP
	•	Puerta de enlace (gateway)
	•	DNS


Ver conexiones y puertos activos
	•	netstat -a lista:
	•	Conexiones activas
	•	Puertos abiertos
	•	Servicios en escucha


Ahorro de tiempo (automatización)
En lugar de escribir 3 comandos manualmente:
	•	Ejecutas 1 solo archivo
	•	Obtienes todo el diagnóstico de una vez

Generar evidencia o reportes
Si usas la versión con .txt:
	•	Guarda resultados automáticamente
	•	Puedes enviarlo por WhatsApp, correo o soporte técnico






@echo off
echo ==============================
echo INFORME DE RED
echo ==============================

echo.
echo [1] CONFIGURACION IP:
ipconfig

echo.
echo [2] PRUEBA DE CONECTIVIDAD (PING 8.8.8.8):
ping 8.8.8.8

echo.
echo [3] CONEXIONES ACTIVAS (NETSTAT):
netstat -a

echo.
echo ==============================
echo FIN DEL INFORME
pause
