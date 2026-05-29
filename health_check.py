#!/usr/bin/env python3
import sys
import os
import csv
import requests
from datetime import datetime

# Códigos de color ANSI para la consola
RED = "\033[91m"
RESET = "\033[0m"

def check_health(urls_list):
    csv_file = "health_report.csv"
    file_exists = os.path.isfile(csv_file)
    
    # Abrir archivo CSV en modo append
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir cabecera si el archivo es nuevo
        if not file_exists:
            writer.writerow(["timestamp", "url", "status_code", "response_time_ms", "estado"])
        
        for url in urls_list:
            url = url.strip()
            if not url:
                continue
                
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                # Realizar GET HTTP con timeout estricto de 5 segundos
                start_time = datetime.now()
                response = requests.get(url, timeout=5.0)
                end_time = datetime.now()
                
                # Calcular el tiempo de respuesta en milisegundos
                response_time = int((end_time - start_time).total_seconds() * 1000)
                status_code = response.status_code
                
                # Definir estado según el código HTTP devuelto (2xx o 3xx se consideran UP)
                if 200 <= status_code < 400:
                    estado = "UP"
                    print(f"[{timestamp}] {url} -> Status: {status_code} | Time: {response_time}ms | Estado: {estado}")
                else:
                    estado = "DOWN"
                    # Imprimir en rojo en consola si algún servicio está caído
                    print(f"{RED}[{timestamp}] {url} -> Status: {status_code} | Time: {response_time}ms | Estado: {estado}{RESET}")
                    
            except requests.exceptions.Timeout:
                # Manejar timeout de 5 segundos sin terminar abruptamente
                status_code = "TIMEOUT"
                response_time = 5000
                estado = "DOWN"
                print(f"{RED}[{timestamp}] {url} -> Error: Connection Timeout (5s exceeded) | Estado: {estado}{RESET}")
                
            except requests.exceptions.RequestException as e:
                # Manejar cualquier otro error de red (DNS inválido, conexión rechazada, etc.)
                status_code = "ERROR"
                response_time = 0
                estado = "DOWN"
                print(f"{RED}[{timestamp}] {url} -> Error de conexión: {e} | Estado: {estado}{RESET}")
            
            # Guardar en el archivo CSV: timestamp, url, status_code, response_time_ms, estado
            writer.writerow([timestamp, url, status_code, response_time, estado])

def main():
    if len(sys.argv) < 2:
        print("Uso correcto:")
        print("  python3 health_check.py <url1> <url2> ...")
        print("  python3 health_check.py <archivo_con_urls.txt>")
        sys.exit(1)
        
    target_input = sys.argv[1]
    urls = []
    
    # Comprobar si el argumento recibido corresponde a un archivo de texto en disco
    if os.path.isfile(target_input):
        with open(target_input, 'r') as f:
            urls = f.readlines()
    else:
        # Interpretar la lista de argumentos como URLs desde la consola
        urls = sys.argv[1:]
        
    check_health(urls)

if __name__ == "__main__":
    main()
