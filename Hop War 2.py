from tkinter import *

gameWidth = 900
gameHeight = 700

window = Tk()
window.geometry(f'{gameWidth}x{gameHeight}')
window.title("Hop War 2")
window.resizable(False, False)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.config(background='#98F5F9')

hop_Area = Canvas(window, background='black', width=gameWidth, height=gameHeight - gameHeight * 0.30)
hop_Area.pack()
 


window.mainloop()

