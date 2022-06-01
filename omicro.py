#/ijp python compiled
class var(object):
    def __init__(self): object.__setattr__(self, "_types", {})
    def set_type(self, name, _type): self._types[name] = _type
    def __setattr__(self, name, value):
        _type = self._types.get(name)
        if _type:
            if type(value) is not _type:
                raise ValueError(
                    "Variable type conflict assigning '{}': was {} is {}".format(
                    name, _type, type(value)))
        else:
            self._types[name] = type(value)
        object.__setattr__(self, name, value)
v = var()
from tkinter import *
from pygments import highlight
from tkinter import colorchooser
import subprocess
from tkinter import ttk, filedialog, messagebox
from tkcode import CodeEditor
from customtkinter import CTkEntry, set_appearance_mode, CTkButton, CTkInputDialog, CTkFrame
import ntpath, platform
set_appearance_mode("light")
v.file_path = ""
langs = str("Python")
block_true = str(False)
name = str("Orcim - Python Code Editor")
filenamee = str("hello.ijp")
top_bg = str("#272727")
top_fg = str('white')
bg = str("#373736")
fg = str("#E4E4E0")
white = str('white')
black = str('black')
monokai = str("monokai")
dracula = str("monokai")
font_family = str("Consolas")
font_size = 13
fs = str(font_size-3)
terminal_bg = str("#262626")
terminal_fg = str("#A1E892")
terminal_bg_light = str("#4C4C4C")
ask_yes_text = str("Your file is not saved, and this could result in loss of work, anger, desperssion and rage quiting")
ask_yes_heading = str("Are you sure you want to open?")
filenamee = str("Untitled File")
root = Tk()
root.title(name)
root.geometry("700x500")
root.configure(bg=top_bg)
terminal = Frame(root, bg=black, width=20)
root.option_add("*tearOff", 0)
code_frame = Frame(root, bg=black)
code_editor = CodeEditor(
    code_frame,
    width=20,
    height=10,
    language=langs,
    highlighter=monokai,
    autofocus=True,
    blockcursor=block_true,
    font = (font_family, font_size),
    insertofftime=0,
    padx=7,
    pady=7,
    bd=2,
    selectbackground='white',
    selectforeground='black',
    startline=1,
    undo=True,
    wrap=WORD
)
def save_file():
    global curr
    curr = code_editor.get("1.0", "end-1c")
    print(f"Text: {curr}")
    try:
        with open(v.file_path, "w") as e:
            e.truncate()
            e.write(curr)
            e.close()
    except NameError: save_as_file()
    except FileNotFoundError: save_as_file()
def open_file():
    if code_editor.get("1.0", "end-1c") != "": real_file_open()
    else: e_real_file_open()
topbar = Frame(bg=top_bg, bd=1)
topbar.pack(side=TOP, fill='x', pady=2, padx=2)
a_frame = Frame(bg='black', bd=0, height=1)
a_frame.pack(side=TOP, fill='x')
def sel_menu():
    root.config(menu="")
    menu_btn.config(command=menu_sel)
def menu_sel():
    root.config(menu=menubar)
    menu_btn.config(command=sel_menu)
    """
    #* COMING SOON NEXT UPDATE
    menus = Frame(root, bg=top_bg, bd=0, highlightthickness=0)
    code_frame.pack_forget()
    menus.pack(fill="x", side=TOP)
    code_frame.pack(fill="both", expand=True, pady=10, padx=10)
    file_lb = Label(menus, text=' File', font=(font_family, font_size), fg=fg, bg=top_bg)
    file_lb.grid(row=0, column=0)
    help_lb = Label(menus, text=' Help', font=(font_family, font_size), fg=fg, bg=top_bg)
    help_lb.grid(row=0, column=1)
    conf_lb = Label(menus, text=' Configure', font=(font_family, font_size), fg=fg, bg=top_bg)
    conf_lb.grid(row=0, column=2)
    themes_lb = Label(menus, text=' Themes/Fonts', font=(font_family, font_size), fg=fg, bg=top_bg)
    themes_lb.grid(row=0, column=3)
    """
