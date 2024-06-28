from selenium.webdriver.common.by import By

class ResultadosEmpleoPage:
    def __init__(self, driver):
        self.driver = driver

    def obtener_texto_resultados(self):
        resultados = self.driver.find_elements(By.XPATH, "//div[@class='is-style-card-default wp-block-webfactory-card']/div/a")
        textos_enlaces = []
        for resultado in resultados:
            texto_enlace = resultado.text.strip()
            textos_enlaces.append(texto_enlace)
        return textos_enlaces
