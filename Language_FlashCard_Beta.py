BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
import time
data=pd.read_csv("C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\data\\french_words.csv")
#new_data=data.to_dict(orient='records')

window=Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas=Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
img_card=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\images\\card_front.png")

word='word'
#new_heading=canvas.create_text(400,150,text='English', fill='white', font=('Ariel',40,'italic'))
new_card=PhotoImage("C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\images\\card_back.png")
#row=random.randint(1, 100)
lang='English'
learnt=pd.DataFrame(columns=['French','English'])
#to_learn_dict={"French":current , "English":trans }
#----------------------------------------- CHANGE WORDS ----------------------------------------------
def known():
    global row
    global current
    global trans
    global learnt
    global new_word
    default()
    #current=random.choice(data)
    row=random.randint(1, data.shape[0])
    current=data.iloc[row,0]
    trans=data.iloc[row,1]
    new_word=canvas.itemconfig(french_word,text=current,fill='black')
    #save known words to 
    learnt=learnt.append({"French":new_word , "English":trans}, ignore_index=True)
    #leave only unknown ones 
    ind=data.index[data['French']==current].to_list()[0]
    data.drop(ind,inplace=True)
    
    ''' row=random.randint(1, len(to_learn))
       current=to_learn.iloc[row,0]
       canvas.itemconfig(french_word,text=current,fill='black') 
    '''
    #t0_learn.add()
    window.after(3000,k_flip)
    #canvas.itemconfig(new_text, text=heading)


   
#-------------------------------------------     TRANSLATE      ------------------------------------------------------
def k_flip():
    global translation
    canvas.itemconfig(old_img, image=new_card)
    '''else:
        trans=to_learn.iloc[row,1]
        canvas.itemconfig(old_img, image=new_card)
    '''
    #global previous_img
    #previous_img = canvas.itemcget(old_img, "image")
    #canvas.itemconfig(current,text= trans)
    translation=canvas.itemconfig(french_word,text=trans,fill='white')
    canvas.itemconfig(heading, text=lang,fill='white')
    
def u_flip():
    n_trans=data.iloc[n_row,1]
    global translation
    canvas.itemconfig(old_img, image=new_card)
    '''else:
        trans=to_learn.iloc[row,1]
        canvas.itemconfig(old_img, image=new_card)
    '''
    #global previous_img
    #previous_img = canvas.itemcget(old_img, "image")
    #canvas.itemconfig(current,text= trans)
    translation=canvas.itemconfig(french_word,text=n_trans,fill='white')
    canvas.itemconfig(heading, text=lang,fill='white')
    
#-----------------------------------------------------------------------------------------------------------------------
def unknown():
    global n_row
    default()
    #learnt=learnt.append({"French":new_word , "English":trans}, ignore_index=True)
    n_row=random.randint(1, data.shape[0])
    current=data.iloc[n_row,0]
    
    canvas.itemconfig(french_word,text=current,fill='black')
    window.after(3000,u_flip)    
    #halt=window.after_cancel(tk.after_id )
def default():
    canvas.itemconfig(old_img, image=prev_img)
    #canvas.itemconfig(current,text= trans)
    canvas.itemconfig(heading, text='French',fill='black')
'''NEXT
only words the user dowsn't know should popup when next they use the app'

 '''
    
old_img=canvas.create_image(400,250,image=img_card)
prev_img=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\images\\card_front.png")
heading=canvas.create_text(400,150,text='French', fill='black', font=('Ariel',40,'italic'))

french_word=canvas.create_text(400,263,text=word, fill='black', font=('Ariel',40,'italic'))
canvas.grid(row=0,column=0,columnspan=2)
tick_img=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\images\\right.png")
tick_button=Button(image=tick_img, highlightthickness=0,command=known)
tick_button.grid(row=1, column=1)
cross_img=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\flash-card-project-start\\images\\wrong.png")

cross_button=Button(image=cross_img, highlightthickness=0,command=unknown)
cross_button.grid(row=1, column=0)
#window.after(5000,flip())









window.mainloop()