def font_sel():
    set_appearance_mode("dark")
    fontselector = CTkInputDialog(text="Type a font or theme name (all simple)", title='Font and theme')
    outs = fontselector.get_input()
    if outs == "dracula":
        code_editor.config(highlighter='dracula')
        terminal_bg = "#292A36"
        terminal_bg_light = "#636582"
        xterm.config(bg=terminal_bg)
        xinput.config(bg=terminal_bg_light)
    elif outs == "monokai":
        terminal_bg = "#262626"
        terminal_bg_light = "#4C4C4C"
        xterm.config(bg=terminal_bg)
        xinput.config(bg=terminal_bg_light)
        code_editor.config(highlighter='monokai')
    elif outs == "consolas": change_font("Consolas")
    elif outs == "jetbrains mono": change_font("JetBrains Mono")
    elif outs == "firacode": change_font("Firacode")
    elif outs == "monospace": change_font("Monospace")
    set_appearance_mode("light")
open_btn = CTkButton(
    topbar, text="Open", text_font=('Helvetica', font_size),
    fg_color=bg, text_color=fg, hover_color=bg, command=open_file, border_width=1, border_color=black,
)
open_btn.pack(side=LEFT, pady=3, padx=3)
save_btn = CTkButton(
    topbar, text="Save", text_font=('Helvetica', font_size),
    fg_color=bg, text_color=fg, hover_color=bg, command=save_file, border_width=1, border_color=black,
)
save_btn.pack(side=LEFT, pady=3, padx=3)
files_label = Label(topbar, text=filenamee, bg=top_bg, fg=top_fg, font=('Helvetica', font_size))
files_label.place(relx=0.5, rely=0.5, anchor=CENTER)
fonts_btn = CTkButton(
    topbar, text="Fonts", text_font=('Helvetica', font_size),
    fg_color=bg, text_color=fg, hover_color=bg, command=font_sel, border_width=1, border_color=black,
)
fonts_btn.pack(side=RIGHT, pady=3, padx=3)
menu_btn = CTkButton(
    topbar, text="Menu", text_font=('Helvetica', font_size),
    fg_color=bg, text_color=fg, hover_color=bg, command=menu_sel, border_width=1, border_color=black,
)
menu_btn.pack(side=RIGHT, pady=3, padx=3)
menubar = Menu(root)
def save_as_file():
    save_sa = filedialog.asksaveasfilename(
        initialdir="/",
        title='Save as',
        filetypes=(("Python files", "*.py"), ("HTML Markup", "*.html"), ("JavaScript", "*.js"), ("All files", "*.*")),
    )
    with open(save_sa, "a+") as a:
        a.truncate()
        a.write(curr)
        a.close()
    print(save_sa)
def real_file_open():
    global filenamee
    askyes = messagebox.askyesno(ask_yes_heading, ask_yes_text)
    if askyes == False: pass
    else:
        v.file_path = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(("Python files", "*.py"), ("HTML Markup", "*.html"), ("JavaScript", "*.js"), ("All files", "*.*")),
        )
        if v.file_path != "":
            code_editor.delete(0.0, END)
            with open(v.file_path, "r") as file:
                filenamee = ntpath.basename(v.file_path)
                code_editor.insert(0.0, file.read())
                files_label.config(text=filenamee)
                file_lab.config(text=filenamee)
                root.title(f"{name} - {filenamee}")           
def e_real_file_open():
    global filenamee
    v.file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("Python files", "*.py"), ("HTML Markup", "*.html"), ("All files", "*.*")),
    )
    if v.file_path != "":
        code_editor.delete(0.0, END)
        with open(v.file_path, "r") as file:
            filenamee = ntpath.basename(v.file_path)
            code_editor.insert(0.0, file.read())
            files_label.config(text=filenamee)
            file_lab.config(text=filenamee)
            file_lab.config(text=filenamee)
            root.title(f"{name} - {filenamee}")
