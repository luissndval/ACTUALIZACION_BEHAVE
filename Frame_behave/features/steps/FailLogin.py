from pages.Navegador import Funciones_driver
from configuration.config import Datatest
from pages.LoginPage import LoginPage
from behave import *
from pages.Navegador import Funciones_driver
from configuration.config import Datatest
from pages.report_allure import Funciones_report
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import  AttachmentType

# Se ejecuta en LoginFail para validar popup de credenciales incorrectas
@then(u'Validar pop up de credenciales incorrectas')
def step_impl(context):
    try:
        LoginPage.ValidacionCredencialesIncorrectas(context)
        context.driver.close()
    except:
        # context.driver.close()
        assert False, "La prueba fallo en: Validar pop up de credenciales incorrectas"
