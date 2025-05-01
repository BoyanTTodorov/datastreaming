
# Using ttkbootstrap for not 80'sh tkinter look
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import numpy as np
from string import ascii_lowercase

class App(ttk.Window):
    def __init__(self, themename="darkly"):
        super().__init__(themename=themename)

        self.create_widgets()

    def create_widgets(self):

        self.title("Insert User into the Database")
        
        self.label = ttk.Label(self, text="", bootstyle="info")
        self.label.pack(pady=20)

        self.badgenum = ttk.Entry(self, bootstyle="info")
        self.badgenum.insert(0, "Badgenumber")
        self.badgenum.pack()

        self.username = ttk.Entry(self, bootstyle="info")
        self.username.insert(0, "Yourname")
        self.username.pack()

        self.email = ttk.Entry(self, bootstyle="info")
        self.email.insert(0, "email@mail.com")
        self.email.pack()

        self.button = ttk.Button(self, text="Click Me", bootstyle="success", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        #self.label.config(text="")
        badgenum = self.badgenum.get().strip()
        username = self.username.get().strip()
        email = self.email.get().strip()

        if not badgenum.isnumeric():
            self.label.config(text="Userbadge need to be numeric")
            self.badgenum.bootstyle="error"
        elif email.count('@') == 0:
            self.label.config(text="Email is not correct")
            self.email.bootstyle="error"
        else:
            pass # Query will go here

# Instantiate the App class
app = App()

# Run the application
app.mainloop()

class inputGenerator:
    def __init__(self, seed):
        self.randomseed = seed

    def generate_badge(self):
        return np.random.randint(1000, 10000, 1)
        
    def generate_name(self):
        return np.random.choice(1, np.random.randint(5,10,1), list(ascii_lowercase))
    
inp = inputGenerator(5)
print(inp.generate_name())