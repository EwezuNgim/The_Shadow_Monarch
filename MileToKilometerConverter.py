# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:44:34 2023

@author: FACULTY OFFICIAL
"""
import tkinter as tk
window=tk.Tk()
window.title('Mile to Km Converter')
#I need an entry bar
#text (Miles) to its right, a label
#distance in kilo under it as a label
#labels either side of it
# A button underneath the result
origin_dist=tk.Entry()
origin_dist.grid(column=2,row=0)

mile=tk.Label(text='Miles')
mile.grid(column=3, row=0)

text1=tk.Label(text='is equal to')
text1.grid(column=1,row=1)

text2=tk.Label(text='Km')
text2.grid(column=3, row=1)

def convert_dist():
    new_val=float(origin_dist.get()) * 1.6
    new_val=round(new_val)
    val=tk.Label(text=str(new_val))
    val.grid(column=2, row=1)
calc=tk.Button(text='Calculate',command=convert_dist)
calc.grid(column=2, row=2)

window.mainloop()