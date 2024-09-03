from tkinter import *
import math
import tkinter.messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    # config do update the label
    title_label.config(text="Timer")
    check_marks.config(text="")
    # programı resetleyip starta bastığımızda en başından başlaması için
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    # if its the 8th rep(for 20 min long break):
    if reps % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Time for long break! Watch your time...")
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # if its 2nd 4th 6th rep(for 5 min breaks):
    elif reps % 2 == 0:
        tkinter.messagebox.showinfo(title="Work", message="Time for 5 min break! Get a coffee :)")
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # if its the 1st 3rd 5th 7th rep(for 25 min working):
    else:
        tkinter.messagebox.showinfo(title="Work", message="Working time!")
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += " ✔ "
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=120, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer, state="normal")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=9)
check_marks.grid(column=1, row=3)



window.mainloop()
