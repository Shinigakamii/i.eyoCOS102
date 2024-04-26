import tkinter as tk
from tkinter import messagebox

class PanAtlanticCafeteria:
    def __init__(self, master):
        self.master = master
        master.title("Pan Atlantic Cafeteria Order Menu")

        self.menu = {
            "Jollof Rice": 350,
            "Coconut Fried Rice": 350,
            "Jollof Spaghetti": 350,
            "Sweet Chil Chicken": 1200,
            "Grilled Chicken Wings": 400,
            "Fried Beet": 400,
            "Fried Fish": 500,
            "Boiled Egg": 200,
            "Sauteed Sausages": 200,
            "Savoury Beans": 350,
            "Roasted Sweet Potatoes": 300,
            "Fried Plantains": 150,
            "Mixed Vegetable Salad": 150,
            "Boiled Yam": 150,
            "Eba": 100,
            "Poundo Yam": 100,
            "Semo": 100,
            "Atama Soup": 450,
            "Egusi Soup": 480,
            "Water": 200,
            "Glass Drink (35cl)": 150,
            "PET Drink (50cl)": 300,
            "Glass/Canned Malt": 500,
            "Fresh Yo": 600,
            "Pineapple Juice": 350,
            "Mango Juice": 350,
            "Zobo Drink": 350,
            "Sandwich": 350,
            "Sandwich": 350,
            
            
         
        }

        self.order = {}
        self.total = 0

        self.label = tk.Label(master, text="Welcome to the Pan Atlantic Cafeteria")
        self.label.pack()

        self.menu_label = tk.Label(master, text="Menu:")
        self.menu_label.pack()

        for item, price in self.menu.items():
            self.menu_item = tk.Label(master, text=f"{item}: N{price}")
            self.menu_item.pack()

        self.name_label = tk.Label(master, text="Please enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.item_label = tk.Label(master, text="Enter food item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(master)
        self.item_entry.pack()

        self.quantity_label = tk.Label(master, text="Enter quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        self.order_button = tk.Button(master, text="Place your order", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        name = self.name_entry.get()
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())

        if item in self.menu:
            price = self.menu[item] * quantity
            self.order[item] = price
            self.total += price
            messagebox.showinfo("Order Placed", f"Order placed for {quantity} {item}(s) by {name}")

            discount = self.calculate_discount(self.total)
            total_with_discount = self.total - discount

            messagebox.showinfo("Total amount", f"Total amount: N{total_with_discount}")

        else:
            messagebox.showerror("Sorry", "We don't have this on the menu. Please place another order.")

    def calculate_discount(self, total):
        if total < 1000:
            return 0
        elif total < 2500:
            return total * 0.1
        elif total < 5000:
            return total * 0.15
        else:
            return total * 0.25

root = tk.Tk()
app = PanAtlanticCafeteria(root)
root.mainloop()