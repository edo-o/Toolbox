import tkinter as tk
from tkinter import ttk
import subprocess

def original_change_text():
    enteredText = text_original.get()
    fileHunterCommand = f'dir "*{enteredText}" /s'
    text_display_original.delete(1.0, tk.END)
    text_display_original.insert(tk.END, fileHunterCommand)

def copy_original():
    text_in_box = text_display_original.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box)
    root.update()
    

def tab2_change_text():
    enteredText = text_enhanced.get()
    fileHunterCommand = f'dir *{enteredText} /s /b'

    try:
        output = subprocess.check_output(fileHunterCommand, shell = True, text = True, stderr = subprocess.DEVNULL)
        text_display_enhanced.delete(1.0, tk.END)
        text_display_enhanced.insert(tk.END, output)

    except subprocess.CalledProcessError:
        text_display_enhanced.delete(1.0, tk.END)
        text_display_enhanced.insert(tk.END, "Ingen filer funnet :/")
    
def tab2_copy():
    text_in_box = text_display_enhanced.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box)
    root.update()

root = tk.Tk()
root.geometry("800x500")
root.title("ToolBox")

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)
notebook.add(tab1, text="File Hunter (Original)")


text_original = tk.Entry(tab1)
text_original.pack()


button1_original = tk.Button(tab1, text="Search", command=original_change_text)
button1_original.pack()

text_display_original = tk.Text(tab1)
text_display_original.pack()

button2_original = tk.Button(tab1, text="Copy", command=copy_original)
button2_original.pack()

tab2 = tk.Frame(notebook)
notebook.add(tab2, text="File Hunter (V2)")

text_enhanced = tk.Entry(tab2)
text_enhanced.pack()

button1_enhanced = tk.Button(tab2, text="Search", command=tab2_change_text)
button1_enhanced.pack()

text_display_enhanced = tk.Text(tab2)
text_display_enhanced.pack()

button2_enhanced = tk.Button(tab2, text="Copy results", command=tab2_copy)
button2_enhanced.pack()



# tab3 = tk.Frame(notebook)
# tab4 = tk.Frame(notebook)


# notebook.add(tab3, text="tab3")
# notebook.add(tab4, text="tab4")



notebook.pack(fill="both", expand=True)

# label = tk.Label(root, text="File Finder", font=("Arial", 18))
# label.pack()

# textbox = tk.Text(root, height=1, font=("Arial", 18))
# textbox.pack()



# entry = tk.Entry(root)
# entry.pack()

# button = tk.Button(root, text="Generate")
# button.pack()

# label1 = tk.Label(root, text="Output CMD Command:", font=("Arial", 18))
# label1.pack()

# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# #buttonframe.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonframe, text="1", font=("Arial", 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

# buttonframe.pack(fill="x")

# textbox = tk.Text(root, height=1, font=("Arial", 18))
# textbox.pack()

root.mainloop()

