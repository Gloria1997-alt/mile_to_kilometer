from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# entry
input = Entry(width=10)
input.grid(column=1, row=0)
# print(input.get())

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0", )
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

button = Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)
#
window.mainloop()
