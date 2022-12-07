@test2

Feature: Inicio de sesion con datos validos.
  Background:
    Given  Iniciando Navegador "turnera-frontend-administracion-app-turnera-pre-qa.apps.ocp4-dev.gcba.gob.ar/login"

    Scenario Outline: Se visualizan campos para iniciar sesion
      When Escribiendo campo CUIT "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      Then Validar pop up de credenciales incorrectas


      Examples:
        | cuit        | password |
        | 20957604081 | asdf     |
        | 23432002508 | asdf     |
        | 1111        | asdf     |
