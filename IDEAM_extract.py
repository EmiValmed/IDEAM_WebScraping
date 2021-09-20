# -*- coding: utf-8 -*-
######################################################################################################################################################
# Name         : pyIDEAM 
# Author       : Emixi Valdez (emixi-sthefany.valdez-medina.1@ulaval.ca) 
# Date         : Mon Aug 23 17:36:22 2021
# 
######################################################################################################################################################
# LIBRERIES
######################################################################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

######################################################################################################################################################
# DIRECTORIES AND PREFERENCE
######################################################################################################################################################

# Directories
dirout = r"C:\path\output folder"                # To modify
chrome_path = r"C:\path of the\chromedriver.exe" # To modify

# Web browser (Chrome) preference
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-sandbox")
prefs = {"download.default_directory" : dirout }
chrome_options.add_experimental_option("prefs",prefs)

# Tables' name in the HTML code
ListsName = ['deptos2','municipio2']


######################################################################################################################################################
# Functions 
######################################################################################################################################################

# Function for manual entry (e.g. dates, names, etc.)
def Input_data(X_PATH, ID, INPUT):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, ID))).click()
    Date = driver.find_element_by_xpath(X_PATH)
    Date.clear()
    Date.send_keys([INPUT], Keys.ENTER)

# Selecting by xpath    
def slect_XPATH(XPATH_t):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, XPATH_t))).click() 

######################################################################################################################################################
# Web scraping IDEAM data
######################################################################################################################################################
driver = webdriver.Chrome(chrome_path, chrome_options = chrome_options)
driver.maximize_window()

def download_IDEAM(DepartmetInfo, inputs):
    
    StartDate = inputs['StartDate']
    EndDate =  inputs['EndDate']
    Parameter = inputs['Parameter']
    Description= inputs['Description'] 
  
    # Open website
    driver.get("http://dhime.ideam.gov.co/atencionciudadano/")

    # Accept terms and conditions 
    slect_XPATH('//*[@id="jimu_dijit_CheckBox_0"]/div[1]')
    slect_XPATH('//div[@class = "jimu-btn jimu-float-trailing enable-btn" ]')
          
    # Start Date
    Input_data('//input[contains(@value, "01/01/1990")]', 'datepicker',StartDate)

    # End Date  
    Input_data('//*[@id="datepicker1"]', 'datepicker1',EndDate)
    
    # Loop by "Departamento" and "Municipio"
    for iDepartment in DepartmetInfo:
        
        for iMunicipio in DepartmetInfo[iDepartment]:
                
            # Selecting parameter and description
            slect_XPATH("//span[@class='k-widget k-dropdown k-header' and @aria-owns='Parametro_listbox']")
            slect_XPATH( "//div[@class='k-animation-container']/div[@id='Parametro-list']//ul//li[text()='{}']".format(Parameter))                                  
            slect_XPATH('//*[@title="{}"]//preceding-sibling::td//input[@type="radio"]'.format(Description))
    
    # Selecting Departamento and Municipio
            VALUE = [iDepartment, iMunicipio]

            for List, Val in zip(ListsName, VALUE):   
                slect_XPATH("//span[@class='k-widget k-dropdown k-header' and @aria-owns='{}_listbox']".format(List))
                slect_XPATH( "//div[@class='k-animation-container']/div[@id='{}-list']//ul//li[text()='{}']".format(List,Val))

    # Selecting stations  
            Stations = DepartmetInfo[iDepartment][iMunicipio]
            for iStations in Stations:
                slect_XPATH('//input[@value="{}"]/parent::td//preceding-sibling::td//input[@type="checkbox"]'.format(iStations))
          
    # Agregar consulta button
            slect_XPATH('//*[@id="first"]/div[5]/div')
            
            # Agregar otros button
            slect_XPATH('//*[@id="second"]/div/div[3]/div[2]')
                           
# Download and accept terms and policies
    slect_XPATH('//*[@id="ContenedorCiudadano_tablist"]/div[4]/div/div[2]') 
    slect_XPATH('//*[@id="second"]/div/div[3]/div[1]')
    slect_XPATH('//*[@id="dijit_form_Button_2_label"]')

# Limpiar descarga buttom
    slect_XPATH('//*[@id="second"]/div/div[3]/div[3]')
    slect_XPATH('//*[@id="dijit_form_Button_4"]')
    
#driver.quit()
