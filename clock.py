from tkinter import * #importando oque é necessario para fazer o menu (GUI)
import time  #importanto o tempo.

#estarei utilizando variaveis em ingles pois é mais facil

def display_time():

    hour = str(time.strftime("%H"))
    minute = str(time.strftime("%M"))
    second = str(time.strftime("%S"))
    day = str(time.strftime("%d"))
    month = str(time.strftime("%B"))
    year = str(time.strftime("%Y"))

    #configurando o texto

    hour_label.config(text = hour)
    minute_label.config(text = minute)
    second_label.config(text = second)

    day_label.config(text = day)
    month_label.config(text = month)
    year_label.config(text = year)

    #atualizando a cada 200milisegundos

    hour_label.after(200, display_time)

# Menu

if __name__ == "__main__":
    gui_root = Tk()
    gui_root.title("Relogio Digital")
    #tamanho e posição da janela
    gui_root.geometry("680x290+680+290")
    
    #desativando a opção de mudar o tamanho da janela
    gui_root.resizable(0, 0)
    gui_root.config(bg = "#2C3C3F")

    #settando o icone da janela
    gui_root.iconbitmap("clock_img.ico")

header_frame = Frame(gui_root, bg = "#2C3C3F")
body_frame = Frame(gui_root, bg= "#2C3C3F")

#frames na janela do windows

header_frame.pack(pady = 15)
body_frame.pack()

header_label = Label(
    header_frame,
    text = "Relogio Digital",
    font = ("consolas", "14", "bold"),
    bg = "#2C3C3F",
    fg = "#CAF6FF"
)

header_label.pack()

# Body Frame (configurando como as coisas vao aparecer no menu)

hour_label = Label(  
    body_frame,  
    text = "00",  
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
    )  
colon_label_one = Label(  
    body_frame,  
    text = ":",  
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
    )  
minute_label = Label(  
    body_frame,  
    text = "00",  
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
    )  
colon_label_two = Label(  
    body_frame,  
    text = ":",  
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
    )  
second_label = Label(  
    body_frame,  
    text = "00",  
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
    )
day_label = Label(
    body_frame,
    text = "00",
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
)
month_label = Label(
    body_frame,
    text = "000000",
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
)
year_label = Label(
    body_frame,
    text = "0000",
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
)
of_one = Label(
    body_frame,
    text = "of",
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
)
of_two = Label(
    body_frame,
    text = "of",
    font = ("nice sugar", "48"),  
    bg = "#2C3C3F",  
    fg = "#00D2FF"  
)


hour_label.grid(row = 0, column = 0, padx = 5, pady = 5)  
colon_label_one.grid(row = 0, column = 1, padx = 5, pady = 5)  
minute_label.grid(row = 0, column = 2, padx = 5, pady = 5)  
colon_label_two.grid(row = 0, column = 3, padx = 5, pady = 5)  
second_label.grid(row = 0, column = 4, padx = 5, pady = 5)  
day_label.grid(row = 1, column = 0, padx = 5, pady = 5)
of_one.grid(row = 1, column = 1, padx = 5, pady = 5)
month_label.grid(row = 1, column = 2, padx = 5, pady = 5)
of_two.grid(row = 1, column = 3, padx = 5, pady = 5)
year_label.grid(row = 1, column = 4, padx = 5, pady = 5)


display_time()
gui_root.mainloop()  




