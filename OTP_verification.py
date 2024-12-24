from tkinter import Tk, Label, Entry, messagebox, Button, PhotoImage  # Add PhotoImage here
from custom_button import TkinterCustomButton
import smtplib
from email.mime.text import MIMEText
import ssl
import random
import main_menu
from tkinter import Frame
import webbrowser


def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

def start(window):
    window.title("Graphical Authentication System")
    window.geometry("1280x600")
    
    OTP_verification_frame = Frame(window, height=600, width=1280)
    OTP_verification_frame.pack(fill='both', expand=1)
    

    label = Label(OTP_verification_frame, text="OTP Authentication", font=('Calibri', 20))
    label.pack(padx=10, pady=10)

    label = Label(OTP_verification_frame, text="Enter your email address:", font=('Calibri', 20))
    label.pack(padx=10, pady=10)
    
    global email_entry
    email_entry = Entry(OTP_verification_frame, font=('Calibri', 16), bg="lightgray", fg="black", bd=3)
    email_entry.pack(pady=50, padx=50, ipadx=115,)

    # Button to initiate OTP verification
    otp_button = TkinterCustomButton(master=OTP_verification_frame, text="Send OTP", command=send_otp_and_open_verify_window, bg="green")

    otp_button.pack(padx=10, pady=10)

    # Go back button
    go_back_button = TkinterCustomButton(master=window, text="Go Back", command=lambda: load_menu(window, OTP_verification_frame), bg="red")
    go_back_button.pack(padx=10, pady=10)

def send_otp_email(email, otp):
    sender_email = "jobzachariah60@gmail.com"
    app_password = "npsq zovn rlcm pidh"

    message = MIMEText(f"Your OTP is: {otp}")
    message['Subject'] = 'OTP Verification'
    message['From'] = sender_email
    message['To'] = email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, [email], message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)

def send_otp_and_open_verify_window():
    email = email_entry.get()
    global user_otp
    user_otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP

    send_otp_email(email, user_otp)

    global verify_window
    verify_window = Tk()
    verify_window.title("Verify OTP")
    verify_window.geometry("500x200")

    Label(verify_window, text="Enter OTP sent to your email:").pack(pady=10)
    global otp_entry
    otp_entry = Entry(verify_window, show="*")
    otp_entry.pack(pady=5)

    # Submit button
    submit_button = Button(verify_window, text="Submit", command=submit_otp)
    submit_button.pack(pady=10)

    verify_window.mainloop()

def submit_otp():
    entered_otp = otp_entry.get()
    if entered_otp == user_otp:
        messagebox.showinfo("OTP Verification", "OTP verification successful.")
        webbrowser.open("https://www.youtube.com/channel/UCOX-54A_Id2K273nVZ2isTA")  # Open the website in the default browser
        verify_window.destroy()  # Close the OTP verification window
    else:
        messagebox.showerror("OTP Verification", "Invalid OTP, please try again.")

if __name__ == "__main__":
    window = Tk()
    start(window)
