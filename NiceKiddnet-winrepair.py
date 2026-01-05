#!/usr/bin/env python

from tkinter import Tk, Toplevel, Label, Button, Entry, StringVar, messagebox
import random # Import the random module for random positioning

SECRET_CODE = "sesame"
PRANK_MESSAGE = "sorry, we couldn't do that! "

def open_prank_popup():
    popup = Toplevel()
    popup.title("NiceKiddnet-winrepair.py")
    popup.geometry("350x170")
    popup.resizable(False, False) 
    popup.attributes("-topmost", True)

    # Function to reposition the popup randomly
    def move_popup_randomly():
        # Get screen dimensions
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()

        # Get popup dimensions
        popup_width = popup.winfo_width()
        popup_height = popup.winfo_height()

        # Calculate random new coordinates, ensuring it stays on screen
        new_x = random.randint(0, screen_width - popup_width)
        new_y = random.randint(0, screen_height - popup_height)

        popup.geometry(f'+{new_x}+{new_y}')

    # Initial centering of the popup
    popup.update_idletasks() # Ensure geometry is calculated
    move_popup_randomly() # Call it once to position it initially (or you can keep initial centering)

    entered_code = StringVar()

    Label(popup, text="do you know the code? ;) ", font=("Arial", 12, "bold"), fg="red").pack(pady=10)
    Label(popup, text="Enter the secret code:").pack(pady=5)
    code_entry = Entry(popup, textvariable=entered_code, show="*")
    code_entry.pack(pady=5)
    code_entry.focus_set()

    def check_code():
        if entered_code.get() == SECRET_CODE:
            popup.destroy()
            messagebox.showinfo("congrats! You beat the malware. Share it so someone. Or delete it. Idc. - NiceKidd")
        else:
            messagebox.showerror("Access Denied", PRANK_MESSAGE)
            entered_code.set("") 
            code_entry.focus_set()
            move_popup_randomly() # <--- CALL THE MOVE FUNCTION HERE!

    check_button = Button(popup, text="Check Code", command=check_code, width=15, height=2, bg="green", fg="white", font=("Arial", 10, "bold"))
    check_button.pack(pady=10)

    popup.protocol("WM_DELETE_WINDOW", check_code)
    popup.grab_set()

root = Tk()
root.withdraw() 

open_prank_popup()
root.mainloop()