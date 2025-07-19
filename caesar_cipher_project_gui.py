import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = int(shift) if mode == 'encrypt' else -int(shift)

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def handle_encrypt():
    text = entry_text.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Shift", "Shift must be a number.")
        return
    result = caesar_cipher(text, shift, 'encrypt')
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state='disabled')

def handle_decrypt():
    text = entry_text.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Shift", "Shift must be a number.")
        return
    result = caesar_cipher(text, shift, 'decrypt')
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state='disabled')

def handle_clear():
    entry_text.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.config(state='disabled')

def handle_copy():
    output = output_text.get(1.0, tk.END).strip()
    if output:
        window.clipboard_clear()
        window.clipboard_append(output)
        messagebox.showinfo("Copied", "Result copied to clipboard.")

def show_about():
    messagebox.showinfo("About", "Caesar Cipher GUI\nDeveloped using Python Tkinter.\nAn internship project demonstrating classical encryption.")

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher GUI Tool")
window.geometry("500x400")
window.config(bg="#f0f8ff")

tk.Label(window, text="Caesar Cipher Encryption/Decryption", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=10)

frame = tk.Frame(window, bg="#f0f8ff")
frame.pack(pady=10)

tk.Label(frame, text="Enter Message:", bg="#f0f8ff").grid(row=0, column=0, padx=5, sticky="w")
entry_text = tk.Entry(frame, width=50)
entry_text.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Shift Value:", bg="#f0f8ff").grid(row=1, column=0, padx=5, sticky="w")
entry_shift = tk.Entry(frame, width=10)
entry_shift.grid(row=1, column=1, pady=5, sticky="w")

btn_frame = tk.Frame(window, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encrypt", width=12, bg="#90ee90", command=handle_encrypt).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decrypt", width=12, bg="#ffcccb", command=handle_decrypt).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Clear", width=12, bg="#fdfd96", command=handle_clear).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Copy Result", width=12, bg="#add8e6", command=handle_copy).grid(row=0, column=3, padx=5)

tk.Label(window, text="Result:", bg="#f0f8ff").pack()
output_text = tk.Text(window, height=5, width=60, state='disabled')
output_text.pack()

tk.Button(window, text="About", command=show_about, bg="#d3d3d3").pack(pady=5)

window.mainloop()
