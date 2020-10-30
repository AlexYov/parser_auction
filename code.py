from ftplib import FTP
import os
import ftplib

HOST = 'ftp.zakupki.gov.ru'

with FTP(HOST) as ftp:
    ftp.login('free','free')

    ftp.cwd('fcs_regions/Sverdlovskaja_obl/contractprojects/currMonth')
    #data = ftp.retrlines('LIST') #показать список файлов
    data =ftp.dir()
    #print(data)
    filenames = ftp.nlst() #получить названия файлов в виде списка

    for filename in filenames:
        host_file = os.path.join('путь где сохранить файлы', filename)
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)

    ftp.quit()
