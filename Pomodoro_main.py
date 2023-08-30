from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    check_marks.config(text=" ")
    text1.config(text='Timer')
    canvas.itemconfig(timer_text,text='00:00')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  
    global reps
    reps+=1
    
    if reps%2 !=0:
        text1.config(text='Work')
        count_down(WORK_MIN*60)
    elif reps%2==0 and reps%8 !=0:
        text1.config(text='Short Break')
        count_down(SHORT_BREAK_MIN *60)
    elif reps%8 ==0:
        text1.config(text='Long Break')
        count_down(LONG_BREAK_MIN * 60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
   global timer
   count_min=math.floor(count/60)
   count_sec=count%60
   if count_sec <10:
       count_sec=f"0{count_sec}"
   
   if count>=0:
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    
    timer=window.after(1000, count_down, count - 1)
   if count ==0:
       start_timer()
       done=""
       cycle=math.floor(reps/2)
       for i in range(0,cycle):
           done+='✓'
       check_marks.config(text=done) 
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Time Manager')
#To create a gap between the image and window (it was occupying all available space)
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#highlightthickness removes the border between th ecanvas and window
img=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\pomodoro-start\\tomato.png")
canvas.create_image(100,112, image=img)
timer_text=canvas.create_text(103, 130 , text='00:00', fill='white',font=(FONT_NAME,35,'bold'))

canvas.grid(column=1,row=1)


    
text1=Label(text='Timer',font=('ARIAL',20),fg='green')
text1.grid(row=0, column=1)

start_button=Button(text='Start',command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text='Reset',command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)
count_down(5)
window.mainloop()