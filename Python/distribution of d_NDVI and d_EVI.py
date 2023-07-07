#!/usr/bin/env python
# coding: utf-8



from osgeo import gdal
from PIL import Image
import rasterio as rs
from rasterio.plot import show
import os
import glob
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from matplotlib.colors import ListedColormap
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import georaster
import copy
import matplotlib.colors as colors



# Distribution of d_NDVI in Obara
ndvi = gdal.Open(r'/Users/zhongchenxi/change_raw/xyc_change_1985-2011.tif')
ndvi_data = ndvi.GetRasterBand(1).ReadAsArray().astype(np.float32)


ndviclass = copy.copy(ndvi_data)
ndviclass[np.where(ndvi_data <= 0)] = 0
ndviclass[np.where((ndvi_data>0)&(ndvi_data<=0.1))] = 1
ndviclass[np.where((ndvi_data>0.1)&(ndvi_data<=0.2))] = 2
ndviclass[np.where((ndvi_data>0.2)&(ndvi_data<=0.3))] = 3
ndviclass[np.where(ndvi_data>0.3)] = 4
plt.figure()


ndvi_colors = ["gray","lightsteelblue", "pink", "gold", "green"]
ndvi_cmap = ListedColormap(ndvi_colors)
ndvi_cat_names = [
    "very poor",
    "poor",
    "good",
    "very good",
    "excellent"
]

classes = np.unique(ndviclass)
classes = classes.tolist()
classes = classes[0:5]

fig, ax = plt.subplots(figsize=(12, 12))
im = ax.imshow(ndviclass, cmap=ndvi_cmap)

ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)

ax.set_axis_off()

plt.tight_layout()




#Distribution of d_NDVI in Shobara
ndvi = gdal.Open(r'/Users/zhongchenxi/change_raw/zy_change_2011-2019.tif')
ndvi_data = ndvi.GetRasterBand(1).ReadAsArray().astype(np.float32)


ndviclass = copy.copy(ndvi_data)
ndviclass[np.where(ndvi_data <= 0)] = 0

ndviclass[np.where((ndvi_data>0)&(ndvi_data<=0.05))] = 1
ndviclass[np.where((ndvi_data>0.05)&(ndvi_data<=0.1))] = 2
ndviclass[np.where((ndvi_data>0.1)&(ndvi_data<=0.2))] = 3
ndviclass[np.where(ndvi_data>0.2)] = 4
plt.figure()


ndvi_colors = ["gray","lightsteelblue", "pink", "gold", "green"]
ndvi_cmap = ListedColormap(ndvi_colors)
ndvi_cat_names = [
    "very poor",
    "poor",
    "good",
    "very good",
    "excellent"
]

classes = np.unique(ndviclass)
classes = classes.tolist()
classes = classes[0:5]

fig, ax = plt.subplots(figsize=(12, 12))
im = ax.imshow(ndviclass, cmap=ndvi_cmap)

ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)
# ax.set_title(
#     "changes of NDVI from 1985 to 2011 in Obara",
#     fontsize=14,
# )
ax.set_axis_off()

plt.tight_layout()




#Distribution of d_EVI in Obara
evi = gdal.Open(r'/Users/zhongchenxi/change_raw/xyc_change_1985-2011.tif')
evi_data = evi.GetRasterBand(2).ReadAsArray().astype(np.float32)


eviclass = copy.copy(evi_data)
eviclass[np.where(evi_data <= 0)] = 0

eviclass[np.where((evi_data>0)&(evi_data<=0.1))] = 1
eviclass[np.where((evi_data>0.1)&(evi_data<=0.2))] = 2
eviclass[np.where((evi_data>0.2)&(evi_data<=0.3))] = 3
eviclass[np.where(evi_data>0.3)] = 4
plt.figure()


evi_colors = ["gray","lightsteelblue", "pink", "gold", "green"]
evi_cmap = ListedColormap(evi_colors)
evi_cat_names = [
    "very poor",
    "poor",
    "good",
    "very good",
    "excellent"
]

classes = np.unique(eviclass)
classes = classes.tolist()
classes = classes[0:5]

fig, ax = plt.subplots(figsize=(12, 12))
im = ax.imshow(eviclass, cmap=evi_cmap)

ep.draw_legend(im_ax=im, classes=classes, titles=evi_cat_names)

ax.set_axis_off()

plt.tight_layout()




#Distribution of d_EVI in Shobara
evi = gdal.Open(r'/Users/zhongchenxi/change_raw/zy_change_2011-2019.tif')
evi_data = evi.GetRasterBand(2).ReadAsArray().astype(np.float32)


eviclass = copy.copy(evi_data)
eviclass[np.where(evi_data <= 0)] = 0

eviclass[np.where((evi_data>0)&(evi_data<=0.05))] = 1
eviclass[np.where((evi_data>0.05)&(evi_data<=0.1))] = 2
eviclass[np.where((evi_data>0.1)&(evi_data<=0.2))] = 3
eviclass[np.where(evi_data>0.2)] = 4
plt.figure()


ndvi_colors = ["gray","lightsteelblue", "pink", "gold", "green"]
ndvi_cmap = ListedColormap(evi_colors)
ndvi_cat_names = [
    "very poor",
    "poor",
    "good",
    "very good",
    "excellent"
]

classes = np.unique(eviclass)
classes = classes.tolist()
classes = classes[0:5]

fig, ax = plt.subplots(figsize=(12, 12))
im = ax.imshow(eviclass, cmap=evi_cmap)

ep.draw_legend(im_ax=im, classes=classes, titles=evi_cat_names)

ax.set_axis_off()

plt.tight_layout()






