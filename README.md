# IDEAM_WebScraping

This repository contains files with Python-code used to download hydroclimate data from the IDEAM (Instituto de Hidrología, Meteorología y Estudios Ambientales), Colombia. The following gives a brief description of the individual files and how to use them.

## Functions
La única función a correr es MainIDEAM.py

MainIDEAM.py     : 

IDEAM_extract.py :

## Required files
- **A WebDriver**: to drive a browser natively. This tool allow us automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. Be sure to download the version that is compatible with your browser.

  * For Chrome click [here](https://chromedriver.chromium.org/home).
  * For Mozilla click [here](https://firefox-source-docs.mozilla.org/testing/geckodriver/).
 
 **NOTE:** these functions are written to work with Chrome. In case of using another browser, it is necessary to change the specifications of the following lines in the IDEAM_extract.py function:
 
  * Line 23    : change the WebDriver's name (**from** chrome_path = r"C:\path of the\chromedriver.exe" **to** *Firefox_path = r"C:\path of the\geckodriver.exe"*, for example)
  * Lines 26-30: **from** chrome_options **to** Firefox_options
  * Line 54    : **from** driver = webdriver.Chrome(chrome_path, chrome_options = chrome_options) **to** driver = webdriver.Firefox(Firefox_path, options=Firefox_options)
 
- **An Excel file** with the following columns:

 | **CODIGO** | **DEPARTAMENTO** | **MUNICIPIO** |
 | -------| ------------ |-----------|
 | Conten |    Conten    |   Conten  | 

The input document extension must be in xls or xlsx. The file name must follows the format: **DD-MM-YYYYY_DD-MM-YYYYY_VARIABLE_Description.xls**.

      Example: 16-02-2020_17-02-2020_PRECIPITACION_Día pluviométrico.xls
      * Start date: 16-02-2020
      * End date: 17-02-2020
      * Variable: PRECIPITACION
      * Description: Día pluviométrico

All the information on the web site is in Spanish, be sure to write correctly the variable names and their description. Otherwise, the program will display an error. Each piece of information contained in the file name must be separated by an underline ( _ ). This file does not necessarily have to be in the same folder as the functions. 

Below are some variables with their descriptions. If you are interested in other variables, you can visit the [IDEAM](http://dhime.ideam.gov.co/atencionciudadano/) website and check the different options. 

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
