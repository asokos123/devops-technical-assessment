# DevOps Technical Assessment - Junior Engineer

Este repositorio contiene la resolución de la prueba técnica para el puesto de Ingeniero DevOps Junior.

## 🚀 Contenido del Repositorio

* `health_check.py`**: Script automatizado en Python para el chequeo de disponibilidad de URLs.
* `urls.txt`**: Archivo de texto plano que sirve como fuente de datos con los endpoints de prueba a evaluar.
* `health_report.csv`**: Reporte de auditoría generado automáticamente por el script con el formato requerido

📝 **Nota sobre las evidencias:** Las capturas de pantalla de la ejecución del script en la terminal, los resultados visuales en color rojo y las evidencias de infraestructura se encuentran adjuntas directamente en el documento de respuestas (Word/PDF) entregado por separado

---

## 🛠️ Instrucciones de Ejecución (Scripting)

El script de Health-Check requiere **Python 3** y la librería `requests`.

1. Instalación de dependencias
Para instalar la biblioteca de red necesaria, ejecuta en tu terminal:
pip install requests 

2. Ejecución leyendo desde el archivo de texto
O bien, puedes hacer que el script procese de forma masiva la lista guardada en el archivo urls.txt:
python health_check.py urls.txt
