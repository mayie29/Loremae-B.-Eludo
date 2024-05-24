import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as scrolledtext

def copy_text():
    selected_text = text_box.get("sel.first", "sel.last")
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def paste_text():
    text_to_paste = root.clipboard_get()
    text_box.insert(tk.INSERT, text_to_paste)

def save_text():
    text_to_save = text_box.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)

root = tk.Tk()
root.title("Copy&Paste")
root.configure(bg="lightblue")

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_box.pack(fill=tk.BOTH, expand=True)

copy_button = tk.Button(root, text="Copy", command=copy_text, bg="#4CAF50", fg="white")  
copy_button.pack(side=tk.LEFT, padx=5, pady=5)

paste_button = tk.Button(root, text="Paste", command=paste_text, bg="#008CBA", fg="white")  
paste_button.pack(side=tk.LEFT, padx=5, pady=5)

save_button = tk.Button(root, text="Save", command=save_text, bg="#f44336", fg="white")  
save_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()