file_menu = Menu(menubar)
file_menu.add_command(label="New", command=lambda: code_editor.delete(0.0, END))
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")
def help():
    messagebox.showinfo("Help", "Go to github.com/ORCIM and ask a question on the disscussion, or email pycodes.10@gmail.com")
def about():
    messagebox.showinfo("About", "Orcim is a Python code editor, it is a free software, and it is open source. It is a decently powerfull Tkinter Code editor.")
def version():
    messagebox.showinfo("Version", "DEVELOPEMENT ALPHA V.1.0")
help_menu = Menu(menubar)
help_menu.add_command(label="Help", command=help)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Version", command=version)
def theme_set(theme):
    code_editor.config(highlighter=theme)
    if theme == "dracula":
        terminal_bg = "#292A36"
        terminal_bg_light = "#636582"
        xterm.config(bg=terminal_bg)
        xinput.config(bg=terminal_bg_light)
        code_editor.config(highlighter='dracula')
    elif theme == "monokai":
        terminal_bg = "#262626"
        terminal_bg_light = "#4C4C4C"
        xterm.config(bg=terminal_bg)
        xinput.config(bg=terminal_bg_light)
        code_editor.config(highlighter='monokai')
def asktheme():
    theme_window = Toplevel(root)
    theme_window.title("Theme Selector")
    if platform.system() == "Linux":
        tentry = CTkEntry(master=theme_window, placeholder_text="Search for a pygments highlighter theme?", text_font=("Arial", 14))
        tentry.pack(fill='x', pady=10, padx=10)
        theme_window.geometry("440x75")
    else:
        tentry = ttk.Entry(master=theme_window, font=("Arial", 14))
        tentry.pack(fill='x', pady=10, padx=10)
        theme_window.geometry("400x75")
    theme_window.resizable(False, False)
def lang_set(langs, flang):
    code_editor.config(language=langs)
    lang_lab.config(text=flang)
    print(f"Language set to {langs}")
def all_langs():
    lags = [
        "Ada", "Bash", "Batch", "C", "CMake", "CofeeScript", "CSS", "C#", "C++", "Dart", "Delphi", "Dockerfile", "Fortan", "Go",
        "Groovy", "Haskell", "HTML", "Java", "Javascript", "JSON", "Kotlin", "Lisp", "Lua", "Matlab", "Makefile", "NASM", "Objective-C",
        "Perl", "PHP", "Powershell", "Python", "R", "Ruby", "Swift", "SQL", "Tcl", "TypeScript", "Vim", "YAML"
    ]
    messagebox.showinfo("ALl languages", lags)
