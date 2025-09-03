import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

wwidth = int(screenwidth / 2)
wheight = int(screenheight / 2)

root.geometry(f"{wwidth}x{wheight}")
root.title("")

container = ttk.Frame(root)
container.pack(expand=True, fill="both")

pages = {}

def show(name):
    for page in pages.values():
        page.pack_forget()
    pages[name].pack(expand=True, fill="both")

homepage = ttk.Frame(container)
pages["home"] = homepage
ttk.Label(homepage, text="hambox", font=("Courier One", 20)).pack(pady=10)
ttk.Label(homepage, text="Your Amateur Radio Toolbox", font=("Courier One", 12)).pack()

ttk.Separator(homepage, orient="horizontal").pack(fill="x", pady=20)

btnframe = ttk.Frame(homepage)
btnframe.pack(pady=10)

homebuttons = ["Operating Tools", "Mapping & DX", "Builders’ Tools", "Signal & Frequency Utilities", "Voice / Digital Helpers", "Reference"]

for i, text in enumerate(homebuttons):
    btn = ttk.Button(btnframe, text=text, command=lambda t=text: show(t), bootstyle=PRIMARY, width=25)
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

ttk.Separator(homepage, orient="horizontal").pack(fill="x", pady=20)
ttk.Label(homepage, text="or search below...").pack()

searchframe = ttk.Frame(homepage)
searchframe.pack(pady=10)
searchentry = ttk.Entry(searchframe, width=40)
searchentry.pack(side="left", padx=(0, 5), pady=(0, 10))
ttk.Button(searchframe, text="Search", bootstyle=SUCCESS).pack(pady=(0, 10), side="left")



page1 = ttk.Frame(container)
pages["Operating Tools"] = page1
ttk.Label(page1, text="qso page", font=("Courier One", 16)).pack(expand=True)
ttk.Button(page1, text="home", bootstyle=DANGER, command=lambda: show("home")).pack(pady=20)


root.update_idletasks()
h = homepage.winfo_reqheight()
root.geometry(f"{wwidth}x{h}")

show("home")
root.mainloop()
