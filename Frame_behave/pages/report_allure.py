import allure
from allure_commons.types import AttachmentType

### EJECUTAR EL SERVIDOR ALLURE CON EL SIGUIENTE COMANDO:
### allure serve .\ruta del reporte\

class Funciones_report():
    def __init__(self, driver):
        self.driver = driver

    def captura_pantalla(self, nombre):
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)
