import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    location = location_var.get()
    weight = weight_var.get()
    
    if location == "Ibeju-Lekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "Epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        messagebox.showerror("Error", "Invalid location")
        return

    messagebox.showinfo("Charge", f"You need to pay N{charge}")

# Create GUI window
window = tk.Tk()
window.title("Simi Services Delivery Charge Calculator")

# Add labels and entry widgets
location_label = tk.Label(window, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=5)

location_var = tk.StringVar()
location_var.set("Ibeju-Lekki")
location_entry = tk.Entry(window, textvariable=location_var)
location_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5)

weight_var = tk.IntVar()
weight_entry = tk.Entry(window, textvariable=weight_var)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

# Add calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_charge)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

window.mainloop()