from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self, url):
        self.driver.get(url)
        try:
            boton_cookies = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class= 'tarteaucitronCTAButton tarteaucitronAllow']"))
            )
            boton_cookies.click()
        except:
            print("No se encontró el pop-up de cookies, continuando sin hacer clic en el botón de cookies.")


    def ingresar_palabra_clave(self, palabra_clave):
        campo_busqueda = self.driver.find_element(By.XPATH, "//input[@class='form-control pe-5 text-uppercase']")
        campo_busqueda.clear()
        campo_busqueda.send_keys(palabra_clave)

    def hacer_clic_en_buscar(self):
        boton_buscar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class= 'btn wp-block-button__link']")))
        boton_buscar.click()
        self.driver.execute_script("window.scrollTo(0, 500)")

    def hacer_clic_en_oferta(self):
        oferta = self.driver.find_element(By.XPATH,"//a[@class= 'card-title order-0 col-11 col-md-6 px-1  px-md-2 py-2 text-decoration-none h-md-100 d-flex align-items-center']")
        oferta.click()