def search_for(search_term):
    if search_term == "Ada": lang_set("ada", "Ada")
    elif search_term == "Bash": lang_set("bash", "Bash")
    elif search_term == "Batch": lang_set("batch", "batch")
    elif search_term == "C": lang_set("c", "C")
    elif search_term == "CMake": lang_set("cmake", "CMake")
    elif search_term == "CoffeeScript": lang_set("coffeescript", "CoffeeScript")
    elif search_term == "CSS": lang_set("css", "CSS")
    elif search_term == "C#": lang_set("csharp", "C#")
    elif search_term == "C++": lang_set("cpp", "C++")
    elif search_term == "Dart": lang_set("dart", "Dart")
    elif search_term == "Delphi": lang_set("delphi", "Delphi")
    elif search_term == "Dockerfile": lang_set("dockerfile", "Dockerfie")
    elif search_term == "Fortran": lang_set("fortran", "Fortan")
    elif search_term == "Go": lang_set("go", "Go")
    elif search_term == "Groovy": lang_set("groovy", "Groovy")
    elif search_term == "Haskell": lang_set("haskell", "Haskell")
    elif search_term == "HTML": lang_set("html", "HTML")
    elif search_term == "Java": lang_set("java", "Java")
    elif search_term == "JavaScript": lang_set("javascript", "JavaScript")
    elif search_term == "JSON": lang_set("json", "JSON")
    elif search_term == "Kotlin": lang_set("kotlin", "Kotlin")
    elif search_term == "Lisp": lang_set("lisp", "Lisp")
    elif search_term == "Lua": lang_set("lua", "Lua")
    elif search_term == "Matlab": lang_set("matlab", "Matlab")
    elif search_term == "Makefile": lang_set("makefile", "Makefile")
    elif search_term == "Assembly (Nasm)": lang_set("nasm", "Assembly")
    elif search_term == "Objective-C": lang_set("objectivec", "Objecive-C")
    elif search_term == "Perl": lang_set("perl", "Perl")
    elif search_term == "PHP": lang_set("php", "PHP")
    elif search_term == "PowerShell": lang_set("powershell", "PowerShell")
    elif search_term == "Python": lang_set("python", "Python")
    elif search_term == "R": lang_set("r", "R")
    elif search_term == "Ruby": lang_set("ruby", "Ruby")
    elif search_term == "Swift": lang_set("swift", "Swift")
    elif search_term == "SQL": lang_set("sql", "SQL")
    elif search_term == "Tcl": lang_set("tcl", "TCL")
    elif search_term == "TypeScript": lang_set("typescript", "TypeScript")
    elif search_term == "Vim": lang_set("vim", "Vim")
    elif search_term == "YAML": lang_set("yaml", "YAML")
    else: 
        messagebox.showerror("Not found", f"{search_term} is not a valid language we can search for")
def search():
    search_window = Toplevel(root)
    search_window.title("Syntax Language Selector")
    if platform.system() == "Linux":
        search_entry = CTkEntry(master=search_window, placeholder_text="Search for a language, eg: python", text_font=("Arial", 14))
        search_entry.pack(fill='x', pady=10, padx=10)
        search_window.geometry("440x100")
    else:
        search_entry = ttk.Entry(master=search_window, font=("Arial", 14))
        search_entry.pack(fill='x', pady=10, padx=10)
        search_window.geometry("400x100")
    search_window.resizable(False, False)
    search_frame = Frame(search_window)
    search_frame.pack(fill='x', pady=10, padx=10)
    python_btn = ttk.Button(search_frame, text="Python", command=lambda: lang_set("python", "Python"))
    python_btn.grid(row=0, column=0)
    javascript_btn = ttk.Button(search_frame, text="JS", command=lambda: lang_set("javascript", "JavaScript"))
    javascript_btn.grid(row=0, column=1)
    html_btn = ttk.Button(search_frame, text="HTML", command=lambda: lang_set("html", "HTML"))
    html_btn.grid(row=0, column=2)
    typescript_btn = ttk.Button(search_frame, text="View", command=lambda: all_langs())
    typescript_btn.grid(row=0, column=3)
    java_btn = ttk.Button(search_frame, text="Java", command=lambda: lang_set("java", "Java"))
    java_btn.grid(row=0, column=4)
    search_entry.bind("<Return>", lambda event: search_for(search_entry.get()))
