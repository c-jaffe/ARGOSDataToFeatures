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

# environments
arcpy.env.overwriteOutput = True

# import data
inputFolder = 'C:/Advanced_GIS/GISandPython/ARGOSTracking/Data/ARGOSData'
inputFiles = os.listdir(inputFolder)
outputFC = "C:/Advanced_GIS/GISandPython/ARGOSTracking/Scratch/ARGOStrack.shp"

outputSR = arcpy.SpatialReference(54002)

outPath,outName = os.path.split(outputFC)
arcpy.CreateFeatureclass_management(outPath, outName, "POINT", "", "", "", outputSR)

arcpy.AddField_management(outputFC, "TagID", "LONG")
arcpy.AddField_management(outputFC, "LC", "TEXT")
arcpy.AddField_management(outputFC, "Date", "DATE")

# create cursor
cur = arcpy.da.InsertCursor(outputFC, ["Shape@", "TagID", "LC", "Date"])

#%% Construct a while loop to iterate through all lines in the datafile

for inputFile in inputFiles:
    #status
    print("Processing {}".format(inputFile))
    
    # skip readme
    if inputFile == "README.txt": continue

    inputFile = os.path.join(inputFolder, inputFile)

    # Open the ARGOS data file for reading
    inputFileObj = open(inputFile,'r')
    
    # Get the first line of data, so we can use a while loop
    lineString = inputFileObj.readline()
    
    # Start the while loop
    while lineString:
        
        # Set code to run only if the line contains the string "Date: "
        if ("Date :" in lineString):
            
            # Parse the line into a list
            lineData = lineString.split()
            
            # Extract attributes from the datum header line
            tagID = lineData[0]
            obsDate = lineData[3]
            obsTime = lineData[4]
            obsLC = lineData[7]
            
            # Extract location info from the next line
            line2String = inputFileObj.readline()
            
            # Parse the line into a list
            line2Data = line2String.split()
            
            # Extract the date we need to variables
            obsLat = line2Data[2]
            obsLon= line2Data[5]
                    
            # try to convert coords to numbers
            try:
                # Convert raw coordinate strings to numbers
                if obsLat[-1] == 'N':
                    obsLat = float(obsLat[:-1])
                else:
                    obsLat = float(obsLat[:-1]) * -1
                if obsLon[-1] == 'E':
                    obsLon = float(obsLon[:-1])
                else:
                    obsLon = float(obsLon[:-1]) * -1
            
                # Construct a point object from the feature class
                obsPoint = arcpy.Point()
                obsPoint.X = obsLon
                obsPoint.Y = obsLat
                
                # create Feature object
                feature = cur.insertRow((obsPoint, tagID, obsLC, obsDate.replace(".","/") + " " + obsTime))
                
            except Exception as e:
                print(f"Error adding record {tagID} to the output")
            
            
        # Move to the next line so the while loop progresses
        lineString = inputFileObj.readline()

    # Close the file object
    inputFileObj.close()

# delete cursor
del cur


#%% 


