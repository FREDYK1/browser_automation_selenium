import tkinter as tk
from main import WebAutomation
from tkinter import messagebox


class App:
    def __init__(self, root_name):
        self.root = root_name
        self.root.title("Web Automation GUI")

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.user_name = tk.Entry(self.login_frame)
        self.user_name.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.password = tk.Entry(self.login_frame)
        self.password.grid(row=1, column=1, sticky="ew")

        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.full_name = tk.Entry(self.form_frame)
        self.full_name.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.email = tk.Entry(self.form_frame)
        self.email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address").grid(row=3, column=0, sticky="w")
        self.current_address = tk.Entry(self.form_frame)
        self.current_address.grid(row=3, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address").grid(row=4, column=0, sticky="w")
        self.permanent_address = tk.Entry(self.form_frame)
        self.permanent_address.grid(row=4, column=1, sticky="ew")

        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)

        tk.Button(self.button_frame, text="Close", command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit_data(self):
        user_name = self.user_name.get()
        password = self.password.get()
        full_name = self.full_name.get()
        email = self.email.get()
        current_address = self.current_address.get()
        permanent_address = self.permanent_address.get()

        self.automation = WebAutomation()
        self.automation.login(user_name, password)
        self.automation.fill_form(full_name, email, current_address, permanent_address)
        self.automation.download_file()

    def close_browser(self):
        try:
            self.root.quit()
            self.automation.close_browser()
            messagebox.showinfo("Success", "Automation Done Successfully")
        except AttributeError:
            print("Done")

s= "FREDYKcode1"
root = tk.Tk()
app = App(root)
root.mainloop()