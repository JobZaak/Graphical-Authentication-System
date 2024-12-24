import tkinter
from tkinter import *
import webbrowser
import speech_recognition as sr
from PIL import ImageTk, Image
import os
import random
import utils

import custom_button
import main_menu
import utils

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

original_text = []

def toggle(event, window):
    input_text = []

    def listen_for_speech():
        nonlocal input_text, e  # Add 'e' to the list of nonlocal variables
        global mic_on  # Access mic_on as a global variable
        try:
            if mic_on:  # Check if mic is turned on
                print("Say Something. Say 'stop' in order to stop")
                with sr.Microphone() as source:
                    audio = e.listen(source)  # Listens to audio
                new_input_text = e.recognize_sphinx(audio)  # Recognizes text using speech recognition
                if new_input_text == "stop":  # Break condition
                    input_text.append("stop")
                else:
                    input_text.append(new_input_text)
                    print("Recognized Text:", new_input_text)  # Print the recognized text
                window.after(100, listen_for_speech)  # Schedule the function to be called again after 100 milliseconds
            else:
                window.after(100, listen_for_speech)  # Schedule the function to be called again after 100 milliseconds
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            input_text.append("error")
            window.after(100, listen_for_speech)  # Continue listening for speech
        except sr.RequestError as e:
            print(f"Could not request results from Speech Recognition service; {e}")
            input_text.append("error")
            window.after(100, listen_for_speech)  # Continue listening for speech

    e = sr.Recognizer()  # Recognizes all input devices
    listen_for_speech()

    # Wait for speech input or "stop" command
    window.wait_variable(tkinter.StringVar(value=input_text))

    # Process the collected speech input
    if "stop" in input_text:
        input_text.remove("stop")  # Remove the "stop" command from the list
        input_text = ' '.join(input_text)  # Combine the recognized words into a single string

        input_text = input_text[:-5]  # Removing "stop" from the end of the line
        input_text = input_text.rstrip()  # Removing \n
        input_text = input_text.lower()  # Converting everything to lowercase
        input_text = input_text.replace(' ', '-')  # Replacing spaces with dashes

        print("Original Text = ", original_text[0])
        print("Input Text = ", input_text)

        if original_text[0] == input_text:
            print("Authenticated")
            #webbrowser.open("https://www.youtube.com/channel/UCOX-54A_Id2K273nVZ2isTA")  # Open the website in the default browser
            utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
        else:
            print("Authentication Failed")
            utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

def toggle_mic():
    global mic_on
    mic_on = not mic_on
    if mic_on:
        mic_button.config(text="Mic: On")
        print("Microphone is now ON")
    else:
        mic_button.config(text="Mic: Off")
        print("Microphone is now OFF")

def start(window):
    
     # Attempt to load the obscure images
    try:
        image_files = os.listdir("obscuredImages")
        random_image = random.choice(image_files)
        img = (Image.open(os.path.join("obscuredImages", random_image)))
    except FileNotFoundError:
        print("Error: Obscure images directory not found or empty")
        # Handle the error appropriately, such as displaying an error message to the user
        return
    
    # Get the corresponding authentication keyword
    keyword_file = os.path.join("original_obscure.txt")
    with open(keyword_file, 'r') as file:
        keywords = file.readlines()
    random_keyword = random.choice(keywords).strip()
    
    obscure_frame = Frame(window, height=600, width=1280)
    obscure_frame.pack(fill='both', expand=1)

    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    label = Label(obscure_frame, text="Click on the microphone and speak the words in the following image",
                  font=('Calibri', 20))
    label.pack(padx=40, pady=10)

    canvas = Canvas(obscure_frame, width=450, height=300)
    img = img.resize((450, 300), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.pack(padx=10, pady=10)

    canvas2 = Canvas(obscure_frame, width=200, height=170)
    canvas2.bind("<Button-1>", lambda event: toggle(event, window))
    img2 = (Image.open("assets/mic.jpg"))
    img2 = img2.resize((200, 170), Image.BICUBIC)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor=NW, image=img2)
    canvas2.pack(padx=20, pady=20)

    global mic_on
    mic_on = True  # Set the initial state of mic to be on

    global mic_button
    mic_button = Button(obscure_frame, text="Mic: On", command=toggle_mic)
    mic_button.pack(padx=20, pady=5)

    custom_button.TkinterCustomButton(master=obscure_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, obscure_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    # Store original text
    original_text.append(random_keyword)

    # Use mainloop instead of the infinite loop
    window.mainloop()

if __name__ == "__main__":
    start(Tk())
