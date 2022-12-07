from pages.Navegador import Funciones_driver
from configuration.config import Datatest
from pages.LoginPage import LoginPage
from behave import *


@given(u'Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"')
def step_impl(context):
    try:
        LoginPage.OpenBrowser(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Iniciando Navegador"

@when(u'Escribiendo campo CUIT "{cuit}"')
def step_impl(context, cuit):
    try:
        LoginPage.InputCuit(context, cuit)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Escribiendo campo CUIT '{cuit}' "

@when(u'Escribiendo password "{password}"')
def step_impl(context, password):
    try:
        LoginPage.InputPassword(context, password)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Escribiendo password '{password}' "

@when(u'Click en boton ingresar')
def step_impl(context):
    try:
        LoginPage.ClickIngresar(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en boton ingresar"


@when(u'validar Inicio Sesion')
def step_impl(context):
    try:
        LoginPage.ValidacionInicioSesion(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: validar Inicio Sesion "

# Se ejecuta cuando inicia sesion OK
@then(u'Click en cerrar sesion')
def step_impl(context):
    try:
        LoginPage.CerrarSesion(context)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "La prueba fallo en: Click en cerrar sesion"

