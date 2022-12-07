import time

from pages.Funciones import Funciones_epidata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from pages.ActionUi import ActionUI
from pages.Navegador import Funciones_driver
from configuration.config import Datatest
from pages.report_allure import Funciones_report
import unittest



t = 1


class LoginPage(Funciones_epidata):

    cuitField = "//input[contains(@id,'cuit')]"
    passwordField = "//input[contains(@id,'contrasena')]"
    btnIngresar = "//button[text()=Ingresar]"
    loginValidationField = "//h2[normalize-space()='Organismos']"
    btnCerrarSesion = "//a[@class='list-group-item list-group-item-logout logout-sm']"

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self):
        global navegador, fun, reporte
        navegador = Funciones_driver
        navegador.driver_Firefox(self, "C:\drivers\geckodriver.exe")
        fun = Funciones_epidata(self.driver)
        fun.Navegar(Datatest.URL, t)
        reporte = Funciones_report

    def InputCuit(self, cuit):
        fun.Input_Texto(By.XPATH, "//input[contains(@id,'cuit')]", cuit)

    def InputPassword(self, password):
        fun.Input_Texto(By.XPATH, "//input[contains(@id,'contrasena')]", password)

    def ClickIngresar(self):
        fun.Click_Field(By.CSS_SELECTOR, "button[type='submit']")

    def ValidacionInicioSesion(self):
        fun.validates(By.XPATH, "//h2[normalize-space()='Organismos']")

    def CerrarSesion(self):
        fun.Click_Field(By.XPATH, "//a[@class='list-group-item list-group-item-logout logout-sm']")

    def ValidacionCredencialesIncorrectas(self):

        element = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text

        val=  WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.toast-header"))).text

        if ( element == val ):

            print(f"se pudo Comparar : ------- { element } == { val } -------")
            fun.captura_pantalla("Captura")

        else:
            print(f"No se pudo validar el campo")

