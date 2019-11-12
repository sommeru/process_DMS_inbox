#!./venv/bin/python3

import os
import subprocess
import glob
import os.path

DMSdirectory = '/Users/sommeru/Documents/DMS/'

DMSinboxConsors = 'inbox_consorsbank/'
DMSoutboxConsors = 'Documents/finanzen/consorsbank/'
DMSoutboxConsorsAccounts = [
    'ulrich_allg_dok',
    '220566180', 'saskia_ulrich-girokonto-220566180',
    '848637666', 'ulrich_depot-848637666',
    '200908373', 'ulrich_girokonto-200908373',
    '843637661', 'ulrich_tagesgeld-843637661',
    '840637664', 'ulrich_verrechnungskonto-840637664',
    ]

DMSinboxComdirect = 'inbox_comdirect/'
DMSoutboxComdirect = 'Documents/finanzen/comdirect/'
DMSoutboxConsorsAccount = 'DE84200411330339130700'


####Consorsbank#####
directory = os.fsencode(DMSdirectory + DMSinboxConsors)

# Process files containing Account Numbers
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".pdf"):
        for i in range (1, len(DMSoutboxConsorsAccounts)):
            if (DMSoutboxConsorsAccounts[i] in filename):
                str_desc = filename[:(filename.find('_dat'))]
                outpath = (DMSoutboxConsorsAccounts[i+1])
                str_date = filename[(filename.find('_dat') + 4):(filename.find('_dat') + 12)]
                #print (str_desc)
                #print (DMSoutboxConsorsAccounts[i+1])
                #print (str_date)
                print ('mv', DMSdirectory + DMSinboxConsors  + filename, DMSdirectory + DMSoutboxConsors + outpath + '/' + str_date + '--' + str_desc + '.pdf')
                subprocess.call(['mv', DMSdirectory + DMSinboxConsors  + filename, DMSdirectory + DMSoutboxConsors + outpath + '/' + str_date + '--' + str_desc + '.pdf'])
                break
        continue
     else:
        continue

#process remaining files
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".pdf"):
        str_desc = filename[:(filename.find('_dat'))]
        outpath = DMSoutboxConsorsAccounts[0]
        str_date = filename[(filename.find('_dat') + 4):(filename.find('_dat') + 12)]
        print ('mv', DMSdirectory + DMSinboxConsors  + filename, DMSdirectory + DMSoutboxConsors + outpath + '/' + str_date + '--' + str_desc + '.pdf')
        subprocess.call(['mv', DMSdirectory + DMSinboxConsors  + filename, DMSdirectory + DMSoutboxConsors + outpath + '/' + str_date + '--' + str_desc + '.pdf'])

####Comdirect####
directory = os.fsencode(DMSdirectory + DMSinboxComdirect)

# Process PDFs
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if (filename.endswith(".pdf")):
        if ("_vom_" in filename):
            str_dateYear = filename[(filename.find('_vom_') + 11):(filename.find('_vom_') + 15)]
            str_dateMonth = filename[(filename.find('_vom_') + 8):(filename.find('_vom_') + 10)]
            str_dateDay = filename[(filename.find('_vom_') + 5):(filename.find('_vom_') + 7)]
            str_date=str_dateYear + str_dateMonth + str_dateDay
            str_desc = filename[:(filename.find('_vom_'))]
            subprocess.call(['mv', DMSdirectory + DMSinboxComdirect  + filename, DMSdirectory + DMSoutboxComdirect + DMSoutboxConsorsAccount + '/' + str_date + '--' + str_desc + '.pdf'])
            print ('mv', DMSdirectory + DMSinboxComdirect  + filename, DMSdirectory + DMSoutboxComdirect + DMSoutboxConsorsAccount + '/' + str_date + '--' + str_desc + '.pdf')



    if ("_per_" in filename):
            str_dateYear = filename[(filename.find('_per_') + 11):(filename.find('_per_') + 15)]
            str_dateMonth = filename[(filename.find('_per_') + 8):(filename.find('_per_') + 10)]
            str_dateDay = filename[(filename.find('_per_') + 5):(filename.find('_per_') + 7)]
            str_date=str_dateYear + str_dateMonth + str_dateDay
            str_desc = filename[:(filename.find('_per_'))]
            print ('mv', DMSdirectory + DMSinboxComdirect  + filename, DMSdirectory + DMSoutboxComdirect + str_date + '--' + str_desc + '.pdf')
            subprocess.call(['mv', DMSdirectory + DMSinboxComdirect  + filename, DMSdirectory + DMSoutboxComdirect + str_date + '--' + str_desc + '.pdf'])



