import json
from collections import defaultdict
import numpy as np

def get_sorted_data(data_file,window=0):
    data = defaultdict(list)
    mov_avg_data = defaultdict(list)


#open the file, read each line, and add the values to the dictionary
    with open(data_file,'r') as f:
        for line in f:
            els = line.split()
            if len(els) !=0:
                #some lines in the data file are empty, avoid those
                keys = str(els[1][-2:])
                    #Only grab the last two characters of the keys to omit any unwanted prefixes
                values = {'osTimeStamp' : str(els[0]), 'value' : int(els[2])}
                    #grab the time and values from the list and create dict for data output
                data[keys].append(values)
                    #add the dict pulled from values


#-------Filter function that adds the moving averaged values, and time stamps to a dict with the specified keys-------
## NOTE: The ifs just handle the window size if it's too big.
## If the window is bigger than the data set-
## then I chose to apply a filter half the size of the number of values. This is an arbitrary choice.
## I figure if you're adding a filter, you want cleaner data,-
## so instead of passing the whole data set, I force a filter size.
## Default window is set to 0 which applies no filter, and returns original data output from part1.

    def filter(nums,window):
        if window == 0:
             return(nums)
        elif window <= len(nums):
            avg = np.convolve([x['value'] for x in nums],np.ones((window))/window, mode = 'valid')
                #This is where the filtering takes place.
            avg = [int(a) for a in avg]
            stamps = [y['osTimeStamp'] for y in nums]
            pair = list(zip(stamps[window-1:], avg))
                # Take the latest time stamps and pair them with the filtered values
            pair_dict = []
            for p in pair:
                pair_dict.append({"osTimeStamp": str(p[0]), "value": int(p[1])})
        elif window > len(nums):
            window = int((len(nums)/2))
                # If the window length exceeds the number of data points, force a filter size
            avg = np.convolve([x['value'] for x in nums],np.ones((window))/window, mode = 'valid')
            avg = [int(a) for a in avg]
            stamps = [y['osTimeStamp'] for y in nums]
            pair = list(zip(stamps[window-1:], avg))
            pair_dict = []
            for p in pair:
                pair_dict.append({"osTimeStamp": str(p[0]), "value": int(p[1])})


        return(pair_dict)


    for k,v in data.items():
        mov_avg_data[k] = filter(v,window)
            #create the cleaned data dict ready for export

    return(mov_avg_data)


#    ex = json.dumps(mov_avg_data)
#    print(ex)
        #uncomment to check functionality


#get_sorted_data('Data.txt',80)
