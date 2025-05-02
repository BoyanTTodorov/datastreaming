
# Using ttkbootstrap for not 80'sh tkinter look
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from input_generator import inputGenerator
from dbManager import dbManager



class App(ttk.Window):
    def __init__(self, themename="darkly"):
        super().__init__(themename=themename)

        self.create_widgets()

    def create_widgets(self):
        """
        Creating UI elements and assign function
        """
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

        self.btn_register = ttk.Button(self, text="Click Me", bootstyle="success", command=self.on_btn_register_click)
        self.btn_register.pack(pady=20)

        self.btn_generate_user = ttk.Button(self, text="GenerateUser",bootstyle="", command=self.on_btn_generate_user_click)
        self.btn_generate_user.pack()
        
    def on_btn_register_click(self):
        #self.label.config(text="")
        badgenum = self.badgenum.get().strip()
        username = self.username.get().strip()
        email = self.email.get().strip()

        if not badgenum.isnumeric():
            self.label.config(text="Userbadge need to be numeric")
        elif email.count('@') == 0:
            self.label.config(text="Email is not correct")
        else:
            path = r"user"
            dbmanager = dbManager(path)
            dbmanager.create(f"INSERT INTO user (badgenumber, username, email) VALUES(?,?,?)", [badgenum, username, email])

    def on_btn_generate_user_click(self):
        new_user = inputGenerator()
        # Debug prints to check the generated values
        print("Generating new user...")
        badge = new_user.generate_badge()
        name = new_user.generate_name()
        email = new_user.generate_email()
        print(f"Badge: {badge}, Name: {name}, Email: {email}")
        
        # Clear the existing content in the input fields
        self.badgenum.delete(0, 'end')
        self.username.delete(0, 'end')
        self.email.delete(0, 'end')
        
        # Insert the new values
        self.badgenum.insert(0, badge)
        self.username.insert(0, name)
        self.email.insert(0, email)

# Instantiate the App class
app = App()

# Run the application
app.mainloop()

