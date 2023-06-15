import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import pytesseract
import io
from tkinter import messagebox


def extract_text(image):
    try:
        text = pytesseract.image_to_string(image, lang='tur')
        return text
    except IOError:
        return None


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        text = extract_text(image)
        if text:
            result_text.set(text)
        else:
            result_text.set("Error extracting text!")


def on_paste(event):
    try:
        image = ImageGrab.grabclipboard()
        if image is None:
            raise tk.TclError
        text = extract_text(image)

        if text:
            result_text.set(text)
        else:
            result_text.set("Error extracting text!")
    except tk.TclError:
        messagebox.showerror("Error", "No image found in clipboard!")


def copy_text():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())


root = tk.Tk()
root.title("Image Text Extraction")
root.geometry("400x350")

title_label = tk.Label(
    root, text="Image Text Extraction", font=("Helvetica", 16))
title_label.pack(pady=10)

select_button = tk.Button(root, text="Select Picture", command=open_file)
select_button.pack(pady=10)

drop_label = tk.Label(root, text="Press Ctrl+V to paste a screenshot",
                      font=("Helvetica", 12), bd=1, relief="solid", height=5)
drop_label.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
result_label.pack(pady=20)

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Copy", command=copy_text)


def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)


result_label.bind("<Button-3>", show_context_menu)

root.bind("<Control-v>", on_paste)

root.mainloop()
