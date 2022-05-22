#Set filepath of Proj.lib
import os

os.environ['PROJ_LIB'] = r"C:\Users\Annika\anaconda3\envs\Assignment2\Library\share\proj"
#import modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import shapely
import shapely.geometry
from shapely.geometry import Point
import gdal
import fiona
import pyproj
import geopandas as gpd
import descartes
import glob
import rasterio
from rasterio.plot import show
from rasterio.crs import CRS


#Read sampling points table and convert to pandas dataframe
'''line 1: read csv to pandas daataframe object named df,
   line 2: select columns from CSV to import
   line 3: print df object'''
df = pd.read_csv("Data\Sampling_Points_coor.csv")
df = df[["FID", "Lat_m", "Lon_m"]]
print(df)

#Convert pandas DataFrame to geopandas GeoDataFrame
'''Create Geoseries of point geometries from "Lat_m and "Long_m" columns,
define coordinate reference system as WGS84 UTM Zone 30N using EPSG code,
define Geodataframe as gdf'''
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Lon_m, df.Lat_m, crs=32630))
print(gdf)

#Write GeoDataFrame to shapefile
'''Write GeoDataFrame to shapefile with geopandas .to_file method,
define encoding method'''
gdf.to_file("Data\Sampling_Points.shp", encoding="utf-8")

#Load habitat map polygon shapefile
'''line 1:Read Ards_Map.shp file to object named Habitat_map,
   line 2:print Habitat_map object
   line 3:define coordinate reference system of Habitat_map object'''
Habitat_map = gpd.read_file("Data\Ards_Map.shp")
Habitat_map = Habitat_map.to_crs(32630)
print(Habitat_map)

#Load Sampling_Points shapefile
'''line 1: Load Sampling_Points shapefile to object named Points,
   line 2:print Points object'''
Points = gpd.read_file("Data\Sampling_Points.shp")
print(Points)

#Read raster chart file
chart = rasterio.open("Data\Ards.tif")


#Plot all layers together
fig, ax = plt.subplots()
base = show(chart, ax=ax)
Habitat_map.plot(ax=ax, column="Habitat", cmap='Pastel2');
Points.plot(ax=ax, color="red");
plt.show()


