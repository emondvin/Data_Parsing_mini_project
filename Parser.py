import json
from collections import defaultdict

#This program will parse a data file that follows the format seen in Data.txt
#Define the function to be called given some data file input
#Sort the data into a dictionary. Use defaultdict such that unkeyed entries can be added

def get_sorted_data(data_file):
    data = defaultdict(list)

#open the file, read each line, and add the values to the dictionary
    with open(data_file,'r') as f:
        for line in f:
            els = line.split()      #split to access elements
            if len(els) !=0:        #some lines in the data file are empty, avoid those
                keys = str(els[1][-2:])     #Only grab the last two characters of the keys to omit any unwanted prefixes
                values = {'osTimeStamp' : str(els[0]), 'value' : int(els[2])}  #grab the time and values from the list and create dict for data output
                data[keys].append(values)  #add the dictionary of values to data dictionary

#uncomment below to test outputs
    #export = json.dumps(data, indent = 4)
    #print(data)
    #print(export)

    return(data)

#get_sorted_data("Data_sub.txt")
