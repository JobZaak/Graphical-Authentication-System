# Import the required libraries
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import PhotoImage
import custom_button
import garbled
import OTP_verification
import password
import segments


def load_garbled(window, menu_frame):
    menu_frame.pack_forget()
    garbled.start(window)


def load_OTP_verification(window, menu_frame):
    menu_frame.pack_forget()
    OTP_verification.start(window)

#def load_obscured(window, menu_frame):
    #menu_frame.pack_forget()
    #obscure.start(window) 


def load_segmented(window, menu_frame):
    menu_frame.pack_forget()
    segments.start(window)


def load_password(window, menu_frame):
    menu_frame.pack_forget()
    password.start(window)

def open_link():
    import webbrowser
    # Replace 'your_link_here' with the actual URL you want to open
    webbrowser.open_new("https://www.example.com")

def start(win):
    win.geometry("1280x600")
    #win.title("Graphical Authentication System")

    # Load the background image
    background_image = PhotoImage(file="my_image (2).png")

    menu_frame = Frame(win, height=600, width=1280)
    menu_frame.pack(fill='both', expand=1)

    # Display the background image
    bg_label = Label(menu_frame, image=background_image)
    bg_label.place(relwidth=1, relheight=1)

    #label = Label(menu_frame, text="Graphical Authentication System", font=('Freestyle Script', 54))
    #label.pack(padx=40, pady=30)

    btn_height = 70
    btn_width = 430
    btn_font = ('Trebuchet MS', 14)

    btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Garbled Images", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=00,
                                             command=lambda: load_garbled(win, menu_frame))
    btn1.place(x=336, y=223, anchor=CENTER)
    btn1.config(highlightthickness=0, highlightbackground='white')
    btn1.configure(background=menu_frame.cget('background'))

    btn2 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Segmented Images", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=00,
                                             command=lambda: load_segmented(win, menu_frame))
    btn2.place(x=336, y=461, anchor=CENTER)
    btn2.config(highlightthickness=0, highlightbackground='white')
    btn2.configure(background=menu_frame.cget('background'))


    btn3 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Password/Image Authentication",
                                             text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=00,
                                             command=lambda: load_password(win, menu_frame))
    btn3.place(x=939, y=223, anchor=CENTER)
    btn3.config(highlightthickness=0, highlightbackground='white')
    btn3.configure(background=menu_frame.cget('background'))
    
    btn4 = custom_button.TkinterCustomButton(master=menu_frame, text="OTP_Authentication", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=00,
                                             command=lambda: load_OTP_verification(win, menu_frame))
    btn4.place(x=939, y=461, anchor=CENTER)
    btn4.config(highlightthickness=0, highlightbackground='white')
    btn4.configure(background=menu_frame.cget('background'))


    win.mainloop()


if __name__ == "__main__":
    win = Tk()
    start(win)
