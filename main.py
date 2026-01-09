from importlib.resources import contents
import tkinter as tk 
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("File Explorer by Shaaf Iqbal")
root.geometry("500x400")
file_path = tk.StringVar()

path_label = tk.Label(root, textvariable=file_path, wraplength=450)
path_label.pack(pady=10)

def browse_file():
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        file_path.set(path)

browse_btn = tk.Button(root, text="Browse Files", command=browse_file)
browse_btn.pack(pady=5)


text_area = tk.Text(root, height= 15, width=60)
text_area.pack(pady=10)

def open_file():
    path = file_path.get()
    if not path:
        messagebox.showerror("Error", "Koi file select nahi hui")
        return
    try:
      with open(path,"r") as file:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
    except Exception as e:
       messagebox.showerror("Error", str(e))        


open_btn = tk.Button(root, text="Open File", command=open_file)
open_btn.pack(pady=5)

root.mainloop()


