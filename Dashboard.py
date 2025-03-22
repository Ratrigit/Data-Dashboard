import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# Set the color cycle for the plots
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["blue", "white", "brown", "violet", "green"])

# Create the first figure for product sales
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Product Sales")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

# Create the second figure for product inventory
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Product Inventory")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")

# Create the third figure for product pie chart
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Product Pie Chart")

# Create the fourth figure for year sales
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Yearly Sales")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")

# Create the fifth figure for monthly inventory
fig5, ax5 = plt.subplots()
ax5.fill_between(list(inventory_month_data.keys()), inventory_month_data.values())
ax5.set_title("Monthly Inventory")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")

# Create a window and add charts
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

side_frame = tk.Frame(root, bg="#4c2a85")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()