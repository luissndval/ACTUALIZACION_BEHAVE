
Feature: Inicio de sesion con datos validos.
  Background:
    Given  Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

    Scenario Outline: Se visualizan campos para iniciar sesion
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      When validar Inicio Sesion
      Then Click en cerrar sesion


       Examples:
      |cuit|password|
      |27395625123|Troquel1|
