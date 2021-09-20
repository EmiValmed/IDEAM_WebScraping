# -*- coding: utf-8 -*-
######################################################################################################################################################
# Name         : pyIDEAM 
# Author       : Emixi Valdez (emixi-sthefany.valdez-medina.1@ulaval.ca) 
# Date         : Mon Aug 23 17:36:22 2021
# 
######################################################################################################################################################
# LIBRERIES
######################################################################################################################################################
import os
import sys
import IDEAM_test
import pandas as pd
import tkinter as tk
from tkinter import filedialog
######################################################################################################################################################
 
######################################################################################################################################################

# Open input file
root    = tk.Tk()
INPUT = filedialog.askopenfilename( title="select file")
root.destroy()

if (INPUT == None):
    sair = tk.raw_input('\tInput file not selected. \n\t\tPress enter to exit.\n')
    sys.exit()

Path, fileName = os.path.split(INPUT)
GeneralInformation = pd.read_excel(INPUT)

# Retrieve file information to fill out the inquiry form
inputs = dict()
inputs['StartDate'] = fileName.split(sep='_')[0].replace("-","/") # Fecha Initial                   
inputs['EndDate'] = fileName.split(sep='_')[1].replace("-","/")   # Fecha Final
inputs['Parameter'] = fileName.split(sep='_')[2]                  # Parámetro
Description = fileName.split(sep='_')[3]                          # Descripción
inputs['Description'] = Description.split(sep='.')[0]             # Eliminating the extension file


## Store the information in a database (Station ID, Departamento and Municipio)
Localization = dict()
for index in GeneralInformation.index:
               
    id_station = GeneralInformation["CODIGO"][index]
    Departamento = GeneralInformation["DEPARTAMENTO"][index]
    Municipio = GeneralInformation["MUNICIPIO"][index]
               
    if Departamento not in Localization:
        Localization[Departamento] = dict()
        if Municipio not in Localization[Departamento]:
             Localization[Departamento][Municipio] = list()
             
    Localization[Departamento][Municipio].append(id_station)
            
######################################################################################################################################################
# IDEAM web scraping   
######################################################################################################################################################
   
IDEAM_test.download_IDEAM(Localization, inputs)
