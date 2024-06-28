Feature: Búsqueda de empleo por palabra clave

Scenario: Realizar una búsqueda de empleo por palabra clave
    Given que estoy en la página de búsqueda de empleo
    When ingreso la palabra clave "java" en el campo de búsqueda
    And hago clic en el botón de buscar
    Then debería ver una lista de ofertas de empleo que contienen la palabra clave "java"

