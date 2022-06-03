import subprocess, sys, time
from rich.console import *
from rich.syntax import Syntax
PYTHON_TARGET = sys.executable
agrs = sys.argv
try:
    filename = agrs[1]
    compile_py = agrs[2]
    try:
        speed = agrs[3]
    except Exception as em:
        speed = "slow"
        print(em)
    print(filename, compile_py, speed)
except Exception:
    print("""usage: IJP [-h] ijp_file compilation_py
VERSION INFO: Varson Alpha Next 1
positional arguments:
  ijp_file          What file to read IJP code from
  compilation_py    Compilation target, what file to compile to?
optional arguments:
  -h, --help    show this help message and exit
  -v --version  show version info
  -d --docs     load mkdocs server for documentation
  """)
    sys.exit()
code = open(filename, "r")
codes = code.readlines()
imports = "from tkinter import *\nfrom tkinter import colorchooser\nfrom tkinter import messagebox\nfrom tkinter import filedialog\nfrom tkinter import ttk"
"""
DIFFERENCES
write("hello world") --> print("hello world")
fun name(): --> def name():
imp --> import
fr --> from
write --> print
tksuper root title geometry color
OOP --> hell
"""
lines = []
console = Console()
class error:
    def __init__(self, type, line_num, content) -> None:
        self.type = type
        line_num = line_num
        self.content = content
    def invalidLangError(type, line_num, content):
        error_line = f"{type} on line {line_num}: {content}"
        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic blue]You can use [italic green]#/ijp python[italic blue] [italic red](or "py" or "python" based on what the python command is on your laptop)[italic blue] to help you fix this error.')
        sys.exit()
    def MissingArgument(type, content):
        error_line = f"{type}: {content}"
        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic blue]Please define a [italic green]variable name and "=" and content[italic blue] [italic red]for example: var name = "Joe"')
        sys.exit()
    def tksuper(type, content):
        error_line = f"{type}: {content}"
        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic green]Example: tksuper root title geometry color')
        sys.exit()
def check_space(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count
def parse(line):
    line_whitespace = line.lstrip()
    if line_whitespace.startswith("write(") == True:
        if line.endswith(")") == True: line = line.replace(f"write", "print", 1)
    elif line_whitespace.startswith("fun ") == True:
        if line.endswith(":") == True: line = line.replace("fun ", "def ", 1)
    elif line_whitespace.startswith("OOP") == True:
        if line.endswith(":") == True: line = line.replace("OOP", "class", 1)
    elif "ijp_version" in line_whitespace:
        line = line.replace("ijp_version", "'Version [Alpha] 2.2.1'")
    elif line_whitespace.startswith("// "):
        line = line.replace("// ", '# ')
    elif line_whitespace == "sepr":
        line = line.replace('sepr', "print('')")
    elif line_whitespace.startswith("init(") == True:
        if line.endswith(":") == True: line = line.replace("init", "def __init__")
    elif line_whitespace.startswith("imp ") == True:
        if line == "imp tkall": line = line.replace(line, imports)
        line = line.replace("imp", "import", 1)
    elif line.startswith("fr ") == True:
        line = line.replace("fr", "from", 1)
    elif line_whitespace.startswith("cstr") or line_whitespace.startswith("cint") or line_whitespace.startswith("cfloat") or line_whitespace.startswith("cbool"):
        line_list = line.split(" ")
        line_list = [x for x in line_list if x != ""]
        try:
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])
            prev = f"{types} {name} = {content}"
            new = f"{name} {identifier} str({content})"
            line = line.replace(prev, new, 1)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)
    elif line_whitespace.startswith("init(") == True:
        line = line.replace("init(", "def __init__(:", 1)
    elif line_whitespace.startswith("onexec:") == True:
        line = line.replace('onexec:', 'if __name__ == "__main__":', 1)
    elif line_whitespace == "#/ijp strict_variables":
        strict_var = """class var(object):
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
v = var()"""
        line = line.replace("#/ijp strict_variables", strict_var)
    elif line_whitespace.startswith("var"):
        line_list = line.split(" ")
        line_list = [x for x in line_list if x != ""]
        try:
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])
            prev = f"{types} {name} = {content}"
            new = f"v.{name} = {content}"
            line = line.replace(prev, new)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)
    elif line_whitespace.startswith("tksuper "):
        lists = line.split(" ")
        lists = [x for x in lists if x != ""]
        try:
            var_root = lists[1]
            var_title = lists[2]
            var_size = lists[3]
            var_color = lists[4]
            print(var_root)
            line = f'''{var_root} = Tk()
root.title({var_title})
root.geometry({var_size})
root.configure(bg={var_color})'''
        except Exception:
            line_num = lists[0]
            error.TkSuper("Rw, WindowTitle, WindowSize, and WindowColor missing", line)
    line = line.replace("#/ijp python", "#/ijp python compiled")
    if line_whitespace.startswith("# ") != True:
        if line_whitespace != "":
            if speed == "slow": console.log(line)
            elif speed == "--slow": console.log(line)
            elif speed == "--fast": pass
            elif speed == "--med": pass
            else: console.log(line)
            lines.append(line)
start = time.time()
for line in codes:
    line = line.replace("\n", "")
    parse(line)
with open(compile_py, "w") as file:
    file.seek(0)
    file.truncate()
    file.close()
for x in lines:
    files = open(compile_py, "a")
    files.write(f"{x}\n")
files.close()
my_code = open(compile_py, "r")
my_codes = my_code.read()
my_code.close()
def output_code():
    syntax = Syntax(my_codes, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
def run_code():
    if speed == "--med":
        console.log(lines)
    end = time.time()
    subprocess.run([PYTHON_TARGET, compile_py])
    console.log(f"Total compilation time {end - start}, speed: {speed}")
if __name__ == '__main__':
    if codes[0] == "#/ijp python\n": pass
    elif codes[0] != "#/ijp python\n":
        error.invalidLangError("Invalid IJP code", "1", codes[0])
        sys.exit()
    try:
        run_code()
        pass
    except Exception as pyerror:
        print(pyerror)
