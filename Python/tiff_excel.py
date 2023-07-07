# -*- coding: utf-8 -*-
"""tiff_excel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zkiqr3gYeBZrCRxG8bmvyNZZJDPG19Kn
"""

from google.colab import drive
drive.mount('/content/drive')

# Install GDAL and Geopandas
!apt install gdal-bin python-gdal python3-gdal --quiet
!apt install python3-rtree --quiet
!pip install git+git://github.com/geopandas/geopandas.git --quiet
!pip install descartes --quiet

# Rasterio
!pip install Rasterio

from osgeo import gdal,gdalconst
import numpy as np
import pandas as pd
import glob
import os

def read_image(img_path):
  dataset = gdal.Open(img_path)
  img_width = dataset.RasterXSize
  img_height = dataset.RasterYSize
  adf_GeoTransform = dataset.GetGeoTransform()
  im_Proj = dataset.GetProjection()

  img_data = np.array(dataset.ReadAsArray(0,0,img_width,img_height),dtype = float)

  del dataset

  return img_data,img_width,img_height,adf_GeoTransform,im_Proj

def dataToCsv(data,width,height,adf_GeoTransform,writer,band):
  index = []
  columns = []
  nXSize = width
  nYSize = height

  for i in range(nXSize):
    lon = adf_GeoTransform[0] + i * adf_GeoTransform[1]
    columns.append(lon)

  for j in range(nYSize):
    lat = adf_GeoTransform[3] + j * adf_GeoTransform[5]
    index.append(lat)

  df = pd.DataFrame(data, index=index, columns=columns)


  df.to_excel(writer, sheet_name = f'{band}')

path = r'/content/drive/MyDrive/subtraction_max_ndvi'
file_names = glob.glob(rf'{path}/*.tif')
print(file_names)

new_path = r'/content/drive/MyDrive/subtraction_max_ndvi_result'


bands_name = ['ndvi','evi','elevation','slope','aspect','hor_curv','ver_curv','max_curv','geo']
#  bands_name = ['ndvi_median','evi_median','avi_median','si_median','bi_median','nbr_median','vci_median','ndwi_median','mndwi_median','brightness_median','greeness_median','wetness_median','fvc_median']
for path in file_names:
  new_name = r'/' + path[-13:-4] + '.xlsx'
  print(new_name)
  writer = pd.ExcelWriter(new_path + new_name)
  img_data,img_width,img_height,adf_GeoTransform,im_Proj = read_image(path)
  if np.shape(img_data)[0] == 1:
    for band in range(0,2):
      data = img_data[band,:,:]
      # print(data)
      print(band)
      dataToCsv(data,img_width,img_height,adf_GeoTransform,writer,bands_name[band])
    writer.save()