# IDEAM_WebScraping :umbrella: :sunny: :cloud:

This repository contains files with Python-code used to download hydroclimate historical series from the [IDEAM](http://dhime.ideam.gov.co/atencionciudadano/) (Instituto de Hidrología, Meteorología y Estudios Ambientales), Colombia. The following gives a brief description of the individual files:

## Required files
- **A WebDriver**: to drive a browser natively. This tool allows us automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. Be sure to download the version that is compatible with your browser.

  * For Chrome click [here](https://chromedriver.chromium.org/home).
  * For Mozilla click [here](https://firefox-source-docs.mozilla.org/testing/geckodriver/).
 
   **NOTE:** the program is written to work with Chrome. In case of using another browser, it is necessary to change the specifications of the following lines in the **IDEAM_extract.py** function:
 
     * **Line 23**    : change the WebDriver's name (**from** "chromedriver.exe" **to** "geckodriver.exe", for example)
     * **Lines 26-30**: **from** chrome_options **to** Firefox_options
     * **Line 54**    : **from** driver = webdriver.**Chrome**(chrome_path, chrome_options = chrome_options) **to** driver = webdriver.**Firefox**(Firefox_path, options=Firefox_options)
 
- **An Excel file** with the following columns:

 | **CODIGO** | **DEPARTAMENTO** | **MUNICIPIO** |
 | -------| ------------ |-----------|
 | Conten |    Conten    |   Conten  | 

The input document extension must be in .xls or .xlsx. The file name must follows the format: **DD-MM-YYYYY_DD-MM-YYYYY_VARIABLE_Description.xls**.

      Example: 16-02-2020_17-02-2020_PRECIPITACION_Día pluviométrico.xls
      * Start date: 16-02-2020
      * End date: 17-02-2020
      * Variable: PRECIPITACION
      * Description: Día pluviométrico

**Important:**
 * This file does not necessarily have to be in the same folder as the functions.
 * All the information on the web site is in Spanish, be sure to write correctly the variable names and their description. Otherwise, the program will display an error.  
 * You must have an .xls file for each description. The website is configured to select one description and variable at a time, so the name of the Excel file should only contain one.
       Incorrects: 16-02-2020_17-02-2020_PRECIPITACION_Día pluviométrico_Precipitación total diaria.xls
                    16-02-2020_17-02-2020_PRECIPITACION_CAUDAL_Día pluviométrico_Caudal medio diario.xls
 * Only 10 inquiries can be made per request. Therefore, the number of stations in the Excel document should not exceed this amount.
 
## Functions

**MainIDEAM.py**     : this is the only function to run. It prepares the inputs to extract the data from the website using the Excel document detailed above. This function does not need to be modified. 

**IDEAM_extract.py** : in this function you must specify the output path and where the WebDriver is located (lines 22-23)

## List of varibales and descriptors
The file **ListVariablesAndDescriptions.md** contins some variables with their descriptions. If you are interested in other variables, you can visit the [IDEAM](http://dhime.ideam.gov.co/atencionciudadano/) website and check the different options. 

***
> **NOTE:** The function works well, but is still in progress. Feel free to contact me if you want to contribute or if you find any bug.

## Contact
You can contact me at emixi-sthefany.valdez-medina.1@ulaval.ca :e-mail::simple_smile:
