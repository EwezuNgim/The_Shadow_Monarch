# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:45:03 2023

@author: root
"""

student_scores={}
'''Add Grades'''
student_scores["Harry"]=81
student_scores["Ron"]=78
student_scores["Hermione"]=99
student_scores["Draco"]=74
student_scores["Neville"]=62

for key in student_scores:
    if student_scores[key]>90:
        student_scores[key]="Outstanding"
    else:
        if student_scores[key]>80:
            student_scores[key]="Exceeds expectation"
        else:
            if student_scores[key]>70:
                student_scores[key]="Acceptable"
            else:
                if student_scores[key] <70:
                    student_scores[key]="Fail"
                    
print(student_scores)