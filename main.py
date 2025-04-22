from tkinter import *
import math
from pygments import highlight

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps =0
Timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(Timer)
    canvas.itemconfig(timer, text="00:00")
    timer_set.config(text="Timer",fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps+=1
    work_sec = WORK_MIN *60

    short_break_sec = SHORT_BREAK_MIN * 60

    long_break_sec = LONG_BREAK_MIN * 60
#if its the 1st/3rd/5th/7th rep:


    if reps%2!=0:
     timer_set.config(text="Work time", fg=RED,bg=YELLOW)
     count_down(work_sec)
    #if its the 8th rep:
    elif reps==8:
       timer_set.config(text="Long Break", fg=GREEN, bg=YELLOW)
       count_down(long_break_sec)
    #if it's 2nd/4th/6th rep:

    elif reps%2==0:
       timer_set.config(text="short break", fg=PINK, bg=YELLOW)
       count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec=count % 60
    if count_sec==0:
       count_sec="00"
    elif count_sec<=9:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")

    if count>0:
        global Timer

        Timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ''
        work_sessions = reps/2
        for _ in range(math.floor(work_sessions)):
            mark = "✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

photo_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo_img)
canvas.grid(column=3,row=3)

timer = canvas.create_text(100,130,text="00:00",font=FONT_NAME,fill="white")
canvas.grid(column=3,row=2)
timer_set = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_set.grid(column=3,row=0)
start_button = Button(text="start",bg="white",highlightthickness=0,command=start_timer)
start_button.grid(column=2,row=4)
reset_button = Button(text="Reset",bg="white",highlightthickness=0,command=reset_timer)
reset_button.grid(column=5,row=4)
check_mark = Label(fg=GREEN,bg=YELLOW,highlightthickness=0)
check_mark.grid(column=3,row=5)

window.mainloop()