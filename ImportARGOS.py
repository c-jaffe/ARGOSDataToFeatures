##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2020
## Author: catherine.jaffe@duke.edu (for ENV859)
##---------------------------------------------------------------------

 # library
import sys, os, arcpy

# import data
inputFile = 'C:/Advanced_GIS/GISandPython/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "C:/Advanced_GIS/GISandPython/ARGOSTracking/Scratch/ARGOStrack.shp"






