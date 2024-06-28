import time
from behave import *
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.utils import *
import traceback

@given('que estoy en la página de resultados de búsqueda de empleo')
def abrir_pagina_resultados(context):
    context.base_page = BasePage(context.driver)
    context.base_page.abrir_pagina('https://www.alten.es/unete-a-alten/empleo/?job_search=diseñador&pagenum=1&per_page=25')
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)
    tomar_captura_pantalla(context.driver,"pagina_resultados_empleo", context.feature.name, context.scenario.name)

@when('hago clic en una oferta de empleo')
def hacer_clic_en_oferta(context):
    context.base_page.hacer_clic_en_oferta()

@then('debería ser redirigido a la página de detalles de la oferta')
def verificar_redireccion_detalles(context):
    time.sleep(3)
    xpath_compartir = "//div[@class = 'mb-4 wp-block-webfactory-share']"
    compartir = context.driver.find_element(By.XPATH, xpath_compartir)
    context.driver.execute_script("window.scrollTo(0, 400)")
    assert compartir.is_displayed(), "No se encontró el elemento compartir"


@then('debería ver el título, descripción, requisitos y detalles de la empresa')
def verificar_contenido_oferta(context):
    time.sleep(3)
    titulo_oferta = context.driver.find_element(By.XPATH, "//h2[@class='is-style-subsection-title my-5 wp-block-post-title']")
    context.driver.execute_script("window.scrollTo(0, 1500)")
    tomar_captura_pantalla(context.driver, "detalle_oferta", context.feature.name, context.scenario.name)
    descripcion_oferta = context.driver.find_element(By.XPATH, "//div[@class='block--inner']")
    ofertas_similares = context.driver.find_element(By.CSS_SELECTOR, "h4.is-style-selection-title")

    try:
        time.sleep(3)
        assert "Diseñador" in titulo_oferta.text, "El título de la oferta no es el esperado"
        assert "Formamos parte de ALTEN" in descripcion_oferta.text, "La descripción de la oferta no contiene el texto esperado"
        assert "OFERTAS SIMILARES" in ofertas_similares.text, "La oferta no contiene el texto esperado"

        nombre_prueba = "Ver detalles oferta"
        resultado_prueba = "exitoso"
        descripcion_error = ""

    except AssertionError as e:
        nombre_prueba = "Ver detalles oferta"
        resultado_prueba = "fallido"
        descripcion_error = str(e)
        context.failed = True
        raise e

    except Exception as e:
        nombre_prueba = "Ver detalles oferta"
        resultado_prueba = "fallido"
        descripcion_error = "Error inesperado: " + str(e) + "\n" + traceback.format_exc()
        context.failed = True
        raise e

    finally:
        escribir_resultado_csv(nombre_prueba, resultado_prueba, descripcion_error)

    print("Verificación detalle de empleo completada.")

