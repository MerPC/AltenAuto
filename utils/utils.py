import csv
import os
from datetime import datetime

def escribir_resultado_csv(nombre_prueba, resultado, descripcion_error=""):

    archivo_csv = 'reports/test_results.csv'
    fecha_hora_ejecucion = datetime.now().strftime("%d-%m-%Y %H:%M")

    if not os.path.exists('reports'):
        os.makedirs('reports')

    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Nombre de la Prueba", "Resultado", "Descripción del Error","Fecha y Hora de Ejecución"])
        writer.writerow([nombre_prueba, resultado, descripcion_error, fecha_hora_ejecucion])

def crear_carpeta_con_timestamp(base_carpeta="reports/screenshots"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    carpeta_con_timestamp = os.path.join(base_carpeta, timestamp)

    if not os.path.exists(carpeta_con_timestamp):
        os.makedirs(carpeta_con_timestamp)
    return carpeta_con_timestamp

def tomar_captura_pantalla(driver, nombre_archivo, feature_name, scenario_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    carpeta_base = crear_carpeta_con_timestamp()
    carpeta_feature = os.path.join(carpeta_base, feature_name)

    if not os.path.exists(carpeta_feature):
        os.makedirs(carpeta_feature)
    carpeta_escenario = os.path.join(carpeta_feature, scenario_name)
    if not os.path.exists(carpeta_escenario):
        os.makedirs(carpeta_escenario)

    nombre_completo = f"{nombre_archivo}_{timestamp}.png"
    ruta_completa = os.path.join(carpeta_escenario, nombre_completo)
    driver.save_screenshot(ruta_completa)



