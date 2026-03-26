@echo off
echo Escaneando red
ipconfig
netstat
ping 8.8.8.8
arp -a
netstat -an

echo Escaneo realizado
pause