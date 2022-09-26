import pandas as pd
import numpy as np
import math
file = pd.read_csv("exp3_file.csv")
from csv import writer

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    l=column.shape[0]
    freq = {}
    for item in column:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    
    probabilities={}
    for item in column:
         probabilities[item]=freq[item]/l

    
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if probabilities[prob] > 0:
            # use log from math and set base to 2
            entropy += probabilities[prob] * math.log(probabilities[prob], 2)
    
    return -entropy


def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    #Find the unique values in the column
    values = data[split_name].unique()
    
    
    # Make two subsets of the data, based on the unique values
    left_split = data[data[split_name] == values[0]]
    right_split = data[data[split_name] == values[1]]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    print(original_entropy - to_subtract)
    return original_entropy - to_subtract

arr=list(file.columns)
length = len(arr)
i=1
row_contents = ["Info Gain"]
while i<length-1:
   info_gain = calc_information_gain(file,arr[i],arr[length-1])
   row_contents.append(info_gain)
   i=i+1   

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

append_list_as_row('exp3_file.csv', row_contents)