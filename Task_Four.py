# -*- coding: utf-8 -*-
"""
Created on Sun Dec 2 22:46:14 2018

@author: Aisha Aijaz Ahmad
"""

#import relevant libraries
#for implementing json file
import json
#for dataframe handling
import pandas as pd
#for printing the graph
from graphviz import Digraph
#to change the path of the graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Aisha Aijaz Ahmad/Desktop/graphviz-2.38/release/bin'

#importing the required dataset
#USE THIS DATASET: http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_cw2.json
Data_List = []
with open('C:/Users/Aisha Aijaz Ahmad/Desktop/dataset.json', 'r') as json_file:
    for line in json_file:
        Data_List.append(json.loads(line))

#starting new class for task 4
class TaskFour:
    
    #task 4a
    """
    Definition Description:
        The function getreaders takes one input and returns the list of visitors
        that have read that document id.
    Parameters: doc_id
        This is the id for the subject document that is to be checked for 
        readers.
    """
    def getreaders(self, doc_id):    
        x=pd.DataFrame.from_records(Data_List)
        byEnv = x.loc[x.subject_doc_id == doc_id] 
        final = byEnv['visitor_uuid'].unique()
        print(final)
        return final
    
    #task 4b
    """
    Definition Description:
        The function getvisitors takes one input and returns the list of documents
        that have been read by that visitor.
    Parameters: vis_id
        This is the id for the user that is to be checked for documents read.
    """
    def getvisitors(self, vis_id):
        y=pd.DataFrame.from_records(Data_List)
        byVis = y.loc[y.visitor_uuid == vis_id]
        final = byVis['subject_doc_id'].unique()
        print(final)
        return final
  
    #task 4c
    """
    Definition Description:
        The function getreaders takes two inputs and returns the SORTED list of documents
        that are most popular (based on number of reads). It also prints the graph for the
        functionality which shows the relationship between the two parameters, visitors and
        documents.
        
    Parameters: visitor_id, document_id
        These are the respective ids for the visitors and the subject documents that are 
        to be checked and for which a directed graph is printed.
    """
    def alsolikes(self, visitor_id, document_id):
        z=pd.DataFrame.from_records(Data_List)
        vislist = self.getreaders(document_id)
        doclist = []
        length = len(vislist)
        graph=Digraph('G',filename='graphPlot.gv')
        
        for i in range(0, length):
            for index, row in z.iterrows():
                
                check1 = vislist[i]
                check2 = z.iloc[index]['visitor_uuid']
                if check1 == check2:
                    doclist.append(z.iloc[index]['subject_doc_id'])
                    
        #task 5
        new = list(set(doclist))
        length2 = len(new)
        for j in range(0, length):
            if vislist[j] == visitor_id:
                graph.node(vislist[j][-4:], shape="square", style = "filled", color = "green")
            else:
                graph.node(vislist[j][-4:],shape='square')
            for k in range(0, length2):
                if document_id == new[k]:
                    graph.node(new[k][-4:], shape = "circle", style = 'filled', color = 'green')
                    graph.edge(vislist[j][-4:], new[k][-4:])
                else:
                    graph.node(new[k][-4:], shape = "circle")
                    graph.edge(vislist[j][-4:], new[k][-4:])
        uniquelength = len(set(doclist))
        
        graph.render('test-output/graphPlot.gv', view=True)
        'test-output/graphPlot.gv.jpg'
        
        return doclist, uniquelength

    #task 4d
        
    """
    Definition Description:
        This definition sorts the dictionary of documents based on the number of "reads" each 
        document has. It has a conditional statement which checks if the number of unique documents
        is less than or greater than 10. If it is less than 10, the list is sorted and printed
        directly, otherwise the list is trimmed to show only the top ten entries which are
        most popular.
    Parameters: unique_count, mydict
        unique_count holds the count of how many documents in the dictionary are unique.
        mydict holds the dictionary of documents required for the system.
        
    """
    def sort_top(self, unique_count, mydict):
        if unique_count<10:
            sorted_x = {k: mydict[k] for k in sorted(mydict.keys())[:]}
            return sorted_x
        else:
            sorted_y = {k: mydict[k] for k in sorted(mydict.keys())[:10]}
            return sorted_y
            
#end of class 



    
