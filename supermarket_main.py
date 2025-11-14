#Supermarket Application with window
#Made by Kasra Tookallo in 2025

from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
from supermarket_module import *
from tkinter import ttk

product_list = []
def reset_form():
    id_number.set(len(product_list)+1)
    name.set("")
    brand.set("")
    quantity.set(0)
    price.set(0)
    expiration_date.set(str(date.today()))

def save():
    try:
        product = creat_products_and_validate(id_number.get() , name.get() , brand.get() , quantity.get() , price.get() , expiration_date.get())
        product_list.append(product)
        print(product, "Product saved successfully.")
        save_to_file(product_list)
        table.insert("" , END, values=tuple(product.values()))
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        reset_form()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong : {e}")

# total_price function attached to supermarket_module
def total_price():
    try:
        messagebox.showinfo("Total Price", f"Total : {calculate_total(product_list)}")
    except Exception as e:
        messagebox.showerror("Error", f"Error!!! : {e}")




window = Tk()
window.geometry("850x350")
window.title("Product Management")

# Identity Number
Label(window, text="ID num.").place(x=40, y=20)
id_number = IntVar()
Entry(window, textvariable=id_number , state="readonly").place(x=180, y=20)

# Name
Label(window, text="Name").place(x=40, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=180, y=60)

# Brand
Label(window, text="Brand").place(x=40, y=100)
brand = StringVar()
Entry(window, textvariable=brand).place(x=180, y=100)

# Quantity
Label(window, text="Quantity").place(x=40, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=180, y=140)

# Price
Label(window, text="Price").place(x=40, y=180)
price = DoubleVar()
Entry(window, textvariable=price).place(x=180, y=180)

# Expire date
Label(window, text="Expire date\n(yyyy/mm/dd)").place(x=40, y=220)
expiration_date = StringVar()
Entry(window, textvariable=expiration_date).place(x=180, y=220)

# Buttons
Button(window, text="Submit", command=save).place(x=40, y=300, width=100)
Button(window, text="Total", command=total_price).place(x=200, y=300, width=100)

table  = ttk.Treeview(window , columns=(1,2,3,4,5,6) , height = 14 ,show = "headings")
table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Quantity")
table.heading(5, text="Price")
table.heading(6, text="Expiration date")

table.column(1, width=80)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=50)
table.column(5, width=50)
table.column(6, width=100)

table.place(x=350,y=20)

reset_form()

window.mainloop()
