# -*- coding: utf-8 -*-
"""Clase 280624.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QiB3L2vAARHucpSzdLpy681MEFDuVr9w
"""

from google.colab import auth
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
#El id es el numero que aparece en el archivo
#https://drive.google.com/file/d/1iIMfMSqLr3eHZ3y-KZKmj_MaAEe2A-3u/view?usp=sharing
myfile = drive.CreateFile({'id': '1iIMfMSqLr3eHZ3y-KZKmj_MaAEe2A-3u'})
myfile.GetContentFile('datos1.txt')

import pandas as pd
frm = pd.read_csv('datos1.txt', header=None)
print(frm.head())
print(frm.tail())
print('Que columnas tengo\n', frm.columns)

import numpy as np

datosF = np.loadtxt('datos1.txt', delimiter=',')
print(datosF)

print(datosF[:,0])

c1 = datosF[:,0]

c1.sort()

print(c1)