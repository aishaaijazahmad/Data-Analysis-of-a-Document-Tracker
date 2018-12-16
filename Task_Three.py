# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 19:29:52 2018

@author: Aisha Aijaz Ahmad
"""

#import relevant libraries
#for implementing json file
import json
#for dataframe handling
import pandas as pd

#importing the required dataset
Data_List = []
with open('C:/Users/Aisha Aijaz Ahmad/Desktop/dataset.json', 'r') as json_file:
    for line in json_file:
        Data_List.append(json.loads(line))
    
#starting new class for task 4
class TaskThree:
    
    #task 3a 
    """
    Definition Description:
        This function prints a histogram recording the frequencies of the all the visitors of for all
        browser identifiers.
    Parameters: none
        The function uses global parameters.
    """
    def threea(self):
        y = pd.DataFrame.from_records(Data_List)
        newcount = y.groupby(by='visitor_useragent', as_index=False).agg({'ts': pd.Series.nunique})
        newcount
        newcount.hist()
        return
    
    #task 3a
    """
    Definition Description:
        This function prints a histogram recording the frequencies of the all the visitors of for all
        browser identifiers when the names of the browsers are shortened.
    Parameters: none
        The function uses global parameters.
    """
    def threeb(self):
        z = pd.DataFrame.from_records(Data_List)
        z['Browser_Name']=z['visitor_useragent'].apply(lambda name:name[name.find("^")+1:name.find("/")])
        count = z['Browser_Name'].value_counts()
        count.plot.bar()
        return count

#end of class