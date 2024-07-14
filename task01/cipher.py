import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_value.get())
        encrypted_text = caesar_encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_value.get())
        decrypted_text = caesar_decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Load background image
background_image = Image.open("scenery.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='lightblue', bd=5, relief='ridge')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Style for rounded corners
style = ttk.Style()
style.configure("TText", padding=5, relief="flat", background="white", borderwidth=0)
style.map("TText",
          bordercolor=[('focus', 'blue'), ('!focus', 'gray')],
          borderwidth=[('focus', 2), ('!focus', 1)])

# Create and place the widgets inside the frame
tk.Label(frame, text="Enter your message:", bg='lightblue').grid(row=0, column=0, padx=10, pady=10)
input_text = tk.Text(frame, height=5, width=50, wrap=tk.WORD, relief="flat", highlightthickness=2, bd=5)
input_text.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Enter shift value:", bg='lightblue').grid(row=1, column=0, padx=10, pady=10)
shift_value = ttk.Entry(frame, width=5)
shift_value.grid(row=1, column=1, padx=10, pady=10, sticky='w')

encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(frame, text="Output message:", bg='lightblue').grid(row=3, column=0, padx=10, pady=10)
output_text = tk.Text(frame, height=5, width=50, wrap=tk.WORD, relief="flat", highlightthickness=2, bd=5)
output_text.grid(row=3, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
