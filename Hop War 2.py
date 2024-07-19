#Hop War 2 

from tkinter import *

gameWidth = 1000
gameHeight = 700

window = Tk()
window.geometry(f'{gameWidth}x{gameHeight}')
window.title("Hop War 2")
window.resizable(False, False)

grass_Dead_Image = PhotoImage('grass_dead_96x96.png')

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.config(background='#98F5F9')

hop_Area = Canvas(window, background='black', width=gameWidth, height=500)
hop_Area.pack()

hop_Area.create_line(0, 440, gameWidth, 440, fill="White", width=5)
hop_Area.create_line(0, 225, gameWidth, 225, fill="White", width=5)

#grass_Dead = hop_Area.create_image(grass_Dead_Image)
#grass_Dead.pack()



    
    







 


window.mainloop()

