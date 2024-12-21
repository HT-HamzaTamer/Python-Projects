import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import requests
from tkcalendar import DateEntry

def update_tree_total():
    for item in tree.get_children():
        values = tree.item(item, "values")
        if len(values) > 2 and values[2] == "Total":
            tree.delete(item)
    
    total_in_usd = total_amount["USD"]
    total_row = tree.insert("", "end", values=(f"{total_in_usd:.2f}", "USD", "Total", "", ""))
    tree.item(total_row, tags=("total",))

    tree.tag_configure("total", background="yellow")

total_amount = {"USD": 0}

def add():
    try:
        amount = float(amount_text.get("1.0", tk.END).strip())
        currency = currency_dropdown.get()
        category = category_dropdown.get()
        payment_method = payment_dropdown.get()
        date = date_entry.get()

        tree.insert("", "end", values=(f"{amount:.2f}", currency, category, payment_method, date))
        convert_and_update_total(currency, amount)
        amount_text.delete("1.0", tk.END)
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")

def convert_and_update_total(currency, amount):
    headers = {"apikey": "Q2AoX9MWrE3GWW1RM9WvxsnnHsPELFB5"}
    try:
        url = f"https://api.apilayer.com/fixer/convert?to=USD&from={currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            converted_amount = data.get("result", 0)
            total_amount["USD"] += converted_amount  
            update_tree_total()
        else:
            print(f"Error converting {currency}: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Window 
window = tk.Tk()
window.geometry("680x450")
window.title("Expenses Tracker")

# Frames
frame = tk.Frame(window, width=680, height=165, bg="#ccc")
frame.place(x=0, y=0)

frame_col1 = tk.Frame(window, bg="#ccc")
frame_col1.place(x=135, y=30)

frame_col2 = tk.Frame(window, bg="#ccc")
frame_col2.place(x=385, y=30)

frame_info = tk.Frame(window)
frame_info.place(x=0, y=165)

# Labels and input 
amount_label = tk.Label(frame_col1, text="Amount", bg="#ccc")
amount_label.grid(row=1, column=1)

amount_text = tk.Text(frame_col2, width=20, height=1)
amount_text.grid(row=1, column=2)

currency_options = ["USD", "EUR", "GBP", "EGP"]
selected_currency = StringVar()
selected_currency.set(currency_options[0])

currency_label = tk.Label(frame_col1, text="Currency", bg="#ccc")
currency_label.grid(row=2, column=1)

currency_dropdown = ttk.Combobox(frame_col2, textvariable=selected_currency, values=currency_options, state="readonly", width=25)
currency_dropdown.grid(row=2, column=2)

category_options = ["Savings", "Food", "Transportation", "Clothes", "Rental", "Education", "Charity", "Grocery", "Gas", "Electricity"]
selected_category = StringVar()
selected_category.set(category_options[0])

category_label = tk.Label(frame_col1, text="Category", bg="#ccc")
category_label.grid(row=3, column=1)

category_dropdown = ttk.Combobox(frame_col2, textvariable=selected_category, values=category_options, state="readonly", width=25)
category_dropdown.grid(row=3, column=2)

payment_options = ["Cash", "Credit Card", "Debit Card", "Paypal"]
selected_payment = StringVar()
selected_payment.set(payment_options[0])

payment_label = tk.Label(frame_col1, text="Payment Method", bg="#ccc")
payment_label.grid(row=4, column=1)

payment_dropdown = ttk.Combobox(frame_col2, textvariable=selected_payment, values=payment_options, state="readonly", width=25)
payment_dropdown.grid(row=4, column=2)

date_label = tk.Label(frame_col1, text="Date", bg="#ccc")
date_label.grid(row=5, column=1)

date_entry = DateEntry(frame_col2, width=25, background="blue", foreground="white", borderwidth=2, date_pattern="dd-mm-yyyy")
date_entry.grid(row=5, column=2)

# Buttons
add_btn = tk.Button(frame_col2, text="Add Expense", width=15, bg="#ccc", command=add)
add_btn.grid(row=6, column=2, padx=2, pady=2)

# Expenses table
columns = ["Amount", "Currency", "Category", "Payment Method", "Date"]
tree = ttk.Treeview(frame_info, columns=columns, show="headings", height=11)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

window.mainloop()
