# Data_processing
Data processing with GEE

##Introduction
This repository offers a pipeline for processing Landsat imagery and conducting statistical analyses to assess the environmental impacts on vegetation recovery in Obara and Shobara, Japan. The pipeline includes preprocessing steps for Landsat data and environmental variables using Google Earth Engine and statistical analysis using Python.

##Features
This pipeline comprises two main parts:

1. Preprocessing and vegetation index generation (GEE):
This part involves downloading, preprocessing, and deriving vegetation indices from Landsat imagery and environmental variables from Digital Elevation Models. These tasks are primarily accomplished using Google Earth Engine (GEE). The resulting geotiffs of vegetation indices can be exported for further analysis. The vegetation indices of interest include:

- NDVI: Normalized Difference Vegetation Index
- EVI: Enhanced Vegetation Index

2. Statistical analysis and trend analysis (Python):
The second part prepares the vegetation index geotiffs for subsequent statistical analyses. The post-processing steps include reshaping arrays, calculating the distribution of d_NDVI and d_EVI, conducting statistical analysis, trend analysis, and modeling.

##Contents:
The repository is organized into the following folders:

- GEE: Contains Google Earth Engine scripts (URL) for obtaining vegetation index values and environmental variables.
- Python: Contains Python scripts for deriving recovery metrics to analyze the environmental effects on vegetation recovery.
