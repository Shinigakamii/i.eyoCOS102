import tkinter as tk
from tkinter import messagebox

# Parent class representing Zenith Bank
class Zenith:
    def unique_services(self):
        return []

    def mutual_services(self):
        return ["Lines of credit", "Investment management and accounts", "Insurance"]

# Subclass for Retail Banking
class RetailBanking(Zenith):
    def unique_services(self):
        return ["Retirement and education accounts", "Loans and mortgages", "Checking and saving"]

# Subclass for Global Banking
class GlobalBanking(Zenith):
    def unique_services(self):
        return ["Multi-currency management services and products", "Foreign currency accounts",
                "Foreign currency credit cards", "Transborder advisory services", "Liquidity management"]

# Subclass for Commercial Banking
class CommercialBanking(Zenith):
    def unique_services(self):
        return ["Advisory services"]

# Function to get the services based on division
def get_services(name, division):
    divisions = {
        "Retail Banking": RetailBanking,
        "Global Banking": GlobalBanking,
        "Commercial Banking": CommercialBanking
    }

    if division in divisions:
        division_obj = divisions[division]()
        services = division_obj.mutual_services() + division_obj.unique_services()
        services_str = '\n'.join(services)
        messagebox.showinfo("Services", f"{name} in {division} offers the following services:\n{services_str}")
    else:
        messagebox.showerror("Error", "Invalid Division Selected")

# Function to handle button click event
def on_submit():
    name = name_entry.get()
    division = division_var.get()
    if name and division:
        get_services(name, division)
    else:
        messagebox.showerror("Error", "Please enter all fields")

# Creating main window
root = tk.Tk()
root.title("Zenith Bank Services")

# Creating input fields and labels
tk.Label(root, text="Employee Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Division:").grid(row=1, column=0, padx=10, pady=10)
division_var = tk.StringVar(root)
division_var.set("Select Division")
division_menu = tk.OptionMenu(root, division_var, "Retail Banking", "Global Banking", "Commercial Banking")
division_menu.grid(row=1, column=1, padx=10, pady=10)

# Creating submit button
submit_button = tk.Button(root, text="Get Services", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

# Running the application
root.mainloop()