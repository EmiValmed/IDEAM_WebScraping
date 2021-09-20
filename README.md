# IDEAM_WebScraping

This repository contains files with Python-code used to web scrapping hydroclimate data from the IDEAM (Instituto de Hidrología, Meteorología y Estudios Ambientales), Colombia. The following gives a brief description of the individual files and how to use them.

# Required files
- A WebDriver: to drive a browser natively. This tool allow us automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. Be sure to download the version that is compatible with your browser.
  * For chrome visit : https://chromedriver.chromium.org/home
  * For Mozilla visit: https://firefox-source-docs.mozilla.org/testing/geckodriver/
- An Excel files with the following columns:

 | CODIGO | DEPARTAMENTO | MUNICIPIO |
 | -------| ------------ |-----------|
 | Conten |    Conten    |   Conten  | 


# Functions
La única función a correr es MainIDEAM.py

MainIDEAM.py     : 

IDEAM_extract.py :

# Inputs
El docuemnto de entrada debe ser extensión xls,xlsx y csv separado por coma. el nombre del archivo debe contener la fecha de inicio, la fecha final, la variable de interés y la descrición del mismo.

DD-MM-YYYY_DD-MM-YYYY_VARIABLE_Description.xls


A continuación las variablescon cada una de las descripciones existentes en el sitio web. Nota: es importante que la variable y la descripción estén escritas tal y como se indica en la lista, de lo contrario provocaría un error. 


# Variables and description
* CAUDAL
  * Caudal máximo diario
  * Caudal medio diario
  * Caudal mínimo diario
  * Caudal máximo mensual
  * Caudal medio mensual
  * Caudal mínimo mensual
  * Caudal máximo anual
  * Caudal medio anual
  * Caudal mínimo anual
  
* EVAPORACION
  * Evaporación total diaria

* PRECIPITACION
  * Precipitación acumulada 10 minutos
  * Precipitación total horaria
  * Dias con lluvia >= 0,1 mm
  * Día pluviométrico
  * Precipitación total diaria

* TEMPERATURA
  * Temperatura máxima diaria
  * Temperatura mínima diaria





