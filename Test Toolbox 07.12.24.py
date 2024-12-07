import tkinter as tk
from tkinter import ttk
import subprocess
import os
import shutil

#-------------------File Hunter (original)----------------------#

def Search_contain(): #Sjekker etter filer som innholder noe
    enteredText = text_original.get()
    fileHunterCommand = f'dir "*{enteredText}*" /s'
    text_display_original.delete(1.0, tk.END)
    text_display_original.insert(tk.END, fileHunterCommand)

def Search_ending_with(): #Sjekker etter filer som slutter på noe
    enteredText = text_original.get()
    fileHunterCommand = f'dir "*{enteredText}" /s'
    text_display_original.delete(1.0, tk.END)
    text_display_original.insert(tk.END, fileHunterCommand)

def Search_starting_with(): #Sjekker etter filer som starter på noe
    enteredText = text_original.get()
    fileHunterCommand = f'dir "{enteredText}*" /s'
    text_display_original.delete(1.0, tk.END)
    text_display_original.insert(tk.END, fileHunterCommand)

def Manual_modification_Search(): #Default så du selv kan endre på commanden
    enteredText = text_original.get()
    fileHunterCommand = f'dir "{enteredText}" /s'
    text_display_original.delete(1.0, tk.END)
    text_display_original.insert(tk.END, fileHunterCommand)

def copy_original(): #Copy command
    text_in_box = text_display_original.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box)
    root.update()

#----------------------File Hunter (V2)---------------------------#

def tab2_change_text(): #Sjekker lokalt etter filer
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

#--------------------System command suggestions--------------------#

def display_command(command, output_widget):
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, command)


def suggest_update_drivers():
    command = "pnputil /scan-devices" #oppdatere drivere
    display_command(command, text_display_command_tab3)

def suggest_list_installed_drivers():
    command = "driverquery" #listere drivere i pcen
    display_command(command, text_display_command_tab3)

def scan_corrupt_files():
    command = "sfc /scannow" #Sjekke for og fixe corrupt system filer
    display_command(command, text_display_command_tab3)

def scan_check_disk():
    command = "chkdsk" #Sjekke for og fixe disk
    display_command(command, text_display_command_tab3)


def suggest_office_repair():
    command = ( #Office repair for 32bit og 64bit maskiner
        "For 32-bit Office:\n"
        "\"C:\\Program Files (x86)\\Common Files\\Microsoft Shared\\ClickToRun\\OfficeC2RClient.exe\" /repair user\n\n"
        "For 64-bit Office:\n"
        "\"C:\\Program Files\\Common Files\\Microsoft Shared\\ClickToRun\\OfficeC2RClient.exe\" /repair user\n\n"
        "Note: Copy the appropriate command for your system architecture."
    )
    display_command(command, text_display_command_tab3)

def system_info():
    command = "systeminfo" #Output system info
    display_command(command, text_display_command_tab3)

def battery_health_report():
    command = "powercfg /batteryreport" #Generer batteri health rapport
    display_command(command, text_display_command_tab3)


#add flere commands her


def copy_command():
    text_in_box = text_display_command_tab3.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box.strip())
    root.update()

#-----------------------Browser og Network commands--------------------------#

def display_browser_command(browser_command, output_widget):
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, browser_command)

def clear_chrome_cache(): #Disse er ikke fact checked
    browser_command = ("rd /s /q \"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cache\"\n"
        "rd /s /q \"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies\"\n\n")
    display_command(browser_command, text_display_command_tab4)

def clear_firefox_cache(): #Disse er ikke fact checked
    browser_command = ("rd /s /q \"%APPDATA%\\Mozilla\\Firefox\\Profiles\\<ProfileName>\\cache2\"\n"
        "del \"%APPDATA%\\Mozilla\\Firefox\\Profiles\\<ProfileName>\\cookies.sqlite\"\n\n")
    display_command(browser_command, text_display_command_tab4)

def clear_edge_cache(): #Disse er ikke fact checked
    browser_command = ("rd /s /q \"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cache\"\n"
        "rd /s /q \"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cookies\"\n\n")
    display_command(browser_command, text_display_command_tab4)

def clear_dns(): #Flusher DNS
    browser_command = "ipconfig /flushdns"
    display_command(browser_command, text_display_command_tab4)

def copy_browser_command(): #Copy command
    text_in_box = text_display_command_tab4.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_in_box.strip())
    root.update()





#-------------------main window setup-----------------------#

root = tk.Tk()
root.geometry("900x700")
root.title("ToolBox")

#-------------------Notebook (tab system)-----------------------#

notebook = ttk.Notebook(root)