def submit():
    text = xinput.get()
    print(text)
    output = subprocess.Popen(text, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = output.communicate()
    print(output)
    xterm.config(state=NORMAL)
    xterm.delete(1.0, END)
    xterm.insert(END, output)
    xterm.config(state=DISABLED)
    xinput.delete(0, END)
def fun_terminal():
    global terminal, xinput, xterm
    terminal.pack(fill='both', side=BOTTOM, pady=7, padx=7)
    fs = font_size-3
    xinput = Entry(terminal, bg=terminal_bg_light, fg=terminal_fg, font=(font_family, fs), bd=0, highlightthickness=0)
    xinput.pack(fill='x', side=BOTTOM, pady=1, padx=1)
    xinput.bind("<Return>", lambda event: submit())
    xterm = Text(terminal, bg=terminal_bg, fg=terminal_fg, font=(font_family, fs), height=7, bd=0, highlightthickness=0)
    xterm.insert(1.0, 'This is not a proper terminal. Inputs and TUI will not work')
    xterm.config(state=DISABLED)
    xterm.pack(anchor='w', fill='both', expand=1, pady=1, padx=1)
lang_menu = Menu(menubar)
lang_menu.add_command(label="Language Syntax Search", command=lambda: search())
lang_menu.add_command(label="Terminal (OFF)", command=lambda: terminal.pack_forget())
lang_menu.add_command(label="Terminal (ON)", command=lambda: terminal.pack(fill='both', side=BOTTOM, pady=7, padx=7))
def write():
    print("URMOM")
theme_menu = Menu(menubar)
theme_menu.add_command(label="Monokai", command=lambda: theme_set("monokai"))
theme_menu.add_command(label="Dracula", command=lambda: theme_set("dracula"))
theme_menu.add_separator()
theme_menu.add_command(label="Consolas", command=lambda: change_font("Consolas"))
theme_menu.add_command(label="JetBrains Mono", command=lambda: change_font("JetBrains Mono"))
theme_menu.add_command(label="Source Code", command=lambda: change_font("Source Code"))
theme_menu.add_command(label="Firacode", command=lambda: change_font("Firacode"))
theme_menu.add_command(label="Monospace", command=lambda: change_font("Monospace"))
def change_font(fonts):
    global font_family
    font_family = fonts
    code_editor.config(font=(font_family, font_size))
    font_label.config(text=f"{font_family} {font_size}")
menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")
menubar.add_cascade(menu=lang_menu, label="Configure")
menubar.add_cascade(menu=theme_menu, label="Themes/Fonts")
bottom_bar = Frame(root, bg=white, bd=0, highlightthickness=0)
bottom_bar.pack(side=BOTTOM, fill='x')
file_lab = Label(bottom_bar, font=("Arial", 10), text=filenamee, bg=white)
file_lab.grid(row=0, column=0)
lang_lab = Label(bottom_bar, font=("Arial", 10), text=langs, bg='lightgrey')
lang_lab.grid(row=0, column=1)
font_label = Label(bottom_bar, font=("Arial", 10), text=f"{font_family} Size: {font_size} Terminal {fs}", bg=white)
font_label.grid(row=0, column=2)
code_frame.pack(fill="both", expand=True, pady=10, padx=10)
code_editor.pack(fill="both", expand=True, pady=1, padx=1)
def increase():
    global font_size, fs
    font_size += 1
    fs = font_size - 3
    print(font_size, fs)
    code_editor.config(font=(font_family, font_size))
    xinput.config(font=(font_family, fs))
    xterm.config(font=(font_family, fs))
    font_label.config(text=f"{font_family} Size: {font_size} Terminal {fs}")
def decrease():
    global font_size, fs
    font_size -= 1
    fs = font_size - 3
    print(font_size, fs)
    code_editor.config(font=(font_family, font_size))
    xinput.config(font=(font_family, fs))
    xterm.config(font=(font_family, fs))
    font_label.config(text=f"{font_family} Size: {font_size} Terminal {fs}")
def retrurns():
    pass
code_editor.bind("<Control-n>", lambda event: code_editor.delete(0.0, END))
code_editor.bind("<Control-o>", lambda event: open_file())
code_editor.bind("<Control-s>", lambda event: save_file())
code_editor.bind("<Control-Shift-S>", lambda event: save_as_file())
if platform.system() == 'Linux': code_editor.bind("<Control-equal>", lambda event: increase())
else: code_editor.bind("<Control-=>", lambda event: increase())
code_editor.bind("<Control-minus>", lambda event: decrease())
code_editor.bind("<Return>", lambda event: retrurns())
#code_editor.bind("<alt>", lambda event: menu_sel())
fun_terminal()
root.update()
root.mainloop()
\
