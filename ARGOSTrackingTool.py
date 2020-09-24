#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sarah Lipuma (sarah.lipuma@duke.edu)
# Date:   September 19, 2020
#--------------------------------------------------------------


#Pretend we read one line of data from the file
# Copy and paste a line of data as the lineString variable value
lineString = '20621	29051	7/3/2003 12:11	B	0	33.575	-77.691	32.741	-73.276	2	0	-126	408	2	401 651134.7	0'

#Split the string into a list of data items
lineData = lineString.split()

#extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")