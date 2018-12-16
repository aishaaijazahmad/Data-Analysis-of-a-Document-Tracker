# -*- coding: utf-8 -*-
"""
Created on Mon Dec 3 19:28:38 2018

@author: Aisha Aijaz Ahmad
"""

#import relevant libraries
#required libraries for GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#for sorting function
from collections import Counter

#importing classes from python files
from Task_Two import TaskTwo
from Task_Three import TaskThree
from Task_Four import TaskFour

#creating objects for each imported class
classObject2 = TaskTwo() 
classObject3 = TaskThree()
classObject4 = TaskFour()
    
#starting new class
class My_window:

    #constructor for this class
    def __init__(self):
        #create the window on startup
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.geometry("300x350+100+100")
        self.mainframe = tk.Frame(self.window)
        
        #create relevant starting labels
        self.select_lbl=tk.Label(self.window,text=" \nData Analysis System of a Document Tracker ", font = 'Helevtica 9 bold')
        self.select_lbl.pack()
        self.Enter_lbl=tk.Label(self.window,text="Enter text :")
        self.Enter_lbl.pack()
        
        #create text box
        uuid = tk.StringVar()
        self.Entry=tk.Entry(self.window, width=40, textvariable=uuid)
        self.Entry.pack()
        
        #create buttons
        self.btn1=tk.Button(self.window,text="Views by Country",command=self.task_two_a,width=30).pack()
        self.btn2=tk.Button(self.window,text="Views by Continent",command=self.task_two_b,width=30).pack()
        self.btn3=tk.Button(self.window,text="Views by Browser",command=self.task_three_a,width=30).pack()
        self.btn4=tk.Button(self.window,text="View by Browser (Non-Verbose)",command=self.task_three_b,width=30).pack()
        self.btn5=tk.Button(self.window,text="Readers of Document",command=self.task_four_a,width=30).pack()
        self.btn6=tk.Button(self.window,text="Documents Read",command=self.task_four_b,width=30).pack()
        self.btn7=tk.Button(self.window,text="Also Likes Functionality",command=self.fn_doc_also_like,width=30).pack()
        
        #create label for command line
        self.Enter_cmd_lbl=tk.Label(self.window,text="\nCommand Line:")
        self.Enter_cmd_lbl.pack()
        
        #creating a new textbox
        uuid2 = tk.StringVar()
        self.Entry_cmd=tk.Entry(self.window, width=40, textvariable=uuid2)
        self.Entry_cmd.pack()
        
        #create a button to run command line
        self.btn8=tk.Button(self.window,text="Run Command",command=self.commandline,width=30, fg = 'red').pack()
        self.window.mainloop()
    
    #call function for task 2 a  
    """
    Definition Description:
        This function calls the task 2a to view by country. It also checks for valid input.
    Parameters: none
    """
    def task_two_a(self):
        txt = self.Entry.get()
        if(len(txt) != 45):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        classObject2.view_country(0, txt)   
        return 
        
    #call function for task 2 b
    """
    Definition Description:
        This function calls the task 2b to view by continent. It also checks for valid input.
    Parameters: none
    """
    def task_two_b(self):
        txt = self.Entry.get()
        if(len(txt) != 45):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        classObject2.country_to_continent(txt)
        return
        
    #call function for task 3 a
    """
    Definition Description:
        This function calls the task 3a to view by verbose browser name.
    Parameters: none
    """
    def task_three_a(self):
        classObject3.threea()
        return  
    
    #call function for task 3 b
    """
    Definition Description:
        This function calls the task 3b to view by non-verbose browser name.
    Parameters: none
    """
    def task_three_b(self):
        classObject3.threeb()
        return  
       
    #call function for task 4 a
    """
    Definition Description:
        This function calls the task 4a to print the list of visitors who read a 
        particular document. It also checks for valid input.
    Parameters: none
    """
    def task_four_a(self):
        txt = self.Entry.get()
        if(len(txt) != 45):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        classObject4.getreaders(txt)
        return
    
    #call function for task 4 b
    """
    Definition Description:
        This function calls the task 4b to print the list of documents that were 
        read by a particular visitor. It also checks for valid input.
    Parameters: none
    """
    def task_four_b(self):
        txt = self.Entry.get()
        if(len(txt) != 16):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        classObject4.getvisitors(txt)
        return
    
    #call function for also likes
    """
    Definition Description:
        This function calls the task 4c, 4d, and 5 to print the sorted list of 
        documents that were read by given visitor, and then also display the
        directed graph which shows a relationship between the visitors and the
        documents. It also checks for valid input.
    Parameters: none
    """
    def fn_doc_also_like(self):
        txt = self.Entry.get()
        if(len(txt) < 45+16+2):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        result = [x.strip() for x in txt.split(',')]     
        #you can use input: 9c29d35352609810, 140226194346-101c05c7d744b2644f916d0d76c2c110  
        fourc, lengths = classObject4.alsolikes(result[0], result[1])
        print("Sorted List:")
        counter = Counter(fourc)
        to_print = classObject4.sort_top(lengths, counter)
        print(to_print)
        return
    
    #function for running command line code
    """
    Definition Description:
        This function is hard-coded to run task 7 to simulate a command line EXACTLY as specified by
        the coursework. It also checks for valid input.
    Parameters: none
    """
    def commandline(self):
        txt = self.Entry_cmd.get()
        #use the following statement to split and strip the input
        #this will give us a string list of inputs
        result = [x.strip() for x in txt.split(' ')]
        print(result)
        #flag is used to check for validity of the input
        flag = 0
        if(result[0] == "-f"):
            dataset = result[1]
            print("Filename: ", dataset)
            if(result[2] == "-t"):
                if(result[3] == "2a"):
                    if(result[4] == "-d"):
                        if(len(result[5]) == 45):
                            cmd_doc = result[5]
                            classObject2.view_country(0, cmd_doc)
                        else: flag = 1
                    else: flag = 1
                elif(result[3] == "2b"):
                    if(result[4] == "-d"):
                        if(len(result[5]) == 45):
                            cmd_doc = result[5]
                            classObject2.country_to_continent(cmd_doc)
                        else: flag = 1
                    else: flag = 1
                elif(result[3] == "3a"):
                    classObject3.threea()
                elif(result[3] == "3b"):
                    classObject3.threeb()
                elif(result[3] == "4d"):
                    if(result[4] == "-u"):
                        if(len(result[5]) == 16):
                            if(result[6] == "-d"):
                                if(len(result[7]) == 45):
                                    cmd_user_id = result[5]
                                    cmd_doc_id = result[7]
                                    classObject4.alsolikes(cmd_user_id, cmd_doc_id)
                                else: flag = 1
                            else: flag = 1
                        else: flag = 1
                    else: flag = 1
                else: flag = 1
            else: flag = 1
        else: flag = 1
        
        if(flag == 1):
            messagebox.showinfo("Invalid input!", "Check your input and try again!")
        
        #possible inputs
        #task 2a: -f dataset.json -t 2a -d 120831070849-697c56ab376445eaadd13dbb8b6d34d0       
        #task 2b: -f dataset.json -t 2b -d 120831070849-697c56ab376445eaadd13dbb8b6d34d0 
        #task 3a: -f dataset.json -t 3a    
        #task 3b: -f dataset.json -t 3b
        #task 4d: -f dataset.json -t 4d -u 9c29d35352609810 -d 140226194346-101c05c7d744b2644f916d0d76c2c110         
       
#end of class
                
#main class
if __name__=='__main__':
    app=My_window()
