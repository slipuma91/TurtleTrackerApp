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



# Copy and paste a line of data as the lineString variable value
lineString = ""

# Use the split command to parse the items in lineString into a list object
lineData = lineString

# Assign variables to specfic items in the list
record_id = lineData[]             # ARGOS tracking record ID
obs_date = obs_dateTime.split()[]   # Observation date
ob_lc = lineData[]                 # Observation Location Class
obs_lat = lineData[]               # Observation Latitude
obs_lon = lineData[]               # Observation Longitude

# Print information to the use
print (f"Record {recordID} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
