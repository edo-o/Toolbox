import tkinter as tk
from tkinter import ttk

def change_text():
    enteredtext = text.get()
    filehuntercommand = f'dir "*{enteredtext}" /s'
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, filehuntercommand)
    
def copy():
    text_in_box = text_display.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box)
    root.update()
    print(text_in_box)

root = tk.Tk()

root.geometry("800x500")
root.title("ToolBox")

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)
notebook.add(tab1, text="File Hunter")
text = tk.Entry(tab1)
text.pack()
button1 = tk.Button(tab1, text="Change Text", command=change_text)
button1.pack()

text_display = tk.Text(tab1)
text_display.pack()

button2 = tk.Button(tab1, text="Copy", command=copy)
button2.pack()

tab2 = tk.Frame(notebook)
# tab3 = tk.Frame(notebook)
# tab4 = tk.Frame(notebook)


notebook.add(tab2, text="tab2")
# notebook.add(tab3, text="tab3")
# notebook.add(tab4, text="tab4")



notebook.pack(fill="x")

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

