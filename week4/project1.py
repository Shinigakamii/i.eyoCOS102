import tkinter as tk

# Sample employee data (name, department)
employees = {
    "ADENIRAN	Oluwatamilore": "Logistics",
    "ADEWUMI	Ayomide":	"Accounting",
    "ADOH-AJAGBE	Oshim":	"Delivery",
    "AGBAKURU-NWOGU	Chukwunonye": "Accounting",
    "AGBAKWURU	Chiemeziem": "Logistics",
    "AKINDE	Oluwatimehin": "	Accounting",
    "ARNIKA	Osose": "Logistics",
    "ATELLY	Daniel": "Delivery",
    "AZOGU	Onyekachi": "Delivery",
    "BETURE	Shalom": "Delivery",
    "CHUKWUMA	Nedi": "Logistics",
    "EBI	Stephanie": "Accounting",
    "EGBORO	Jason": "Administration",
    "EJEDIMU	Edward": "Delivery",
    "ELERI	Otu": "Administration",
    "EZE	Onyinyechi": "Administration",
    "EZEONYE	Makuochukwu": "Logistics",
    "GIWA	Moyosore": "Logistics",
    "ICHA	Ayonete": "Accounting",
    "IKPATI	Eche": "Accounting",
    "ILOENYOSI": "Michael	Delivery",
    "IYAWE	Oluwadamilola": "Delivery",
    "NWOKOLO	Chijindu": "Logistics",
    "NWOTOKUBO	Joseph": "Logistics",
    "OBASOGIE	Daisy": "Accounting",
    "OBI 	Samuel": "Accounting",
    "OBIALOR	Betha": "Accounting",
    "OGBONNA	Boluwatife": "Delivery",
    "OIGBOCHIE	Mary": "Delivery",
    "OKOCHA-OJEAH	Raphael": "Administration",
    "OKOLO	Victor": "Administration",
    "OKORO	Derek": "Logistics",
    "OLOWOKERE	Akorede": "Accounting",
    "OLUBUADE	Rasheed": "Accounting",
    "OSEMEKE	Daniel": "Accounting",
    "OSSAI	Mary-Cynthia": "Logistics",
    "PETER	Owoede": "Logistics",
    "QUADRI	Oluwafikunmi": "Delivery",
    "UDE-IBE	Uchenna": "Delivery",
    "UMEH	Ejike": "Administration",

    
    "Jane Smith": "Operations",
    "Michael Johnson": "Logistics",
    "Emily Brown": "Operations",
    # Add more employees here
}

# Function to check if the user is an employee
def check_employee(name, department):
    if name in employees and employees[name] == department:
        return True
    else:
        return False

# Function to display employees in the same department
def display_department_members(department):
    members = [name for name, dept in employees.items() if dept == department]
    return members

# Function to handle button click event
def check_employee_and_display():
    name = name_entry.get()
    department = department_entry.get()

    if check_employee(name, department):
        message_label.config(text=f"Welcome, {name}!\nOther members in {department} department:\n{', '.join(display_department_members(department))}")
    else:
        message_label.config(text="Employee does not exist.")

# GUI setup
root = tk.Tk()
root.title("Employee Verification System")

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

department_label = tk.Label(root, text="Department:")
department_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

message_label = tk.Label(root, text="")
message_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

department_entry = tk.Entry(root)
department_entry.grid(row=1, column=1, padx=10, pady=5)

# Button
check_button = tk.Button(root, text="Check", command=check_employee_and_display)
check_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()