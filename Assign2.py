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

#Read sampling points table and convert to pandas dataframe
df = pd.read_csv("Data\Sampling_Points_coor.csv")
df = df[["FID", "Lat_m", "Lon_m"]]
'''select columns from CSV to import'''
print(df)

#Convert pandas DataFrame to geopandas GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Lon_m, df.Lat_m, crs=32630))
'''Create Geoseries of point geometries from "Lat_m and "Long_m" columns,
 define coordinate reference system as WGS84 UTM Zone 30N using EPSG code,
 define Geodataframe as gdf'''
print(gdf)

#Write GeoDataFrame to shapefile
gdf.to_file("Data\Sampling_Points.shp", encoding="utf-8")
'''Write GeoDataFrame to shapefile with geopandas .to_file method,
define encoding method'''

#Load habitat map polygon shapefile
Habitat_map = gpd.read_file("Data\Ards_Map.shp")
print(Habitat_map)
Habitat_map.plot(column="Habitat", cmap='Pastel2', legend=True);
#plt.show()

#Read raster chart file
#chart = rasterio.open("Data\1121.tif")