#-------------------Tab 1: File Hunter (Original)-----------------------#


tab1 = tk.Frame(notebook)
notebook.add(tab1, text="File Hunter (Original)")
File_hunter_label = tk.Label(tab1, text="File Hunter (Original) for CMD", font=("Arial", 18))
File_hunter_label.pack()

text_original = tk.Entry(tab1)
text_original.pack()


button1_original = tk.Button(tab1, text="Search contain", command=Search_contain)
button1_original.pack()

button2_original = tk.Button(tab1, text="Search ending with", command=Search_ending_with)
button2_original.pack()

button3_original = tk.Button(tab1, text="Search starting with", command=Search_starting_with)
button3_original.pack()

button4_original = tk.Button(tab1, text="Manual modification Search", command=Manual_modification_Search)
button4_original.pack()

text_display_original = tk.Text(tab1)
text_display_original.pack()

button_copy_original = tk.Button(tab1, text="Copy Search Command", command=copy_original)
button_copy_original.pack()

#-------------------Tab 2: File Hunter (V2)-----------------------#

tab2 = tk.Frame(notebook)
notebook.add(tab2, text="File Hunter V2 (Local Search)")

Browser_Network_label = tk.Label(tab2, text="File Hunter V2 (Local Search with CMD)", font=("Arial", 18))
Browser_Network_label.pack()


text_enhanced = tk.Entry(tab2)
text_enhanced.pack()

button1_enhanced = tk.Button(tab2, text="Search", command=tab2_change_text)
button1_enhanced.pack()

text_display_enhanced = tk.Text(tab2)
text_display_enhanced.pack()

button2_enhanced = tk.Button(tab2, text="Copy results", command=tab2_copy)
button2_enhanced.pack()

#-------------------Tab 3: System command suggestions---------------------#

tab3 = tk.Frame(notebook)
notebook.add(tab3, text="System Commands")

System_commands_label = tk.Label(tab3, text="System Commands for CMD", font=("Arial", 18))
System_commands_label.pack()

button_system_info = tk.Button(tab3, text="System Info", command=system_info)
button_system_info.pack()

button_update_drivers = tk.Button(tab3, text="Update Drivers", command=suggest_update_drivers)
button_update_drivers.pack()

button_list_drivers = tk.Button(tab3, text="List Installed Drivers", command=suggest_list_installed_drivers)
button_list_drivers.pack()

button_scan_corrupt_files = tk.Button(tab3, text="Check and Fix Corrupt Files (System Files)", command=scan_corrupt_files)
button_scan_corrupt_files.pack()

button_scan_check_disk = tk.Button(tab3, text="Check and Fix Corrupt Files (Check Disk)", command=scan_check_disk)
button_scan_check_disk.pack()

button_office_repair = tk.Button(tab3, text="Office repair", command=suggest_office_repair)
button_office_repair.pack()

button_office_repair = tk.Button(tab3, text="Office repair", command=battery_health_report)
button_office_repair.pack()


text_display_command_tab3 = tk.Text(tab3)
text_display_command_tab3.pack()

button_copy_command = tk.Button(tab3, text="Copy Command", command=copy_command)
button_copy_command.pack()


#--------------------------Tab 4: Browser og Network------------------#

tab4 = tk.Frame(notebook)
notebook.add(tab4, text="Browser og Network")

Browser_Network_label = tk.Label(tab4, text="Browser og Network commands for CMD", font=("Arial", 18))
Browser_Network_label.pack()

button_clear_chrome_cache = tk.Button(tab4, text="Clear Chrome Cache and Cookies", command=clear_chrome_cache)
button_clear_chrome_cache.pack()

button_clear_firefox_cache = tk.Button(tab4, text="Clear Firefox Cache and Cookies", command=clear_firefox_cache)
button_clear_firefox_cache.pack()

button_clear_edge_cache = tk.Button(tab4, text="Clear Edge Cache and Cookies", command=clear_edge_cache)
button_clear_edge_cache.pack()

button_clear_dns = tk.Button(tab4, text="DNS Flush", command=clear_dns)
button_clear_dns.pack()

text_display_command_tab4 = tk.Text(tab4)
text_display_command_tab4.pack()

button_copy_browser_command = tk.Button(tab4, text="Copy Browser Command", command=copy_browser_command)
button_copy_browser_command.pack()



#------------------------Display notebook------------------------#

notebook.pack(fill="both", expand=True)


# tab3 = tk.Frame(notebook)
# tab4 = tk.Frame(notebook)


# notebook.add(tab3, text="tab3")
# notebook.add(tab4, text="tab4")

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

