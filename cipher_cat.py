import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ciphers import (
    CaesarCipher,
    VigenereCipher,
    SubstitutionCipher,
    AffineCipher,
    TranspositionCipher,
    MorseCodeCipher,
)  # Ensure these modules are implemented
import os
import sys


def resource_path(relative_path):
    """Get the absolute path to resource, works for development and PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Global variables to hold the image references
bg_photo_initial = None
bg_photo = None
global_selected_cipher = None  # Initialize global_selected_cipher
cipher_window = None  # Initialize cipher_window


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius,
        y1,
        x1 + radius,
        y1,
        x2 - radius,
        y1,
        x2 - radius,
        y1,
        x2,
        y1,
        x2,
        y1 + radius,
        x2,
        y1 + radius,
        x2,
        y2 - radius,
        x2,
        y2 - radius,
        x2,
        y2,
        x2 - radius,
        y2,
        x2 - radius,
        y2,
        x1 + radius,
        y2,
        x1 + radius,
        y2,
        x1,
        y2,
        x1,
        y2 - radius,
        x1,
        y2 - radius,
        x1,
        y1 + radius,
        x1,
        y1 + radius,
        x1,
        y1,
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)


def open_cipher_window():
    global cipher_window, content_frame, bg_photo

    if cipher_window is not None:
        cipher_window.destroy()

    cipher_window = tk.Toplevel()  # Use Toplevel to allow multiple windows
    cipher_window.title("Cipher GUI")

    # Set the size of the window to 1920x1080 and prevent resizing
    cipher_window.geometry("1920x1080")
    cipher_window.resizable(False, False)

    # Load the background image
    bg_image_original = Image.open(resource_path("images/CIpherCat.png"))

    bg_image_resized = bg_image_original.resize(
        (1920, 1080), Image.LANCZOS
    )  # Set size to match window
    bg_photo = ImageTk.PhotoImage(bg_image_resized)

    # Create and place the background label
    background_label = tk.Label(cipher_window, image=bg_photo, bg="white")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = bg_photo  # Keep a reference to avoid garbage collection

    # Create a frame to hold the content and center it
    content_frame = tk.Frame(cipher_window, bg="#efefef", padx=20, pady=20)
    content_frame.place(
        x=750, rely=0.5, anchor="center"
    )  # Adjusted x value to move frame more to the left

    # Initialize the GUI for the default cipher
    update_cipher_options(None)

    # Add the Back button with image
    back_image = Image.open(
        resource_path("images/back_button_image.png")
    )  # Load image for back button
    back_image_resized = back_image.resize(
        (150, 100), Image.LANCZOS
    )  # Resize if needed
    back_photo = ImageTk.PhotoImage(back_image_resized)
    back_button = tk.Button(
        cipher_window, image=back_photo, command=go_back, bd=0, bg="#efefef"
    )
    back_button.place(x=25, y=20)  # Positioning the button in the top-left corner
    back_button.image = back_photo  # Keep a reference to avoid garbage collection


def go_back():
    global cipher_window, global_selected_cipher

    if cipher_window:
        cipher_window.destroy()
        cipher_window = None  # Reset the cipher window global variable

    global_selected_cipher = None  # Reset the selected cipher
    initial_window.deiconify()  # Show the initial window again


def update_cipher_options(event=None):  # Add default parameter for event
    cipher_type = global_selected_cipher

    # Clear existing widgets in the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()  # Use destroy instead of pack_forget

    # Define a custom font
    custom_font = ("ISOCPEUR", 24)
    entry_font = ("Lucida Console", 14)

    # Add widgets based on the selected cipher
    tk.Label(content_frame, text="MESSAGE", font=custom_font).pack(
        padx=10, pady=10, anchor="center"
    )

    global message_entry
    canvas_message = tk.Canvas(
        content_frame, width=500, height=50, bg="#efefef", highlightthickness=0
    )
    canvas_message.pack(padx=10, pady=10, anchor="center")
    create_rounded_rectangle(canvas_message, 0, 0, 500, 50, radius=20, fill="#3d3d3d")

    message_entry = tk.Entry(
        canvas_message,
        width=50,
        font=entry_font,
        bg="#3d3d3d",
        fg="white",
        insertbackground="white",
        relief="flat",
    )
    message_entry.place(x=5, y=5, width=490, height=40)

    # Only show key entry if necessary
    if cipher_type in ["Caesar Cipher", "Affine Cipher"]:
        tk.Label(content_frame, text="SHIFT", font=custom_font).pack(
            padx=10, pady=10, anchor="center"
        )

        global shift_entry
        canvas_shift = tk.Canvas(
            content_frame, width=500, height=50, bg="#efefef", highlightthickness=0
        )
        canvas_shift.pack(padx=10, pady=10, anchor="center")
        create_rounded_rectangle(canvas_shift, 0, 0, 500, 50, radius=20, fill="#3d3d3d")

        shift_entry = tk.Entry(
            canvas_shift,
            width=50,
            font=entry_font,
            bg="#3d3d3d",
            fg="white",
            insertbackground="white",
            relief="flat",
        )
        shift_entry.place(x=5, y=5, width=490, height=40)

    if cipher_type in [
        "Vigenere Cipher",
        "Substitution Cipher",
        "Transposition Cipher",
    ]:
        tk.Label(content_frame, text="Key:", font=custom_font).pack(
            padx=10, pady=10, anchor="center"
        )

        global key_entry
        canvas_key = tk.Canvas(
            content_frame, width=500, height=50, bg="#efefef", highlightthickness=0
        )
        canvas_key.pack(padx=10, pady=10, anchor="center")
        create_rounded_rectangle(canvas_key, 0, 0, 500, 50, radius=20, fill="#3d3d3d")

        key_entry = tk.Entry(
            canvas_key,
            width=50,
            font=entry_font,
            bg="#3d3d3d",
            fg="white",
            insertbackground="white",
            relief="flat",
        )
        key_entry.place(x=5, y=5, width=490, height=40)

    # Add Encrypt and Decrypt buttons
    global encrypt_button, decrypt_button, result_label, result_text
    button_frame = tk.Frame(content_frame, bg="#efefef")
    button_frame.pack(padx=10, pady=10, anchor="center")

    button_style = {
        "font": ("ISOCTEUR", 12),
        "bg": "black",
        "fg": "white",
        "activebackground": "grey",
        "activeforeground": "white",
        "width": 7,
        "height": 1,
        "relief": "flat",
    }

    canvas_encrypt = tk.Canvas(
        button_frame, width=105, height=40, bg="#efefef", highlightthickness=0
    )
    canvas_encrypt.pack(side="left", padx=10)
    create_rounded_rectangle(canvas_encrypt, 0, 0, 105, 40, radius=10, fill="black")

    encrypt_button = tk.Button(
        canvas_encrypt,
        text="ENCRYPT",
        command=lambda: perform_cipher("Encrypt"),
        **button_style,
    )
    encrypt_button.place(x=5, y=5, width=95, height=30)

    canvas_decrypt = tk.Canvas(
        button_frame, width=105, height=40, bg="#efefef", highlightthickness=0
    )
    canvas_decrypt.pack(side="right", padx=10)
    create_rounded_rectangle(canvas_decrypt, 0, 0, 105, 40, radius=10, fill="black")

    decrypt_button = tk.Button(
        canvas_decrypt,
        text="DECRYPT",
        command=lambda: perform_cipher("Decrypt"),
        **button_style,
    )
    decrypt_button.place(x=5, y=5, width=95, height=30)

    tk.Label(content_frame, text="RESULT", font=custom_font).pack(
        padx=10, pady=10, anchor="center"
    )

    canvas_result = tk.Canvas(
        content_frame, width=600, height=100, bg="#efefef", highlightthickness=0
    )
    canvas_result.pack(padx=10, pady=10, anchor="center")
    create_rounded_rectangle(canvas_result, 0, 0, 600, 100, radius=20, fill="#3d3d3d")

    result_text = tk.Text(
        canvas_result,
        height=4,
        width=60,
        wrap=tk.WORD,
        font=entry_font,
        bg="#3d3d3d",
        fg="white",
        insertbackground="white",
        relief="flat",
    )
    result_text.place(x=5, y=5, width=590, height=90)


def perform_cipher(action):
    cipher_type = global_selected_cipher
    message = message_entry.get()

    # Get shift value if applicable
    shift = None
    if cipher_type in ["Caesar Cipher", "Affine Cipher"] and "shift_entry" in globals():
        shift = shift_entry.get()
        try:
            shift = int(shift)
        except ValueError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Shift must be an integer.")
            return

    # Get key value if applicable
    key = None
    if (
        cipher_type
        in ["Vigenere Cipher", "Substitution Cipher", "Transposition Cipher"]
        and "key_entry" in globals()
    ):
        key = key_entry.get()

    # Select the cipher based on the global selection
    cipher = None
    if cipher_type == "Caesar Cipher":
        cipher = CaesarCipher(message, shift)
    elif cipher_type == "Vigenere Cipher":
        cipher = VigenereCipher(message, key)
    elif cipher_type == "Substitution Cipher":
        cipher = SubstitutionCipher(message, key)
    elif cipher_type == "Affine Cipher":
        cipher = AffineCipher(message, shift)
    elif cipher_type == "Transposition Cipher":
        cipher = TranspositionCipher(message, key)
    elif cipher_type == "Morse Code":
        if action == "Encrypt":
            result = MorseCodeCipher.encode(message)
        else:
            result = MorseCodeCipher.decode(message)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
        return
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Unknown cipher type.")
        return

    # Perform the encryption or decryption
    if action == "Encrypt":
        result = cipher.encrypt()
    else:
        result = cipher.decrypt()

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)


def select_cipher(cipher_type):
    global global_selected_cipher
    global_selected_cipher = cipher_type

    # Hide initial screen and show cipher window
    initial_window.withdraw()  # Hide the initial window
    open_cipher_window()


def exit_application():
    initial_window.destroy()  # Close the initial window and exit the application


# Create the initial window for cipher selection
initial_window = tk.Tk()
initial_window.title("Select Cipher")

# Set the size of the window and prevent resizing
initial_window.geometry("1920x1080")
initial_window.resizable(False, False)

# Load the background image for the initial window
bg_image_initial = Image.open(resource_path("images/CIpherCat1.png"))

bg_image_initial = bg_image_initial.resize(
    (1920, 1080), Image.LANCZOS
)  # Set size to match window
bg_photo_initial = ImageTk.PhotoImage(bg_image_initial)

# Create and place the background label for the initial window
background_label_initial = tk.Label(initial_window, image=bg_photo_initial, bg="white")
background_label_initial.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the content and align it to the center vertically
initial_frame = tk.Frame(initial_window, bg="#efefef", padx=20, pady=20)
initial_frame.place(
    x=675, y=75, rely=0.5, anchor="center"  # Center horizontally with adjusted x value
)

# Create and place text options for cipher selection in a 3x2 grid
cipher_buttons_frame = tk.Frame(initial_frame, bg="#efefef")
cipher_buttons_frame.grid(row=0, column=0, padx=10, pady=10)

cipher_buttons = [
    "Caesar Cipher",
    "Vigenere Cipher",
    "Substitution Cipher",
    "Affine Cipher",
    "Transposition Cipher",
    "Morse Code",
]

for idx, cipher in enumerate(cipher_buttons):
    label = tk.Label(
        cipher_buttons_frame,
        text=cipher,
        font=("ISOCPEUR", 30),
        bg="#efefef",
        cursor="hand2",
    )
    label.grid(row=idx % 3, column=idx // 3, padx=10, pady=10)
    label.bind("<Button-1>", lambda e, c=cipher: select_cipher(c))

# Add Exit button with image
exit_image = Image.open(resource_path("images/exit.png"))
# Load image for exit button
exit_image_resized = exit_image.resize((150, 75), Image.LANCZOS)  # Resize if needed
exit_photo = ImageTk.PhotoImage(exit_image_resized)
exit_button = tk.Button(
    initial_window, image=exit_photo, command=exit_application, bd=0, bg="#efefef"
)
exit_button.place(x=30, y=950)  # Positioning the button at the bottom-left corner
exit_button.image = exit_photo  # Keep a reference to avoid garbage collection

# Start the main event loop
initial_window.mainloop()
