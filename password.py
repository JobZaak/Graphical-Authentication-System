from tkinter import messagebox
import copy
import hashlib
from random import randint

import tkinter
from tkinter import *
import custom_button
import main_menu

import utils
from PIL import ImageTk, Image
from tkinter import Entry

from tkinter import Canvas, Label, Entry, StringVar, Frame, BOTH, CENTER
from PIL import Image, ImageTk
import custom_button
import utils
from random import randint
import webbrowser

# Global variable to track login attempts
login_attempts = 0
image_attempts = 0

s_image = [""]
s_image.append("")

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)


# Saves image selected by user
def clicked(canvas, img_name, event):
    canvas.config(highlightthickness=1, highlightbackground="black")
    s_image[0] = img_name;


def add_user(username, password, image):
    # Open the file in append mode to add a new user
    filepath = "credentialImages/orig_credentials.txt"
    with open(filepath, "a") as f:
        # Hash the password
        h = hashlib.new('sha512_256')
        h.update(password.encode())
        hashed_password = h.hexdigest()

        # Write the new user information to the file
        f.write(f"{username} {hashed_password} {image}\n")
        messagebox.showinfo("Login System", "Registration Succefull")
        print("Registration Succefull")


def authenticate(selected_image, selected_password, selected_name):
    global login_attempts  # Use global variable to track attempts
    global image_attempts

    # Perform authentication
    if selected_name == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif selected_name == "" and selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")

    h = hashlib.new('sha512_256')
    h.update(selected_password.encode())
    selected_password = h.hexdigest()
    filepath = "credentialImages/orig_credentials.txt"
    f = open(filepath, "r")
    name = ""
    password = ""
    image = ""
    is_user = False

    while True:
        string = f.readline()
        #print("String read:", string)  # this line for debugging
        if string == "":
            if not is_user:
                print("Username not exist")
                messagebox.showinfo("Login System", "Password is not correct")
            break
        info = string.split(" ")
        #print("Info:", info)  # this line for debugging
        if len(info) < 3:
            #print("Invalid format:", string)
            continue  # Skip processing invalid lines
        name = info[0].rstrip()
        password = info[1].rstrip()
        image = info[2].rstrip()

        if name == selected_name:
            is_user = True
            if password == selected_password:
                if image == selected_image:
                    print("Authenticated!!")
                    
                    messagebox.showinfo("Login System", "Authenticated!!")
                    webbrowser.open("https://jobdoneright.framer.ai/")  # Open the website in the default browser
                    break
                else:
                    image_attempts += 1
                    print("Image attempt:", image_attempts)
                    print("Image is not correct")
                    messagebox.showinfo("Login System", "Image is not correct")
                    break
            else:
                login_attempts += 1
                print("Password is not correct")
                messagebox.showinfo("Login System", "Password is not correct")
                break

                
    # Check if image attempts exceed the limit
    if image_attempts > 0:
        messagebox.showerror("Login System", "Maximum image attempts exceeded. Closing program.")
        exit()  # Close the program if limit exceeded

    # Check if login attempts exceed the limit
    if login_attempts > 2:
        messagebox.showerror("Login System", "Maximum login attempts exceeded. Closing program.")
        exit()  # Close the program if limit exceeded


def create_canvas(window):
    global login_attempts  # Reset login attempts when creating the canvas
    global image_attempts

    login_attempts = 0
    image_attempts = 0

    window.title("Login Page")
    window.geometry("1280x600")

    root = Frame(window, height=600, width=1280)
    root.pack(fill='both', expand=1)

    width = 1280
    height = 600
    img_name1 = "cat"
    img_name2 = "flower"
    img_name3 = "mouse"

    num = randint(0, 2)
    print("Random number =", num)

    imgList = utils.getCredentialImages()

    canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    
    # Add background image
    bg_image = Image.open(r"C:\Users\ASUS\Documents\Graphical-Password-Authentication-System-job\assets\login_image 1.png")
    bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, anchor='nw', image=bg_image)
    canvas.lower(bg_image)  # Ensure it's at the bottom

    #label = Label(root, text="Login Page", font=("Arial", 15, "bold"))
    #canvas.create_window(850, 40, anchor="nw", window=label)

    #user_label = Label(root, text="User name:", font=("Arial", 12, "bold"))
    #canvas.create_window(850, 170, anchor="nw", window=user_label)

    #password_label = Label(root, text="Password:", font=("Arial", 12, "bold"))
    #canvas.create_window(480, 210, anchor="nw", window=password_label)

    user_entry = Entry(root, font=("Arial", 12),width=23)
    user_entry.focus()
    selected_name = user_entry.get()
    canvas.create_window(900, 172, anchor="nw", window=user_entry)

    pas = StringVar()
    password_entry = Entry(root, textvar=pas, font=("Arial", 12),width=23, show="*")
    selected_password = password_entry.get()
    canvas.create_window(900, 233, anchor="nw", window=password_entry)

    canvas2 = Canvas(root, width=110, height=70)
    canvas2.bind("<Button-1>",
                 lambda event: clicked(canvas2, img_name1, event))
    canvas2.place(x=780, y=300)
    img2 = (Image.open("credentialImages/" + imgList[num]))
    img2 = img2.resize((90, 60), Image.BICUBIC if hasattr(Image, 'BICUBIC') else 3)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor="nw", image=img2)

    canvas3 = Canvas(root, width=110, height=70)
    canvas3.bind("<Button-1>",
                 lambda event: clicked(canvas3, img_name2, event))
    canvas3.place(x=940, y=300)
    img3 = (Image.open("credentialImages/" + imgList[num + 3]))
    img3 = img3.resize((90, 60), Image.BICUBIC)
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(10, 10, anchor="nw", image=img3)

    canvas4 = Canvas(root, width=110, height=70)
    canvas4.bind("<Button-1>",
                 lambda event: clicked(canvas4, img_name3, event))
    canvas4.place(x=1100, y=300)
    img4 = (Image.open("credentialImages/" + imgList[num + 6]))
    img4 = img4.resize((90, 60), Image.BICUBIC)
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(10, 10, anchor="nw", image=img4)
     #=================================
     
    # registration button display
    # calls add_user on click with entered credentials
    register = custom_button.TkinterCustomButton(master=root, text="Register", height=40, corner_radius=10,
                     command=lambda: add_user(user_entry.get(), password_entry.get(), s_image[0])).place(x=930, y=500)
                     
    #===============================
    login = custom_button.TkinterCustomButton(master=root, text="Log In", height=40, corner_radius=10,
                                                command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())).place(x=930, y=450)

    custom_button.TkinterCustomButton(master=root, text="Go Back", height=40, corner_radius=00,
                                  command=lambda: load_menu(window, root),bg="red").place(x=60, y=25)

    window.mainloop()


def start(window):
    create_canvas(window)


if __name__ == "__main__":
    window = tkinter.Tk()
    start(window)
