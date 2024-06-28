Feature: Visualización de Detalles de la Oferta

  Scenario: Ver detalles de una oferta de empleo
    Given que estoy en la página de resultados de búsqueda de empleo
    When hago clic en una oferta de empleo
    Then debería ser redirigido a la página de detalles de la oferta
    And debería ver el título, descripción, requisitos y detalles de la empresa

