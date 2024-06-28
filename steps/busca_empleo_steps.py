import time
from behave import *
from pages.base_page import BasePage
from pages.resultados_empleo_page import ResultadosEmpleoPage
from utils.utils import *
import traceback

@given('que estoy en la página de búsqueda de empleo')
def abrir_pagina_busqueda(context):
    context.base_page = BasePage(context.driver)
    context.base_page.abrir_pagina('https://www.alten.es/unete-a-alten/empleo/')
    tomar_captura_pantalla(context.driver, "pagina_busqueda_empleo", context.feature.name, context.scenario.name)

@when('ingreso la palabra clave "{palabra_clave}" en el campo de búsqueda')
def ingresar_palabra_clave(context, palabra_clave):
    context.base_page.ingresar_palabra_clave(palabra_clave)
    tomar_captura_pantalla(context.driver, "ingresar_palabra_clave", context.feature.name, context.scenario.name)

@when('hago clic en el botón de buscar')
def hacer_clic_en_buscar(context):
    context.base_page.hacer_clic_en_buscar()
    time.sleep((5))

@then('debería ver una lista de ofertas de empleo que contienen la palabra clave "{palabra_clave}"')
def verificar_resultados(context, palabra_clave):
   tomar_captura_pantalla(context.driver, "lista_ofertas_empleo", context.feature.name, context.scenario.name)
   resultados_page = ResultadosEmpleoPage(context.driver)
   textos_enlaces = resultados_page.obtener_texto_resultados()
   print(f"\nTotal de textos encontrados: {len(textos_enlaces)}")

   try:
       for texto in textos_enlaces:
           print(f"\nVerificando texto: {texto}")
           assert palabra_clave.lower() in texto.lower(), f"La palabra clave '{palabra_clave}' no está presente en el texto '{texto}'"
           print(f"La palabra clave '{palabra_clave}' está presente en el texto '{texto}'")

       nombre_prueba = "Búsqueda de empleo por palabra clave"
       resultado_prueba = "exitoso"
       descripcion_error = ""

   except AssertionError as e:
       nombre_prueba = "Búsqueda de empleo por palabra clave"
       resultado_prueba = "fallido"
       descripcion_error = str(e)
       context.failed = True
       raise e

   except Exception as e:
       nombre_prueba = "Búsqueda de empleo por palabra clave"
       resultado_prueba = "fallido"
       descripcion_error = "Error inesperado: " + str(e) + "\n" + traceback.format_exc()
       context.failed = True
       raise e

   finally:
       escribir_resultado_csv(nombre_prueba, resultado_prueba, descripcion_error)

   print("Verificación busqueda de empleo completada.")



